# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('menu_data.csv')
sales_filepath = Path('sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list

with open(menu_filepath, 'r') as menu_csv:
    menu_reader = csv.reader(menu_csv, delimiter=',')   
    menu=list(menu_reader)

menu=menu[1:]
#print(menu)


# @TODO: Read in the sales data into the sales list
with open(sales_filepath, 'r') as sales_csv:
    sales_reader = csv.reader(sales_csv, delimiter=',')   
    sales=list(sales_reader)

sales=sales[1:]
#print(f'Sales Data: {sales}')


# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object

for s_item in sales:
    qty=int(s_item[3])
    sales_item=s_item[4]
    #print (s_item[4])



    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables


    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if sales_item not in report.keys():
        report[sales_item]={
            "01-count":0,
            "02-revenue":0,
            "03-cogs":0,
            "04-profit":0,
        }

    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for m_item in menu:

        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables
        menu_item=m_item[0]
        price=float(m_item[3])
        cost=float(m_item[4])
        #print(m_item[0])
       


        # @TODO: Calculate profit of each item in the menu data
        profit = price-cost

        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if menu_item == sales_item:
            
            # @TODO: Print out matching menu data
            #print(f"Menu Item: {menu_item} ")


            # @TODO: Cumulatively add up the metrics for each item key

            report[sales_item]["01-count"] += qty
            report[sales_item]["02-revenue"] += price * qty
            report[sales_item]["03-cogs"] += cost * qty
            report[sales_item]["04-profit"] += profit * cost
            
             # @TODO: Increment the row counter by 1
            row_count +=1

        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match
        else:
            continue


# @TODO: Print total number of records in sales data

print(f"Records in Report{row_count}")

#print(report)


# @TODO: Write out report to a text file (won't appear on the command line output)
with open("report.txt", 'w') as file:
    for record in report.items():
        file.write(f"{record[0]} {record[1]}\n")
    
    file.close()

with open("readme.md", 'w') as file:
    for record in report.items():
        file.write(f"{record[0]} {record[1]}\n")
    
    file.close()
