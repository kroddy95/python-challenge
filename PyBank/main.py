import os
import csv

# Initialize the variables
total_months = 0
total_amount = 0
total_change = 0
previous = 0
greatest_increase = 0
greatest_decrease = 0

# Get the path for the data
cvspath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# Get the path for the results 
outputpath = os.path.join('..', 'PyBank', 'analysis', 'results.txt')

# Create/open the new output file
results = open(outputpath, "w")

# Print to the terminal
print("Financial Analysis")
print("-----------------------------------")

# Write to the output file
results.write("Financial Analysis\n")
results.write("-----------------------------------\n")


# Open the data and process each row
with open(cvspath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Store the header
    header = next(csvfile)
    
    # For each of the remaing rows in the csv file
    for row in csvreader:

        # Get the total for the month   
        total = float(row[1])
        
        # Increase the number of months
        total_months += 1

        # Add the total to the running total
        total_amount += total

        # If the previous value is not 0, figure out the change between the last two months
        if previous != 0:
            change = total - previous
            total_change += change

            # Is this change the greatest increase so far, then set the variable and the month
            if change > greatest_increase: 
                greatest_increase = change
                increase_month = row[0]

            # Is this change the greatest decrease so far, then set the variable and the month
            if change < greatest_decrease:
                greatest_decrease = change
                decrease_month = row[0]
            
        # Set the previous total for processing the next row
        previous = total
       
    # Determine the average change, which is 1 month short of total months
    average_change = total_change/(total_months - 1)

    # Format the answers into money
    format_amount = "${:,.2f}".format(total_amount)
    format_change = "${:,.2f}".format(average_change)
    format_increase = "${:,.2f}".format(greatest_increase)
    format_decresase = "${:,.2f}".format(greatest_decrease)

    # Print the totals to the terminal
    print(f"Total Months: {total_months}")
    print(f'Total: {format_amount}')

    # Write the totals to the output file
    results.write(f"Total Months: {total_months} \n")
    results.write(f'Total: {format_amount} \n')

    # Print the rest of the results to the terminal
    print(f'Average Change: {format_change}')
    print(f'Greatest Increase in Profits: {increase_month} ({format_increase})')
    print(f'Greatest Decrease in Profits: {decrease_month} ({format_decresase})')

    # Write the rest of the results to the output file
    results.write(f'Average Change: {format_change} \n')
    results.write(f'Greatest Increase in Profits: {increase_month} ({format_increase}) \n')
    results.write(f'Greatest Decrease in Profits: {decrease_month} ({format_decresase})')

    # Close the results file
    results.close()
    
