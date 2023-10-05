# imports
import os
import csv

# join the csv file
budgetCSV = os.path.join("Resources", "budget_data.csv")

# variables
totalMonths = 0
difference = 0

# lists
incDecValues = [0]
differences = [0]
months = []
greatestInc = ["", 0]
greatestDec = ["", 0]

# read csv
with open(budgetCSV, "r") as budgetFile:

    # create reader
    csvreader = csv.reader(budgetFile, delimiter=",")

    # skip header
    header = next(budgetFile)

    # loop data reading
    for row in csvreader:

        # add to total months and list of values
        totalMonths += 1
        incDecValues.append(int(row[1]))

        # add current month to list
        months.append(row[0])

        # find difference between current +/- and previous and add to list
        incOrDec = incDecValues[-1] - incDecValues[-2]
        differences.append(int(incOrDec))

        # if statement to find greatest increase/decrease
        if differences[-1] > greatestInc[-1]:
            greatestInc = [months[-1], differences[-1]]

        if differences[-1] < greatestDec[-1]:
            greatestDec = [months[-1], differences[-1]]

# clear initial '0' in differences that made if statement work
# and the result of the first loop based on that '0'
differences.pop(1)
differences.pop(0)

# round avg change to 2 decimals
avgChange = round(sum(differences)/len(differences), 2)

# create file for output
outputFile = os.path.join("Analysis", "analysis.txt")

# write to text file
with open(outputFile, "w") as analysisFile:
    analysisFile.write("Financial Analysis")
    analysisFile.write("\n--------------------")
    analysisFile.write(f"\nTotal Months: {totalMonths}")
    analysisFile.write(f"\nTotal: ${sum(incDecValues)}")
    analysisFile.write(f"\nAverage Change: ${avgChange}")
    analysisFile.write(f"\nGreatest Increase in Profits: {greatestInc[0]} (${greatestInc[1]})")
    analysisFile.write(f"\nGreatest Decrease in Profits: {greatestDec[0]} (${greatestDec[1]})")

# print results in terminal
print("Financial Analysis")
print("\n--------------------")
print(f"\nTotal Months: {totalMonths}")
print(f"\nTotal: ${sum(incDecValues)}")
print(f"\nAverage Change: ${avgChange}")
print(f"\nGreatest Increase in Profits: {greatestInc[0]} (${greatestInc[1]})")
print(f"\nGreatest Decrease in Profits: {greatestDec[0]} (${greatestDec[1]})")