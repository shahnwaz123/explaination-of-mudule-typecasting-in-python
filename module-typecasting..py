#!/usr/bin/env python
# coding: utf-8

# # Module in python

# In[3]:


#Module is a file consisting of python code.It can be defined functions,classes,and variablesa nd can also include runnable python code.


# In[4]:


# Two type of modules.

# 1.Inbuilt PIP
# 2.external pip


# In[5]:


# PIP- Package manager for python.


# # Run first python code

# In[7]:


print("hello world")


# In[8]:


# We are going to learn about comment,escape sequences and print statement.


# # Comment

# In[9]:


# A paragraph or sentence inside the coding just to explain the things not actually for command.


# In[10]:


# use (#)for turn a command into comment.


# # use of "end" command

# In[13]:


# End command basically use to end a statement and run statement just beside first statement.


# In[14]:


# example-


# In[15]:


print("hello world")
print("i am learning python")


# In[16]:


# now after using end command 


# In[17]:


print("hello world",end=",")
print("i am learning python")


# In[18]:


# example2.


# In[21]:


print("hello world",end=" ")
print("i am learning python")


# # Use of \n,\" and \t command 

# In[22]:


# how to use \n command.


# In[23]:


# it is basically use to start stement in new line.
# example


# In[25]:


print("i am learning\npython")


# In[26]:


# how to use \"" command.


# In[27]:


# It is basically use to place quotes inside a staemnet.


# In[38]:


print("i am learning\"python")


# In[39]:


# how to use \t command.


# In[40]:


# It is basically use to give tab or space between two words in a statement.


# In[41]:


# Example


# In[42]:


print("i am learning\tpython")


# # Variables

# In[43]:


# It is container in python where you can store the data types.
# Variables has name and type.


# In[44]:


# Example-


# In[46]:


var1 = "hello world"
print(var1)


# In[47]:


# var1 is work as ariable where "hello world" is stored.


# # Data type

# In[48]:


# there are various data type in python such as-

# 1.str="sam"
# 2.int=25
# 3.float=3.17
# 4.bool= True,False
# 5.Complex number=7+8j,9-6j


# # type casting

# In[49]:


# the method of changing one data type to anothet data type is called as type casting.


# In[51]:


# some type casting command are-
# 1.str()= for changing in str data type.
# 2.int()= for changig in integer data type.
# 3.float()= for changing in float data type.


# In[52]:


# let see some example


# In[54]:


var1=54
var2=56
print(type(var1))
print(type(var2))


# In[55]:


print(var1+var2)


# In[56]:


# now we are converting it into str.


# In[65]:


var1=54
var2=56
print(str(var1)+str(var2))


# In[66]:


var3="54"
var4="Mohit"


# In[67]:


print(type(var3)


# In[68]:


# Now we are going to cahange it into integers 


# In[69]:


print(var3+var4)


# In[73]:


var3="54"
var4="51"


# In[74]:


print(type(var3))
print(type(var4))


# In[72]:


print(int(var3)+int(var4))


# In[75]:


print(type(int(var3)+int(var4)))


# In[82]:


# how to print staement in multiple times,


# In[3]:


print(10 * "hello world\n")


# In[5]:


# We need to convert int in str for print it in multiple time


# In[20]:


print(10*(str(10)))


# In[ ]:




