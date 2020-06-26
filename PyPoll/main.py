import os
import csv

# Initialize variables
total_votes = 0
candidate_info = []
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
        total_votes +=1
        candidate = row[2]

        # If this is a new candidate, add to the list.  Otherwise increase vote by 1
        if candidate in candidate_info:
            index = candidate_info.index(candidate)

            # Get the current number of votes and update date it with one more
            current_votes = candidate_info[index + 1]
            candidate_info[index + 1] = current_votes + 1

        else:

            # Add the new candidate to the list
            candidate_info.append(candidate)
            candidate_info.append(1)

    # Print the total number of votes to the terminal
    print(f"Total Votes: {total_votes}")
    print("-----------------------------------")

    # Write the total number of votes to the output file
    results.write(f"Total Votes: {total_votes}\n")
    results.write("-----------------------------------\n")

    # Get the number of candidates in the list to determine the winnder
    nbr_candidates = len(candidate_info)

    # We will go by two, since each candidate has name and votes in the list
    for n in range (0, nbr_candidates, 2):

        # Determine the percent of votes and format it
        percent_votes = "{:.3%}".format(candidate_info[n+1] / total_votes)
        candidate_votes = candidate_info[n+1]

        # If the current votes are more than the max, set the new max
        if candidate_votes > max_votes:
            max_votes = candidate_votes
            winner = candidate_info[n]

        # Print candidate info to the terminal and to output file
        print(f"{candidate_info[n]}: {percent_votes} ({candidate_votes})")
        results.write(f"{candidate_info[n]}: {percent_votes} ({candidate_votes})\n")
    
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
        

