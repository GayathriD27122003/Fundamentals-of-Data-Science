#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


student_data=pd.DataFrame({"Name": ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
"Age": [23, 25, 22, 24, 23],
"Gender": ['F', 'M', 'M', 'M', 'F'],
"Score": [85, 78, 92, 70, 88],
})


# In[4]:


#1.	Display the first three rows.
#2.	Filter out and display the rows where 'Gender' is 'F'.
#3.	Add  two columns Score1,Score2  which duplicates the Score column
#4.	Add a column Age1 which duplicates the Age column
#5.	Drop the Age1 column
#6.	Drop the Score1 and Score2 columns
#7.	Drop the row ai index 3
#8.	Filter out and display the rows where 'Gender' is 'F' ‘ and ‘Score’ is greater than 85.
#9.	Sort the DataFrame based on the 'Score' column in descending order.
#10.	Add a new column 'Grade' based on the 'Score' with the following criteria: 'A' for Score >= 90, 'B' for 80 <= Score < 90, 'C' for 70 <= Score < 80, 'D' for Score < 70.


# In[5]:


student_data.head(3)


# In[6]:


student_data[student_data["Gender"]=='F']


# In[7]:


student_data["Score1"]=student_data["Score"]
student_data["Score2"]=student_data["Score"]


# In[8]:


student_data


# In[9]:


student_data["Age1"]=student_data["Age"]


# In[10]:


student_data.drop(student_data[["Age1"]],axis=1,inplace=True)


# In[11]:


student_data.drop(student_data[["Score1"]],axis=1,inplace=True)


# In[12]:


student_data


# In[13]:


student_data.drop(student_data[["Score2"]],axis=1,inplace=True)


# In[14]:


student_data.drop(index=student_data.index[3], inplace=True)


# In[15]:


filtered_data = student_data[(student_data["Gender"] == 'F') & (student_data["Score"] >= 85)]


# In[16]:


filtered_data


# In[17]:


sorted_data = student_data.sort_values(by='Score', ascending=False)


# In[18]:


def determine_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'D'

student_data['Grade'] = student_data['Score'].apply(determine_grade)


# In[19]:


sales_data=pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar'],
 'Product': ['A', 'A', 'A', 'B', 'B', 'B'],
 'Sales': [150, 200, 250, 300, 400, 500],
})


# In[19]:


#1.	Group the data by 'Product' and calculate the total 'Sales' for each product.
#2.	Find the month with the highest sales for each product.
#3.	Add a new column 'Sales_Percentage' which represents the percentage contribution of each sale to the total sales of that product.


# In[22]:


product=sales_data.groupby("Product")["Sales"].sum()


# In[23]:


product


# In[40]:


maximum = sales_data.loc[sales_data["Sales"].idxmax()][0]


# In[41]:


maximum


# In[42]:


def percentag(x):
  if x=='A':
    return (x/600)*100
  else:
    return (x/1200)*100
sales_data["Sales_Percentage"]=sales_data["Sales"].apply(percentag)


# In[43]:


sales_data


# In[78]:


employee_data=pd.DataFrame({"Name": ['John', 'Doe', 'Jane', 'Anna', 'Smith'],
"Department": ['HR', 'Finance', None, 'IT', 'HR'],
"Salary": [50000, 60000, 55000, None, 58000]
})


# In[79]:


#1.	Identify and count the number of missing values in each column.
#2.	Fill the missing values in the 'Department' column with the mode of the column.
#3.	Fill the missing values in the 'Salary' column with the mean of the column.
#4.	Drop any rows that still contain missing values.


# In[80]:


employee_data.isnull().sum()


# In[81]:


mode1=employee_data["Department"].mode()[0]


# In[82]:


employee_data["Department"].fillna(mode1,inplace=True)


# In[83]:


employee_data


# In[85]:


mean1=employee_data["Salary"].mean()
mean1


# In[86]:


employee_data["Salary"].fillna(mean1,inplace=True)


# In[87]:


employee_data


# In[88]:


employee_data.isnull().sum()


# In[89]:


temperature=pd.Series([23, 21, 20, 25, 27, 30, 28, 22, 24, 26])


# In[ ]:


#1.	Calculate the mean, median, and standard deviation of the series.
#2.	Create a new Series temperature_celsius that converts the temperature from Fahrenheit to Celsius (temperature - 32) * 5/9
#3.	Find the index of the maximum and minimum values in the original temperature series.
#4.	Sort the Series in ascending and descending order.


# In[90]:


mean1=temperature.mean()
median1=temperature.median()
std1=temperature.std()


# In[92]:


mean1


# In[93]:


median1


# In[94]:


std1


# In[95]:


temperature1=(temperature-32)*5/9


# In[96]:


temperature1


# In[105]:


temperature.idxmax()


# In[106]:


temperature.idxmin()


# In[107]:


temperature.sort_values(ascending=True)


# In[108]:


temperature.sort_values(ascending=False)


# In[109]:


orders=pd.DataFrame({"OrderID": [1, 2, 3, 4, 5],
"CustomerID": [101, 102, 103, 104, 101],
"Product": ['A', 'B', 'A', 'C', 'B']
})


# In[110]:


customers=pd.DataFrame({"CustomerID": [101, 102, 103, 104],
"Name": ['Alice', 'Bob', 'Charlie', 'David'],
"Location": ['New York', 'Los Angeles', 'Chicago', 'Houston']
})


# In[ ]:


#1.	Merge the orders and customers DataFrames on the 'CustomerID' column.
#2.	Display the merged DataFrame.
#3.	Group the merged DataFrame by 'Location' and calculate the total number of orders from each location.


# In[111]:


merged=pd.merge(orders,customers,on="CustomerID")


# In[112]:


merged


# In[115]:


merged.groupby("Location")["Location"].count()


# In[ ]:




