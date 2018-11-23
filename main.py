import csv
import os

PyBank_csv_path = os.path.join("Resources", "budget_data.csv")

with open(PyBank_csv_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)
    print(f"CSV Header: {header}")
    Val= []

    for row in csv_reader:
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