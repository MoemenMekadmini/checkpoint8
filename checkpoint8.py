#!/usr/bin/env python
# coding: utf-8

# In[39]:


f= open("python.txt",'r',encoding = 'utf-8')
N = int(input("Enter  N lines: "))
filename = 'python.txt'
with open(filename) as file:
    head = file.readlines()[:N]
    print(head)
with open(filename) as file:
    last=file.readlines()[N:]
    print(last)
def count_words(filepath):
    with open(filepath) as f:
        data = f.read()
        data.replace(",", " ")
        return len(data.split(" "))
print(count_words("python.txt"))


# In[ ]:





# In[ ]:





# In[ ]:




