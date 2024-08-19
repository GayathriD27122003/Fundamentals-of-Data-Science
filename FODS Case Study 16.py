#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dd=pd.read_excel('payroll_dataset.xlsx',sheet_name='Departments')
de=pd.read_excel('payroll_dataset.xlsx',sheet_name='Employees')


# In[3]:


merged_tab=pd.merge(de,dd,on='DepartmentID')
merged_tab.head(5)


# In[4]:


merged_tab.drop_duplicates()
merged_tab.head(5)


# In[5]:


q1=merged_tab['Salary'].quantile(0.75)
q3=merged_tab['Salary'].quantile(0.25)


# In[6]:


iqr=q3-q1
lb=q1-1.5*iqr
ub=q3+1.5*iqr


# In[7]:


outlier=(merged_tab[['Salary']]<lb)|( merged_tab[['Salary']]>ub)
outlier


# In[8]:


clean=(~merged_tab.isin(outlier))
clean


# In[9]:


sal_min=merged_tab['Salary'].min()
sal_max=merged_tab['Salary'].max()


# In[10]:


merged_tab['Salary']=(merged_tab['Salary']-sal_min)/(sal_max-sal_min)
merged_tab


# In[11]:


dummies=pd.get_dummies(merged_tab,columns=['Location'])
dummies


# In[12]:


dummies=pd.get_dummies(merged_tab,columns=['Location'],drop_first=False)
dummies


# In[ ]:




