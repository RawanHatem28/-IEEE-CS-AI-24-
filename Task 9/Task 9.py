#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


print(np.identity(3)*9)


# In[3]:


arr = np.array(range(1,33))
even_arr = arr[arr % 2 == 0]
mean = np.mean(even_arr)
std = np.std(even_arr)
half_std = 0.5 * std
lower_bound = mean - half_std
upper_bound = mean + half_std
filtered_values = (even_arr >= lower_bound) & (even_arr <= upper_bound)
print(lower_bound)
print(upper_bound)
print(even_arr)
print(filtered_values)
print(even_arr[filtered_values])


# In[4]:


print(np.zeros((9,9),dtype = int))


# In[8]:


n = int(input("Enter the value of n: "))
result = np.ones((n, 1), dtype = int) * np.arange(1, n + 1)
print("Resultant array: ")
print(result)


# In[12]:


matrix_dimention = input()
matrix_dimentions= matrix_dimention.split()
rows =[]
for i in range(int(matrix_dimentions[0])):
    row = input().split()
    row_array = np.array(row)
    if not row_array.size == int(matrix_dimentions[1]):
        print("invalid number of columns..")
        continue  
    rows.append(row_array)
    array = np.array(rows)
colored = np.where(((array == 'C') | (array == 'M')|(array == 'Y')))
if array[colored].size == 0:
    print("#Black&White")
else:
    print("#Color")


# In[14]:


matrix_dimention = input()
matrix_dimentions= matrix_dimention.split()
rows =[]
for i in range(int(matrix_dimentions[0])):
    row = input().split()
    row_array = np.array(row)
    if not row_array.size == int(matrix_dimentions[1]):
        print("invalid number of columns..")
        continue  
    rows.append(row_array)
    array = np.array(rows)
colored = np.where(((array == 'C') | (array == 'M')|(array == 'Y')))
if array[colored].size == 0:
    print("#Black&White")
else:
    print("#Color")


# In[15]:


def game_score(n,cards):
    sereja_score = 0
    dima_score = 0
    left = 0
    right = n-1
    
    while left <= right:
        if cards[left] > cards[right]:
            sereja_score += cards[left]
            left += 1
        else:
            sereja_score += cards[right]
            right -= 1
            
        if cards[left] > cards[right]:
            dima_score += cards[left]
            left += 1
        else:
            dima_score += cards[right]
            right -=1

        if left > right:
            break
    return sereja_score, dima_score


n = int(input())
cards = np.array(list(map(int,input().split())))
sereja_score, dima_score = game_score(n, cards)
print(sereja_score, dima_score)


# In[ ]:




