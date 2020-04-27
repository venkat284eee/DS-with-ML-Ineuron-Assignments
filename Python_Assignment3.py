#!/usr/bin/env python
# coding: utf-8

# 1.1 Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()

# In[2]:


def myreduce(mylist):
    result = mylist[0]
    for x in mylist[1:]:
        result = result * x
    return result

mylist = [1, 2, 3, 4]
myreduce(mylist)


# 1.2 Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()
# 

# In[3]:


nums = [5, 12, 17, 18, 24, 32]

def myFunc(x):
      if x % 2 ==0:
        return True
      else:
        return False

even = filter(myFunc, nums)

for x in even:
  print(x, end=" ")


# 2. Implement List comprehensions to produce the following lists.
# Write List comprehensions to produce the following Lists
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],
# [4, 5, 6, 7], [5, 6, 7, 8]]
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

# In[4]:


def seq1():
    my_list = ['x','y','z']
    result = [ x*y for x in my_list for y in range(1,5)  ]
    print(str(result))
    return
    

def seq2():
    my_list = ['x','y','z']
    result = [ x*y for y in range(1,5) for x in my_list  ]
    print(str(result))
    return

def seq3():
    my_list = [2,3,4]
    result = [ [x+y] for x in my_list for y in range(0,3)]
    print(str(result))
    return

def seq4():
    my_list = [2,3,4,5]
    result = [ [x+y for x in my_list] for y in range(0,4)  ]
    print(str(result))
    return

def seq5():
    my_list=[1,2,3]
    result = [ (b,a) for a in my_list for b in my_list]
    print(str(result))

seq1()
seq2()
seq3()
seq4()
seq5()

