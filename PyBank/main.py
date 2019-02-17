import os
import csv



#set path for budget data csv
budgetpath = os.path.join('budget_data.csv')
#open budget data csv
with open(budgetpath, newline='') as budgetfile:
    #read budget data csv as a csv file
    budgetreader = csv.reader(budgetfile, delimiter=',')
    #remove header
    csvheader = next(budgetreader)
    
    months =[]
    money = []
    totalmoney = 0
    #for loop to get initial lists
    for row in budgetreader:
        # list for months
        months.append(row[0])
        #list for money
        money.append(row[1])

        #experiment, total money?
        totalmoney += int(row[1])

    #total months
    totalmonths = len(months)
    #convert money to integers
    for i in range(len(money)):
        money[i] = int(money[i])
    
    #change per month
    changes = [money[i] - money[i - 1] for i in range(1, len(money))]
    #average change per month
    totalchange = 0
    for i in changes:
        totalchange += i
    averagechange = round((totalchange / len(changes)), 2)
    
    #max increase
    maxchange = max(changes)

    #maxdecrease
    maxdecrease = min(changes)    
    # change list
    changemonths = months
    changemonths.pop(0)
    changelist = zip(months, changes)
    
    #max increase month
    for row in changelist:
        if row[1] == maxchange:
            maxmonth = row[0]
        elif row[1] == maxdecrease:
            minmonth = row[0]

    print("Financial Analysis")
    print('----------------------------')
    print(f'Total Months: {totalmonths}')
    print(f'Total: ${totalmoney}')
    print(f'Average  Change: ${averagechange}')
    print(f'Greatest Increase in Profits: {maxmonth} (${maxchange})')
    print(f'Greatest Decrease in Profits: {minmonth} (${maxdecrease})')

    output_path = os.path.join('pybankoutput.txt')
    with open(output_path, 'w', newline='') as outputfile:
        
        outputfile.writelines(f"Financial Analysis")
        outputfile.writelines(f'----------------------------')
        outputfile.writelines(f'Total Months: {totalmonths}')
        outputfile.writelines(f'Total: ${totalmoney}')
        outputfile.writelines(f'Average  Change: ${averagechange}')
        outputfile.writelines(f'Greatest Increase in Profits: {maxmonth} (${maxchange})')
        outputfile.writelines(f'Greatest Decrease in Profits: {minmonth} (${maxdecrease})')



