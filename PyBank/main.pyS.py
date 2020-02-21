import os
import csv

csvpath = os.path.join("C:/PREWORK_AS/Module-3/Python_challenge-master/Python_challenge-master/PyBank/main.py/03-Python_Instructions_PyBank_Resources_budget_data.csv")

total_months = []
total_profit = []
monthly_profit_change = []

with open(csvpath, newline='') as csvfile:

   
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    
    for i in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")


output_file = os.path.join('PyBank_output.txt')
with open(output_file,"w")as output:

    output.write(f"Total Months: {len(total_months)}")
    output.write(f"Total: ${sum(total_profit)}")
    output.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    output.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    output.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")



