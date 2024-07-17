import os
import csv

# Create file path
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header
    next(csvreader)
    
    # Initialize variables
    total_months = 0
    net_total = 0
    changes = []
    dates = []
    
    # Read data from csv
    for line in csvreader:
        total_months += 1
        net_total += int(line[1])
        dates.append(line[0])
        
        if total_months > 1:
            changes.append(int(line[1]) - previous_profit_loss)
        previous_profit_loss = int(line[1])
    
    # Calculate average change
    average_change = round(sum(changes) / len(changes), 2)
    
    # Find greatest increase and decrease
    greatest_increase = max(changes)
    greatest_increase_date = dates[changes.index(greatest_increase)]
    greatest_decrease = min(changes)
    greatest_decrease_date = dates[changes.index(greatest_decrease)]
    
    # Print analysis results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
    
    # Export results to text file
    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${net_total}\n"
        f"Average Change: ${average_change}\n"
        f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"
    )
    
    # Create the 'Analysis' directory if it does not exist
    output_dir = 'Analysis'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_path = os.path.join(output_dir, 'financial_analysis.txt')
    with open(output_path, 'w') as textfile:
        textfile.write(output)
