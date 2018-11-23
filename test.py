import csv
import os

PyBank_csv_path = os.path.join("Resources", "budget_data.csv")
Date = []
P_L = []

with open(PyBank_csv_path, newline='') as csvfile:
    for row in csv_reader:
        Date.append(row[1])
        P_L.append(row[2])
        try:
            Val.append(float(row[1]))
        except ValueError:
            print("error","on line",row)
print("Financial Analysis")
print("-------------------------")
print("Total Months: ",len(Val))
print("Total: ",sum(Val))
print("Average Change: ",(sum(Val)/len(Val)))
print("Greatest Increase in Profits: ", max(Val))
print("Greatest Decrease in Profits: ", min(Val))