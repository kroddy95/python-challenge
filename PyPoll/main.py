import os
import csv

# Initialize variables
total_votes = 0
candidate_info = {}
max_votes = 0

# Get the path for the data
cvspath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

# Get the path for the results 
outputpath = os.path.join('..', 'PyPoll', 'analysis', 'results.txt')

# Create/open the new output file
results = open(outputpath, "w")

# Print to the terminal
print("Election Results")
print("-----------------------------------")

# Write to the output file
results.write("Election Results\n")
results.write("-----------------------------------\n")

# Open the data and process each row
with open(cvspath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Store the header
    header = next(csvfile)
    
    # For each of the remaing rows in the csv file
    for row in csvreader:

        # Increase the vote total and get the candicate name
        total_votes +=1
        candidate = row[2]

        # If this is an existing candidate increase their vote by 1, otherwise add to the dictionary
        if candidate in candidate_info:
            candidate_info[candidate] = candidate_info[candidate] + 1
        else:
            candidate_info[candidate] = 1
            
    # Print the total number of votes to the terminal
    print(f"Total Votes: {total_votes}")
    print("-----------------------------------")

    # Write the total number of votes to the output file
    results.write(f"Total Votes: {total_votes}\n")
    results.write("-----------------------------------\n")

    # Figure out winner and candidate number of votes and percentage by going through the dictionary
    for candidate, candidate_votes in candidate_info.items():

        # Determine the percent of votes and format it
        percent_votes = "{:.3%}".format(candidate_votes / total_votes)

        # If the current candidate votes are more than the max, set the new max
        if candidate_votes > max_votes:
            max_votes = candidate_votes
            winner = candidate

        # Print candidate info to the terminal and to output file
        print(f"{candidate}: {percent_votes} ({candidate_votes})")
        results.write(f"{candidate}: {percent_votes} ({candidate_votes})\n")
    
    # Print the winner to terminal
    print("-----------------------------------")
    print(f"Winner: {winner}")
    print("-----------------------------------")

    # Write the winner to output file
    results.write("-----------------------------------\n")
    results.write(f"Winner: {winner}\n")
    results.write("-----------------------------------")    

    # Close the results file
    results.close()