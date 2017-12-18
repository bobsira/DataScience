
# coding: utf-8

# In[1]:

# Python Crash Course
# Strings
data = 'hello world'
print(data[0])
print(len(data))
print(data)


# In[2]:

# Numbers
value = 123.1
print(value)
value = 10
print(value)


# In[3]:

# Boolean
a = True
b = False
print(a, b)


# In[4]:

# Multiple Assignment
a, b, c = 1, 2, 3
print(a, b, c)


# In[5]:

# No value
a = None
print(a)


# In[8]:

value = 99
if value == 99:
    print('That is fast')
elif value > 200:
    print('That is too fast')
else:
    print('That is safe')


# In[9]:

# For-Loop
for i in range(10):
    print(i)


# In[2]:

# While-Loop
i = 0
while i < 10:
    print(i)
    i = i + 1


# In[4]:

#Tuple
a = (1, 2, 3)
print(a)


# In[2]:

#list
mylist = [1, 2, 3]
print("Zeroth Value: %d" % mylist[0]) 
mylist.append(4)
print("List Length: %d" % len(mylist) ) 
for value in mylist:
    print(value)


# In[4]:

#Dictionary
mydict = {'a': 1, 'b': 2, 'c': 3}
print("A value: %d" % mydict['a']) 
mydict['a'] = 11
print("A value: %d" % mydict['a']) 
print("Keys: %s" % mydict.keys()) 
print("Values: %s" % mydict.values()) 
for key in mydict.keys():
    print(mydict[key])


# In[5]:

# Sum function
def mysum(x, y):
    return x + y
# Test sum function
result = mysum(1, 3)
print(result)


# In[6]:

#NumPy Crash Course
# define an array
import numpy
mylist = [1, 2, 3]
myarray = numpy.array(mylist)
print(myarray)
print(myarray.shape)


# In[7]:

# access values
import numpy
mylist = [[1, 2, 3], [3, 4, 5]]
myarray = numpy.array(mylist)
print(myarray)
print(myarray.shape)
print("First row: %s" % myarray[0]) 
print("Last row: %s" % myarray[-1]) 
print("Specific row and col: %s" % myarray[0, 2]) 
print("Whole col: %s" % myarray[:, 2]) 


# In[9]:

# arithmetic
import numpy
myarray1 = numpy.array([2, 2, 2])
myarray2 = numpy.array([3, 4, 3])
print("Addition: %s" % (myarray1 + myarray2))
print("Multiplication: %s" % (myarray1 * myarray2))


# In[10]:

#Matplotlib Crash Course
# basic line plot
import matplotlib.pyplot as plt
import numpy
myarray = numpy.array([1, 2, 3])
plt.plot(myarray)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()


# In[12]:

# basic scatter plot
import matplotlib.pyplot as plt
import numpy
x = numpy.array([1, 2, 3])
y = numpy.array([2, 4, 6])
plt.scatter(x,y)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()


# In[14]:

#Pandas Crash Course
#series
import numpy 
import pandas
myarray = numpy.array([1,2,3])
rownames = ['a', 'b', 'c']
myseries = pandas.Series(myarray, index=rownames)
print(myseries)


# In[15]:

print(myseries[0])
print(myseries['a'])


# In[16]:

# dataframe
import numpy
import pandas
myarray = numpy.array([[1, 2, 3], [4, 5, 6]])
rownames = ['a', 'b']
colnames = ['one', 'two', 'three']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)


# In[17]:

print("method 1:")
print("one column: %s" % mydataframe['one']) 
print("method 2:")
print("one column: %s" % mydataframe.one) 


# In[ ]:



