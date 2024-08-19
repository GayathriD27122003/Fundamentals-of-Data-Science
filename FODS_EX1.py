#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.DataFrame({"EmployeeID": [101, 102, 103, 104, 105], "Name": ['Alice', 'Bob', 'Charlie', 'David', 'Eva'], 'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'], 'Salary': [50000, 60000, 55000, 65000, 58000]
})


# In[3]:


df


# In[ ]:


#1.	Display the 'Name' and 'Salary' columns from the Employee_data DataFrame.
#2.	Find the average salary of employees in the 'IT' department.
#3.	Add a new column 'Bonus' where the bonus is 10% of the salary.
#4.	Rename the 'EmployeeID' column to 'ID'.
#5.	Drop the 'Department' column.


# In[4]:


df[["Name","Salary"]]


# In[7]:


df1=df[df["Department"]=="IT"]


# In[8]:


df1


# In[9]:


df1["Salary"].mean()


# In[10]:


df["Bonus"]=df["Salary"]*0.1


# In[14]:


df["EmployeeID"].rename("ID")


# In[17]:


df.drop(df[["Department"]],axis=1)


# In[18]:


sales_analysis=pd.DataFrame({"Month": ['Jan', 'Feb', 'Mar', 'Apr', 'May'], "Product_A": [150, 200, 250, 300, 350], "Product_B": [300, 250, 200, 150, 100]
})


# In[ ]:


#1.	Calculate the total sales for each product ('Product_A' and 'Product_B') in the sales_data DataFrame.
#2.	Find the month with the highest sales for Product_A.
#3.	Add a new column 'Total_Sales' which is the sum of 'Product_A' and 'Product_B'.
#4.	Normalize the 'Product_A' sales by dividing by the maximum sales.
#5.	Filter the DataFrame to show only months where total sales exceeded 400.


# In[26]:


sales_analysis["Total_sales"]=sales_analysis.iloc[:,1]+sales_analysis.iloc[:,2]


# In[29]:


sales_analysis


# In[30]:


sales_analysis["Product_A"]=sales_analysis["Product_A"]/sales_analysis["Product_A"].max()


# In[31]:


sales_analysis


# In[32]:


sales_analysis[sales_analysis["Total_sales"]>400]


# In[44]:


customer_data=pd.DataFrame({"CustomerID": [1, 2, 3, 4, 5], "Name": ['John', 'Jane', None, 'Alice', 'Bob'], "Purchase": [200, 300, 150, None, 500]
})


# In[45]:


customer_data


# In[46]:


#1.	Identify and count the number of missing values in each column of the customer_data DataFrame.
#2.	Fill the missing values in the 'Name' column with 'Unknown'.
#3.	Fill the missing values in the 'Purchase' column with the median of the column.
#4.	Drop any rows that still contain missing values.
#5.	Filter the DataFrame to show only customers who made purchases above the median value.


# In[47]:


customer_data.isnull().sum()


# In[50]:


customer_data["Name"].fillna("Unknown",inplace=True)


# In[51]:


customer_data


# In[52]:


customer_data["Purchase"].fillna(customer_data["Purchase"].median(),inplace=True)


# In[53]:


customer_data


# In[54]:


customer_data[customer_data["Purchase"]>customer_data["Purchase"].median()]


# In[55]:


temperature=pd.Series([23, 21, 20, 25, 27, 30, 28, 22, 24, 26])


# In[ ]:


#1.	Find the mean, median, and variance of the temperature series.
#2.	Create a new Series indicating whether each temperature is above or below the mean.
#3.	Convert the temperatures to a different scale (e.g., Kelvin, K = C + 273.15).
#4.	Calculate the rolling mean with a window size of 3.
#5.	Filter out temperatures that are within one standard deviation of the mean.


# In[56]:


temperature.mean()


# In[57]:


temperature.median()


# In[58]:


temperature.var()


# In[59]:


temperature1=pd.Series(temperature>temperature.mean())


# In[60]:


temperature1


# In[61]:


temperature=temperature+273.15


# In[62]:


temperature


# In[63]:


rolling_mean=temperature.rolling(window=3).mean()


# In[64]:


rolling_mean


# In[65]:


mean=temperature.mean()


# In[68]:


std=temperature.std()


# In[69]:


lower_bound=mean-std
upper_bound=mean+std


# In[70]:


filter=[x for x in temperature if x<lower_bound or x>upper_bound]


# In[71]:


filter


# In[72]:


orders=pd.DataFrame({"OrderID": [1, 2, 3, 4, 5], "CustomerID": [101, 102, 103, 104, 101], "Product": ['A', 'B', 'A', 'C', 'B'], "Quantity": [2, 1, 4, 2, 3]
})


# In[73]:


customers=pd.DataFrame({"CustomerID": [101, 102, 103, 104], "Name": ['Alice', 'Bob', 'Charlie', 'David'], "Location": ['New York', 'Los Angeles', 'Chicago', 'Houston']
})


# In[74]:


#1.	Merge the orders and customers DataFrames on the 'CustomerID' column.
#2.	Group the merged DataFrame by 'Location' and calculate the total quantity of orders from each location.
#3.	Find the customer who placed the highest number of orders.
#4.	Add a new column 'Total_Quantity' which is the cumulative sum of quantities for each product.
#5.	Filter the merged DataFrame to show only the orders for products 'A' and 'B'.


# In[76]:


merged=pd.merge(orders,customers,on="CustomerID")


# In[77]:


merged


# In[81]:


quantity_per_location=merged.groupby('Location')['Quantity'].sum()


# In[82]:


quantity_per_location


# In[83]:


merged["CustomerID"].mode()


# In[84]:


total_quantity_products=merged.groupby("Product")["Quantity"].sum()


# In[85]:


total_quantity_products


# In[91]:


filter=merged[merged["Product"].isin(['A','B'])]


# In[92]:


filter

