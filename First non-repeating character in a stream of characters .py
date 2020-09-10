#!/usr/bin/env python
# coding: utf-8

# # Basic concept : 

# # 1. At first for first value we will input A[i] to q as there is no character before that character so it is first non repeating.

# # 2. Then we will check if A[i] is in q then we will insert it to L[] for keeping track of repeated value and remove for q

# # 3. And if A[i] is already in L[] then check if len(q) == 0, if yes then insert ' # ' else insert A[i] to q

# # 4.After each condition insert character to B like here " B=B+q[front]"

# In[56]:


A = "jpxvxivxkkthvpqhhhjuzhkegnzqriokhsgea"  #test input
front = 0   # for keeping track of first element of queue
B=''  #re quired string stored here ( empty string)
l=[]  # for keeping track of repeated character in given string
q=[]  # for queue based operations
for i in range(len(A)):
    if (i ==0):
        q.append(A[i])
        B=B+q[front]
        continue   
    elif(A[i] in q):
        l.append(A[i])
        q.remove(A[i])
    if (A[i] in l):
        if(len(q)==0):
            B=B+'#'
            continue
    else:
        q.append(A[i])
    if (len(A)==0):
        B=B+'#'
        continue
    B=B+q[front]
        
print(B)

