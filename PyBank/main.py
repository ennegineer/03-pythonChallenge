import os
import csv

# Grab CSV file from the Resources folder
pybank = os.path.join('.', 'Resources', 'budget_data.csv')

data = []
# Read the CSV file
with open(pybank, 'r') as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=',')
    header = next(csvreader)

    # Put data into a list 'data'
    for row in csvreader:
        data.append(row)
        
#   The total number of months included in the dataset    
totalMonths = len(data)
    
#  The net total amount of "Profit/Losses" over the entire period   
totalPL = 0
totalChanges = 0
highestRow = [0,0,0]
lowestRow = [0,0,0]
    
for index,row in enumerate(data):
    totalPL = totalPL + int(row[1])
    # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    if index == 0:
        # Create a new column for the change, calculate changes from one month to the next
        row.append(0)
    else:
        # Find the average of the changes (the new column)
        row.append(int(data[index][1]) - int(data[index-1][1]))
        #  The greatest increase in profits (date and amount) over the entire period
        if row[2] > highestRow[2]:
            highestRow = row
        #  The greatest decrease in profits (date and amount) over the entire period
        if row[2] < lowestRow[2]:
            lowestRow = row
    totalChanges = totalChanges + int(row[2])

def currency(var):
    return("${:,.2f}".format(var))      

print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: {currency(totalPL)}")
print(f"Average Change: {currency(totalChanges/totalMonths)}")
print(f"Greatest Increase in Profits: {highestRow[0]} {currency(highestRow[2])}")
print(f"Greatest Decrease in Profits: {lowestRow[0]} {currency(lowestRow[2])}")
        
# Create output txt file in Analysis folder
output = os.path.join(".", "Analysis", "output.csv")
with open(output, 'w', newline='') as output_file:
    csvwriter = csv.writer(output_file, delimiter=' ')
    csvwriter.writerow(['Financial'] + ['Analysis'])
    csvwriter.writerow(["---------------------------------"])
    csvwriter.writerow(['Total'] + ['Months:'] + [totalMonths])
    csvwriter.writerow(['Total:'] + [currency(totalPL)])
    csvwriter.writerow(['Average'] + ['Change:'] + ([currency(totalChanges/totalMonths)]))
    csvwriter.writerow(['Greatest'] + ['Increase'] + ['in'] + ['Profits:']  + [highestRow[0]] + ([currency(highestRow[2])]))
    csvwriter.writerow(['Greatest'] + ['Decrease'] + ['in'] + ['Profits:'] + [lowestRow[0]] + ([currency(lowestRow[2])]))