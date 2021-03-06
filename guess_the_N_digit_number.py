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

i = 0
n = 7 # Note: it finds the solution for 4, 5, 7 digits. for other digits, either there's no solution 
# or there should be a better way to code
test = np.random.randint(0, n - 1, n)
all_values = np.zeros(n, dtype=int)

power_limit = np.power(n, n)
test_limit = (250000 if power_limit > 250000 else power_limit)

while i < test_limit:
    correct_values = np.zeros(n, dtype=int)
    all_values=np.append(all_values, test)
    
    i+=1
    for j in range(n):
        if np.count_nonzero(test == j) == test[j]:
            correct_values[j] = 1
        else:
            break
            
    if np.count_nonzero(correct_values == 1) == n:
        print("At which attempt the solution found: " + str(i))
        print(test)
        break
    
    test = np.random.randint(0, n - 1, n)
    
all_values_shaped=all_values.reshape(int(len(all_values)/n), n)
print('Unique random arrays generated: ' + str(len(np.unique(all_values_shaped, axis=0))))
print('correct_values: ' + str(correct_values))

