#!/usr/bin/env python
# coding: utf-8

# Question 1:¶
# 
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
# 

# In[1]:


for x in range(2000, 3201):
    if (x%7)==0:
        if (x%5)!=0:
            print(x, end =' ')


# Question 2:¶
# 
# Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

# In[4]:


print("Enter Firstname:")
f_name = input()
print("Enter Lastname:")
l_name = input()
print("Reverse order of the entered name is :" + l_name + " "+ f_name)


# Question 3:¶
# 
# Write a Python program to find the volume of a sphere with diameter 12 cm
# Formula: V=4/3 * π * r 3

# In[3]:


#Formula: V=4/3 * π * r 3
dia = 12
pi = (22/7)
radius = dia/2
vol = (4/3)*pi*(radius**3)
print("volume of sphere with diameter 12 cm is :" + str(vol))

