# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 11:31:03 2025

@author: 28pgd
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
# Replace with the actual path to your file
file_path = r'D:\SAP\employee_attrition_data.csv'
data = pd.read_csv(file_path)




# Set up visualization style
sns.set(style='whitegrid')

# 1. Attrition Rate Analysis
attrition_rate = data['Attrition'].mean() * 100
print(f'Attrition Rate: {attrition_rate:.2f}%')

# Plotting Attrition Count
plt.figure(figsize=(6,4))
sns.countplot(x='Attrition', data=data, palette='viridis')
plt.title('Attrition Count')
plt.show()

# 2. Satisfaction vs. Attrition
plt.figure(figsize=(8,5))
sns.boxplot(x='Attrition', y='Satisfaction_Level', data=data, palette='Set2')
plt.title('Satisfaction Level vs. Attrition')
plt.show()

# 3. Departmental Attrition
plt.figure(figsize=(10,6))
sns.countplot(x='Department', hue='Attrition', data=data, palette='cool')
plt.title('Attrition by Department')
plt.xticks(rotation=45)
plt.show()

# 4. Impact of Promotions
plt.figure(figsize=(6,4))
sns.countplot(x='Promotion_Last_5Years', hue='Attrition', data=data, palette='muted')
plt.title('Attrition by Promotion Status')
plt.show()

# 5. Work Hours and Attrition
plt.figure(figsize=(8,5))
sns.boxplot(x='Attrition', y='Average_Monthly_Hours', data=data, palette='Blues')
plt.title('Monthly Hours vs. Attrition')
plt.show()

# 6. Salary Distribution and Attrition
plt.figure(figsize=(8,5))
sns.boxplot(x='Attrition', y='Salary', data=data, palette='Reds')
plt.title('Salary vs. Attrition')
plt.show()

# 7. Gender and Attrition
plt.figure(figsize=(6,4))
sns.countplot(x='Gender', hue='Attrition', data=data, palette='pastel')
plt.title('Gender vs. Attrition')
plt.show()

# 8. Years at Company vs. Attrition
plt.figure(figsize=(8,5))
sns.boxplot(x='Attrition', y='Years_at_Company', data=data, palette='Oranges')
plt.title('Years at Company vs. Attrition')
plt.show()