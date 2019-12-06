#!/usr/bin/env python
# coding: utf-8

# In[6]:


# PyBank

# Dependencies
import csv
import os


# In[8]:


# Files to load and output
file_to_load = os.path.join("budget_data.csv")
#file_to_output = os.path.join ("budget_analysis.txt")


# In[30]:




# Declare the different financial parameters
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999999]
total_net = 0

# Read the csv and convert into list of dictionaries
with open (file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    
    # Read the header row
    header = next(reader)
    #print(header)
    
    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    #print(first_row)
    total_months = total_months + 1
    
    # print(total_net)
    # print(prev_net)
    total_net = total_net = int(first_row[1])
    prev_net = int(first_row[1])
    
    
    
    # Loop through data
    for row in reader:
        
        # Track the total
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        #print(total_net)
        
        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]
        #print(net_change_list)
        #print(month_of_change)
        
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        #print("Greatest Increase")
        #print(greatest_increase)
        
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
            
# Calculate the average net change
net_monthly_avg =sum(net_change_list) / len(net_change_list)
#print(net_monthly_avg)
        
       
#print("Total Month" + str(total_months))

print("Financial")
print("-"*15)
print(f"Total Months: {total_months}")
print(f"Total: {total_net}")
print(f"Average Change: {net_monthly_avg}")
print(f"Greatest Increase In Profits: {greatest_increase}")
print(f"Greatest Decrease In Profits: {greatest_decrease}")



        
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




