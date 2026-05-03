#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
df= pd.read_csv(r"C:\Users\ashik\Downloads\Superstore_Management_System.csv")


# In[2]:


df.head()


# In[3]:


# Checking if missing data or null values are present in the dataset

df.isnull().sum()


# In[4]:


# Summary statistics using .describe()

df.describe(include='all')


# In[5]:


df.dtypes


# In[6]:


df.sample()


# In[7]:


f'Data Type is :{type(df)}'


# In[8]:


df.describe(include = 'object')


# # Data Analysis
Data Quality Check
# In[9]:


print("\n=== Data Quality Assessment ===")

#check for missing values
print("\nMissing Values:")
missing_data = df.isnull().sum()
print(missing_data[missing_data > 0])

#check for duplicates
print(f"\nDuplicate Rows: {df.duplicated().sum()}")


# Data Type Conversion

# In[10]:


df['Order Date'] = pd.to_datetime(df['Order Date'], format = '%d-%m-%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format = '%d-%m-%Y')


# Univariate Analysis

# In[11]:


print("\n=== Categorical Variables ===")

categorical_cols = ['Customer Segment', 'Category','Region', 'Payment Mode', 'Delivery Status','Auto Reorder']
for col in categorical_cols:
    print(f"\n---{col}---")
    print(df[col].value_counts())

#Visuliazation
    plt.figure(figsize=(6,6))
    df[col].value_counts().plot(kind='bar', color='skyblue')
    plt.title(f'Distribution of {col}')
    plt.xticks(rotation = 30)
    plt.tight_layout()
    plt.show()


# Numerical Variable Analysis

# In[12]:


print("\n=== Numerical Variables ===")

numerical_cols = ['Quantity','Unit Price', 'Discount (%)','Sales Amount', 'Cost Price', 'Profit','Stock Left','Reorder Quantity']
for col in numerical_cols:
    print(f"\n---{col}---\n")
    print(f"Mean: {df[col].mean():.2f}")
    print(f"Median: {df[col].median():.2f}")
    print(f"Std Dev: {df[col].std():.2f}")
    print(f"Min: {df[col].min():.2f}")
    print(f"Max: {df[col].max():.2f}")
    
    #Visuliazation
    plt.figure(figsize=(8,4))
    
    plt.subplot(1,2,1)
    df[col].hist(bins=30,  color = 'lightgreen',alpha=0.7)
    plt.title(f'Distribution of {col}')
    
    plt.subplot(1,2,2)
    df.boxplot(column = col)
    plt.title(f' boxplot of {col}')
    
    plt.tight_layout()
    plt.show()


# Bivariate Analysis

# In[13]:


print("\n=== Sales & Profit by Category ===\n")

category_performance = df.groupby('Category').agg({
    'Sales Amount': 'sum',
    'Profit': 'sum',
    'Order ID': 'count'    
}).rename(columns = {'Order ID': 'Order Count'})

category_performance['Profit Margin'] = (category_performance['Profit']/category_performance['Sales Amount']) * 100
print(category_performance,"\n\n")

#visuliazation
fig,axes = plt.subplots(2,2, figsize=(15,12))

#Sales by Category
category_performance['Sales Amount'].plot(kind ='bar', ax=axes[0,0], color = 'blue', alpha = 0.7)
axes[0,0].set_title('Total Sales By Category')
axes[0,0].tick_params(axis='x', rotation = 45)

#Profit by Category
category_performance['Profit'].plot(kind ='bar', ax=axes[0,1], color = 'green', alpha = 0.7)
axes[0,1].set_title('Total Profit By Category')
axes[0,1].tick_params(axis='x', rotation = 45)

#Profit Margins by Category
category_performance['Profit Margin'].plot(kind ='bar', ax=axes[1,0], color = 'orange', alpha = 0.7)
axes[1,0].set_title('Profit Margin By Category (%)')
axes[1,0].tick_params(axis='x', rotation = 45)

#Order Count by Category
category_performance['Order Count'].plot(kind ='bar', ax=axes[1,1], color = 'red', alpha = 0.7)
axes[1,1].set_title('Order Count By Category')
axes[1,1].tick_params(axis='x', rotation = 45)


plt.tight_layout()
plt.show()


# Regional Performance

# In[14]:


print("\n=== Sales & Profit by Region ===\n")

Regional_performance = df.groupby('Region').agg({
    'Sales Amount': 'sum',
    'Profit': 'sum',
    'Order ID': 'count'    
}).rename(columns = {'Order ID': 'Order Count'})

Regional_performance['Profit Margin'] = (Regional_performance['Profit']/Regional_performance['Sales Amount']) * 100
print(Regional_performance,"\n\n")

# Reset index for seaborn
Regional_performance = Regional_performance.reset_index()

#visuliazation
plt.figure(figsize=(12,8))

#Sales by Region
plt.subplot(2,2,1)
Regional_performance['Sales Amount'].plot(kind ='pie', autopct = '%1.1f%%')
plt.title('Sale Distribution By Region')

#Profit by Region
plt.subplot(2,2,2)
Regional_performance['Profit'].plot(kind ='pie', autopct = '%1.1f%%')
plt.title('Profit Distribution By Region')


#Order Count by Region
plt.subplot(2,2,3)
sns.barplot(x = Regional_performance.index, y='Order Count', data=Regional_performance)
plt.title('Order Count by Region')
plt.xticks(rotation = 30)

#Profit Margins by Region
plt.subplot(2,2,4)
sns.barplot(x = Regional_performance.index, y='Profit Margin', data=Regional_performance)
plt.title('Profit Margin by Region (%)')
plt.xticks(rotation = 30)


plt.tight_layout()
plt.show()


# Time Series Analysis

# In[21]:


print("\n=== Time Series Analysis ===\n")
#Extract time components
df['Order Month'] = df['Order Date'].dt.to_period('M')
df['Order Year'] = df['Order Date'].dt.year

#Monthly Trends
monthly_trends= df.groupby('Order Month').agg({
    'Sales Amount': 'sum',
    'Profit': 'sum',
    'Order ID': 'count'
}).rename(columns={'Order ID': 'Order Count'})

print('Monthly Trends:')
print(monthly_trends.tail(10),'\n\n')

#visualization
plt.figure(figsize=(15,10))

plt.subplot(3,1,1)
monthly_trends['Sales Amount'].plot(kind='line', color ='blue', marker ='o')
plt.title('Monthly Sales Trends')
plt.ylabel('Sales Amount')
plt.grid(True)

plt.subplot(3,1,2)
monthly_trends['Profit'].plot(kind='line', color ='Green', marker ='o')
plt.title('Monthly Profit Trends')
plt.ylabel('Profit')
plt.grid(True)

plt.subplot(3,1,3)
monthly_trends['Order Count'].plot(kind='line', color ='red', marker ='o')
plt.title('Monthly Order Count Trends')
plt.ylabel('Order Count')
plt.grid(True)

plt.tight_layout()
plt.show()


# # Advanced Analysis

# In[23]:


print("\n=== Correlations Analysis ===\n")

numerical_df = df[['Quantity', 'Unit Price', 'Discount (%)', 'Sales Amount', 'Cost Price', 'Profit']]

#correlation matrix
correlation_matrix = numerical_df.corr()
print("Correlation Matrix:")
print(correlation_matrix,'\n\n')

plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot = True, cmap = 'coolwarm', center =0, square =True, linewidths=0.5)
plt.title('Correlations Heatmap')
plt.tight_layout()
plt.show()


# # Customer Segment Analysis

# In[24]:


print("\n=== CUSTOMER SEGMENT ANALYSIS ===\n")

segment_analysis = df.groupby('Customer Segment').agg({
    'Sales Amount': ['sum', 'mean'],
    'Profit': ['sum', 'mean'],
    'Order ID': 'count',
    'Discount (%)': 'mean'
}).round(2)

segment_analysis.columns = [
    'Total Sales', 'Avg Sales',
    'Total Profit', 'Avg Profit',
    'Order Count', 'Avg Discount'
]

print(segment_analysis, '\n\n')

# Visualization
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

segment_analysis['Total Sales'].plot(kind='bar', ax=axes[0, 0], color='lightblue')
axes[0, 0].set_title('Total Sales by Customer Segment')
axes[0, 0].tick_params(axis='x', rotation=30)

segment_analysis['Total Profit'].plot(kind='bar', ax=axes[0, 1], color='lightgreen')
axes[0, 1].set_title('Total Profit by Customer Segment')
axes[0, 1].tick_params(axis='x', rotation=30)

segment_analysis['Avg Profit'].plot(kind='bar', ax=axes[1, 0], color='orange')
axes[1, 0].set_title('Average Profit by Customer Segment')
axes[1, 0].tick_params(axis='x', rotation=30)

segment_analysis['Avg Discount'].plot(kind='bar', ax=axes[1, 1], color='red')
axes[1, 1].set_title('Average Discount by Customer Segment')
axes[1, 1].tick_params(axis='x', rotation=30)

plt.tight_layout()
plt.show()


# # Key Insights And Summary

# In[25]:


print("\n=== KEY INSIGHTS SUMMARY ===")

# Overall Metrics
total_sales = df['Sales Amount'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique()
avg_profit_margin = (total_profit / total_sales) * 100

print(f"\nOVERALL PERFORMANCE:\n")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Average Profit Margin: {avg_profit_margin:.2f}%")

# Top Performing Categories
top_categories = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)

print(f"\nTOP PERFORMING CATEGORIES:\n")
for i, (category, profit) in enumerate(top_categories.items(), 1):
    print(f"{i}. {category}: ${profit:,.2f}")

# Regional Performance
best_region = df.groupby('Region')['Profit'].sum().idxmax()
print(f"\nBEST PERFORMING REGION: {best_region}")

# Delivery Performance
delivery_stats = df['Delivery Status'].value_counts(normalize=True) * 100

print(f"\nDELIVERY STATUS:")
for status, percentage in delivery_stats.items():
    print(f"{status}: {percentage:.1f}%")

# Customer Segments
best_segment = df.groupby('Customer Segment')['Profit'].sum().idxmax()
print(f"\nMOST PROFITABLE CUSTOMER SEGMENT: {best_segment}")


# # Export Results

# In[26]:


print("\n=== EXPORT RESULTS ===")

analysis_results = {
    'total_sales': total_sales,
    'total_profit': total_profit,
    'total_orders': total_orders,
    'avg_profit_margin': avg_profit_margin,
    'top_category': top_categories.index[0],
    'best_region': best_region,
    'best_customer_segment': best_segment
}

# Convert to DataFrame and save
results_df = pd.DataFrame([analysis_results])
results_df.to_csv('eda_analysis_summary.csv', index=False)

print("\n✅ Analysis summary saved to 'eda_analysis_summary.csv'")


# In[27]:


import os
print(os.getcwd())


# In[ ]:




