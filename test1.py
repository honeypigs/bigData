#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
csv_path = "./iris.csv"
test = pd.read_csv(csv_path)
test.info()


# In[8]:


test.head()


# In[10]:


test["Species"].value_counts()


# In[11]:


test.describe()


# In[17]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt 
test.hist(bins=100, figsize=(20,15)) 
plt.show()


# In[27]:


test.plot(kind="scatter", x="Petal.Length", y="Sepal.Length",alpha=0.5,s=test["Sepal.Width"], label="Sepal.Width",
         c="Petal.Width", cmap=plt.get_cmap("jet"), colorbar=True,)


# In[30]:


from pandas.plotting import scatter_matrix
attributes = ["Species", "Petal.Length", "Sepal.Length",
                  "Sepal.Width"]
scatter_matrix(test[attributes], figsize=(12, 8))


# In[ ]:




