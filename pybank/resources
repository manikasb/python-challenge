# Create file path
impost os
import csv

# Grab data from csv file with open ('budget_data.csv', 'r')
csvpath = os.path.join('Resources', 'budget_data.csv')

open(csvpath, encoding = 'utf') as csvfile:

# Read csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    budget_data = [next(csvreader)]
    net_amount = int(budget_data[0][1])
    changes = []
    previous_profit_loss = net_amount

for line in csvreader:
    budget_data.append(line)
    net_amount = net_amount + int(line[1])
    changes.append(int(line[1])-previous_profit_loss)
    previous_profit_loss = int(line[1])
           
# Calculate changes in "profit/losses" and average change
    average_change = ${round(sum(changes) / len(changes), 2)}

# Find greatest increase and decrease 
greatest_increase = max(changes)
greatest_increase_date = dates [changes.index(greatest_increase)]
greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease)]

# print analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# export results to a text file with open('financial_analysis.txt', 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

print(output)
csvpath = os.path.join('Analysis', 'financial_analysis.txt')
with open(csv.path, 'w') as textfile:
    textfile.write(output)
