# Import os and csv 
import os 
import csv

# Imported debugger to see if code was working 
#import pdb

# Find relative path
csv_pybank = ('./Resources/budget_data.csv')

# Create lists for Column 0 and Column 1 so data can be stored
date = []
profit_loss = []

# Open and read csv file. Skip header row. 
with open(csv_pybank) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

# Read through rows in csvfile
    for row in csvreader:

# Find total values for months and total profit/loss        
        date.append(row[0])

        profit_loss.append(int(row[1]))


# Create lists to store data in, traverse through columns, find the mean changes, max changes, min changes
    changes = []
    month_max = []
    month_min = []
    changes_monthmax = []
    changes_monthmin = []

    for i in range(1,len(profit_loss)):
        changes.append(profit_loss[i]-profit_loss[i-1])
        changes_monthmax.append(date[i])
        changes_monthmin.append(date[i])

    mean_changes = sum(changes) / len(changes)
    max_changes = max(changes)
    min_changes = min(changes)

# Traverse through the new 'changes' list in order to find the max and min changes. 
    for i in range(1,len(changes)):
        if changes[i] == max_changes:
            month_max = changes_monthmax[i]
        if changes[i] == min_changes:
            month_min = changes_monthmin[i]

## CAN SET DEBUGGER - TRIALLED THROUGH TO SEE IF CODE WORKED.
    #pdb.set_trace()        

# Print data:
    print("Financial Analysis")
    print("-----------------------------------")
        
    print(f"Total Months: {len(date)}")
    print(f"Total: {sum(profit_loss)}")
    print(f"Average Change: {round(mean_changes,2)}")
    print(f"Greatest Increase in Profits: {month_max} (${max_changes})")
    print(f"Greatest Decrease in Profits: {month_min} (${min_changes})")


# Write and export to txt.file in Analysis Folder
output_path = ('./Analysis/PyBank_FinancialAnalysis.txt')

with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------------"])
    csvwriter.writerow([f"Total Months: {len(date)}"])
    csvwriter.writerow([f"Total: {sum(profit_loss)}"])
    csvwriter.writerow([f"Average Change: {round(mean_changes,2)}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {month_max} (${max_changes})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {month_min} (${min_changes})"])