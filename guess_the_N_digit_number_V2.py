#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
It's a 5 digit number where 

1st digit denotes how many zeroes are there in the number
2nd digit denotes how many ones are there in the number
3rd digit denotes how many twos are there in the number
4th digit denotes how many threes are there in the number
5th digit denotes how many fours are there in the number

Can you guess the number?
'''

import numpy as np
import datetime

i = 0
n = 8 # Note: it finds the solution for 4, 5, 7 digits. for other digits, either there's no solution 
# or there should be a better way to code
test = np.random.randint(0, n - 1, n)
# the experiment for digits 4, 5, 7 and 8 shows that the max number is n/2+1 for any digit, 
# so no need to create a random number with the max value (n - 1) as earlier done. n/2+1 should be sufficient.
#test = np.random.randint(0, int(n/2) + 2, n)
all_values = np.zeros(n, dtype=int)
#print(test)

power_limit = np.power(n, n)
manual_limit = 20000000
test_limit = (manual_limit if power_limit > manual_limit else power_limit)
#print(int(n/2))

starttime = datetime.datetime.now()
print(datetime.datetime.now())

while i < test_limit:
    correct_values = np.zeros(n, dtype=int)
    # having the below check is too much costly when the digit>7, so it will be commented out. 
    # should only be used if n < 8
    #all_values=np.append(all_values, test)
    
    i += 1
    for j in range(n):
        if np.count_nonzero(test == j) == test[j]:
            correct_values[j] = 1
        else:
            break
            
    if np.count_nonzero(correct_values == 1) == n:
        print("At which attempt the solution found: " + str(i))
        print(test)
        break
    
    # to have an idea how fast/slow is the process and where we are, how far to the final test
    if i % int(test_limit/n) == 0:
        print("Total numbers have been tested until now: ", i)
        print("Total numbers will be tested if no solution is found: ", test_limit)
        print("So {}% of the test is done in the worst case.".format(i/test_limit*100))
        print(datetime.datetime.now())
    
    #test = np.random.randint(0, n - 1, n)
    test = np.random.randint(0, int(n/2) + 1, n)
    #print(test)
    
# should only be used if n < 8
#all_values_shaped=all_values.reshape(int(len(all_values)/n), n)

endtime = datetime.datetime.now()

# should only be used if n < 8
#print('Unique random arrays generated: ' + str(len(np.unique(all_values_shaped, axis=0))))
print('correct_values: ' + str(correct_values))
print('Calculation time: ' + str(endtime - starttime))

