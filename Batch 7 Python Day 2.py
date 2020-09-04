#!/usr/bin/env python
# coding: utf-8

# # List and its default fuctions

# In[3]:


Lst = [1,'a',1.5,"sud",[1,2,3]]


# In[4]:


Lst[0]


# In[13]:


Lst[0:]


# In[21]:


Lst[4]


# In[22]:


Lst[4][0]


# In[23]:


Lst[-1:]


# In[31]:


Lst[-2:]


# In[30]:


Lst[:-4]


# In[26]:


Lst[-5:]


# In[27]:


Lst[-6:]


# In[28]:


Lst[-10:]


# In[32]:


Lst[0:2]


# In[33]:


Lst+Lst


# In[6]:


Lst2 = [1,2]


# In[7]:


Lst2+Lst2


# In[8]:


Lst2*3


# In[9]:


Lst2.append(3)


# In[10]:


Lst2


# In[49]:


Lst2.count(1)


# In[13]:


Lst2


# In[14]:


Lst2.index(2)


# In[15]:


Lst2.insert(3,10)


# In[16]:


Lst2


# In[17]:


Lst2.pop(0)


# In[18]:


Lst2


# In[19]:


Lst2.remove(2)


# In[20]:


Lst2


# In[22]:


Lst2.reverse()


# In[23]:


Lst2


# # Dictionary and its defualt functions

# In[50]:


Dit = {"name":"Sud","Age":"35","Cell":"9930842130"}


# In[51]:


Dit


# In[52]:


Dit.get('name')


# In[53]:


Dit['name']


# In[54]:


Dit['name1']


# In[55]:


Dit.keys()


# In[56]:


Dit.values()


# In[57]:


Dit.fromkeys(Dict)


# In[58]:


Dit


# In[47]:


seq = ('name', 'age', 'sex')


# In[48]:


seq


# In[59]:


Dit.fromkeys(seq)


# In[60]:


Dit.fromkeys(seq,5)


# In[61]:


Dit.items()


# In[64]:


Dit


# In[72]:


Dit.pop('name')


# In[73]:


Dit


# In[75]:


Dit.popitem()


# In[76]:


Dit


# In[81]:


Dit1 = {"name":"sud"}


# In[82]:


Dit.update(Dit1)


# In[83]:


Dit


# In[84]:


Dit1 = {"name":"sud1"}


# In[85]:


Dit.update(Dit1)


# In[86]:


Dit


# #  Sets and its default functions
# 

# In[87]:


# Sets doesnot store duplicates


# In[88]:


set1 = {1, 2, 3, 4, 3, 2}


# In[90]:


set1


# In[99]:


set2 = {1, 2, 3, 1.0,4, 3,1.0, 2,"a",'a',1.1,1.2,1.3,1.1,1.2,1.3,"xyz",'aa','aa','xyz'}


# In[100]:


set2


# In[101]:


set2.add(34)


# In[102]:


set2


# In[104]:


set2.pop()


# In[105]:


set2


# In[106]:


set2.pop()


# In[107]:


set2


# In[108]:


set2.remove(1.1)


# In[109]:


set2


# In[113]:


set3 = (11,12)


# In[114]:


set2.update(set3)


# In[115]:


set2


# In[116]:


set2.union(set3)


# In[117]:


set2.intersection(set3)


# In[118]:


set2.difference(set3)


# # Tuple and explore default methods
# 

# In[120]:


tup = (1,2,3,4,5,[1,2,3])


# In[122]:


tup.count(1)


# In[123]:


tup.index(5)


# In[124]:


tup.index([1,2,3])


# # String and explore default methods

# In[4]:


str = "hello world"


# In[7]:


str.count("hello")


# In[8]:


str.capitalize()


# In[10]:


str.center(1)


# In[11]:


str.endswith("d")


# In[12]:


str.endswith("e")


# In[14]:


str.find("lo")


# In[16]:


str.index("e")


# In[17]:


str.islower()


# In[18]:


str1 ="   abc" 


# In[19]:


str1.lstrip()


# In[23]:


str.replace("hello","HELLO")


# In[ ]:




