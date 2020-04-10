#!/usr/bin/env python
# coding: utf-8

# # Question 1:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple
# of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
# comma-separated sequence on a single line.

# In[1]:


for x in range(2000, 3201):
    if (x%7)==0:
        if (x%5)!=0:
            print(x, end =' ')


# # Question 2:
# Write a Python program to accept the user's first and last name and then getting them printed in
# the the reverse order with a space between first name and last name.

# In[2]:


print("Enter Firstname:")
f_name = input()
print("Enter Lastname:")
l_name = input()
print("Reverse order of the entered name is :" + l_name + " "+ f_name)


# # Question 3:
# Write a Python program to find the volume of a sphere with diameter 12 cm.

# In[3]:


#Formula: V=4/3 * π * r 3
dia = 12
pi = (22/7)
radius = dia/2
vol = (4/3)*pi*(radius**3)
print("volume of sphere with diameter 12 cm is :" + str(vol))


# # Question 4:
# Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list.

# In[4]:


print("Enter sequence of comma seperated numbers.")
values = input()
list1 = values.split(",")
print(list1)


# # Question 5:
# Create the below pattern using nested for loop in Python.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# In[5]:


n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# # Question 6:
# Write a Python program to reverse a word after accepting the input from the user.

# In[6]:


value = input("Enter a string: " )
for i in range(len(value) -1, -1, -1):
    print(value[i], end="")
print("\n")


# # Question 7:
# Write a Python Program to print the given string in the format specified in the sample output.
# WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
# SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
# its citizens
# 
# Sample Output:
# WE, THE PEOPLE OF INDIA,
# having solemnly resolved to constitute India into a SOVEREIGN, !
# SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
# and to secure to all its citizens

# In[4]:


str = """WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens"""
lst = str.split(" ")
val = len(lst)
x = lst[0]
print(x, end=" ")
for i in lst[1:val:1]:
    if i.isupper()==x.isupper():
        print(i, end=" ")
    elif i.islower()==x.islower():
        print(i, end=" ")
    else: print("\n", end="")
    x=i


# In[ ]:




