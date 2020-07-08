#!/usr/bin/env python
# coding: utf-8

# In[1]:


# to find the additional trace of a square matrix using python
def swapDiagonal(matrix): 
    '''
    function used to swap the diagonals of the given matrix
    '''     
    for i in range(R): 
          
        matrix[i][i], matrix[i][R-i-1] =             matrix[i][R-i-1], matrix[i][i]

        
import numpy as np 
  
R = int(input("Enter the size of the square matrix :"))

print("Enter the entries in a single line (separated by space): ") 
  
# User input of entries in a  
# single line separated by space 
entries = list(map(int, input().split())) 
  
# For printing the matrix 
matrix = np.array(entries).reshape(R, R) 
print(matrix)


# In[2]:


# swap diagonals of matrix 
swapDiagonal(matrix);
print(matrix)


# In[6]:


n = matrix.diagonal()
print(n)


# In[5]:


y = list(n)
print("y =",y)

import numpy
additional_trace = numpy.prod(y) 
print("The Additional trace =",additional_trace)
print("Manual multiplication of the elements of the list =",3*5*7)
print("Therefore Additional trace = multiplication of elements of the minor diagonal")


# In[ ]:




