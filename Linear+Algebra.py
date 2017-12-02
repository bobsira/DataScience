
# coding: utf-8

# In[22]:

from __future__ import division # want 3 / 2 == 1.5
import re, math, random # regexes, math functions, random numbers
import matplotlib.pyplot as plt # pyplot
from collections import defaultdict, Counter
from functools import partial


# In[1]:

height_weight_age = [70, # inches,
                     170, # pounds,
                     40 ] # years


# In[2]:

grades = [95, #exam1
            80,#exam2
             75,#exam3
             62 #exam4
         ]


# In[23]:

def vector_add(v, w):
    """adds two vectors componentwise"""
    return [v_i + w_i for v_i, w_i in zip(v,w)]


# In[24]:

def vector_subtract(v, w):
    """subtracts two vectors componentwise"""
    return [v_i - w_i for v_i, w_i in zip(v,w)]


# In[30]:

def vector_sum(vectors):
    """sums all corresponding elements"""
    result = vectors[0] #start with the first vector 
    for vector in vectors[1:]: #then loop over the others
        result = vector_add(result,vector) #and add them to the result
    return result
#def vector_sum(vectors):
    #return reduce(vector_add, vectors)
#vector_sum = partial(reduce, vector_add)


# In[31]:

vector_sum([ [1,2,3], [1,2,3], [1,2,3]])


# In[32]:

def scalar_multiply(c, v):
    """c is a number, v is a vector"""
    return [c * v_i for v_i in v]


# In[33]:

scalar_multiply(5,[2,4,1/5])


# In[34]:

# this isn't right if you don't from __future__ import division
def vector_mean(vectors):
    """compute the vector whose i-th element is the mean of the
    i-th elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


# In[38]:

vector_mean([ [1,2,3], [2,4,3], [3,2,7]])


# In[39]:

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


# In[40]:

dot([1,1],[2,1])


# In[41]:

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)


# In[44]:

sum_of_squares([1,2,3])


# In[45]:

def magnitude(v):
    return math.sqrt(sum_of_squares(v)) # math.sqrt is square root function


# In[51]:

magnitude([4,3])


# In[55]:

def squared_distance(v, w):
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(vector_subtract(v, w))


# In[56]:

def distance(v, w):
   return math.sqrt(squared_distance(v, w))


# In[57]:

distance([1,2,3],[3,6,7])


# In[58]:

A = [ [1,2,3],   # A has 2 rows and 3 columns
      [4,5,6] ]


# In[60]:

B = [   [1,2],  # B has 3 rows and 2 columns
        [3,4],
        [5,6]]


# In[ ]:

#Given this list-of-lists representation, the matrix A has len(A) rows and len(A[0])
#columns, which we consider its shape:


# In[61]:

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0  # number of elements in first row
    return num_rows, num_cols


# In[63]:

shape(B)


# In[64]:

def get_row(A, i):
    return A[i]  # A[i] is already the ith row


# In[65]:

def get_column(A, j):
    return [A_i[j]         # jth element of row A_i
            for A_i in A]  # for each row A_i


# In[66]:

get_row(A,1)


# In[67]:

get_column(A,1)


# In[68]:

A


# In[70]:

def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix 
    whose (i,j)-th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j)                 # given i, create a list
             for j in range(num_cols)]      # [entry_fn(i, 0), ... ]
            for i in range(num_rows)]       # create one list for each i


# In[71]:

def is_diagonal(i, j):
    """1's on the 'diagonal', 0's everywhere else"""
    return 1 if i == j else 0


# In[72]:

identity_matrix = make_matrix(5, 5, is_diagonal)


# In[73]:

identity_matrix


# In[74]:

#          user 0  1  2  3  4  5  6  7  8  9
#
friendships = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # user 0
               [1, 0, 1, 1, 0, 0, 0, 0, 0, 0], # user 1
               [1, 1, 0, 1, 0, 0, 0, 0, 0, 0], # user 2
               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0], # user 3
               [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], # user 4
               [0, 0, 0, 0, 1, 0, 1, 1, 0, 0], # user 5
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 6
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 7
               [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], # user 8
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]] # user 9


# In[76]:

friendships[0][2] == 1 # True, 0 and 2 are friends


# In[77]:

friendships[0][8] == 1 # False, 0 and 8 are not friends


# In[78]:

friends_of_five = [i                                             # only need
                    for i, is_friend in enumerate(friendships[5])# to look at
                    if is_friend]                                # one row


# In[80]:

friends_of_five


# In[ ]:

#book mark books to read

