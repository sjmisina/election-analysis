#   Libraries
import csv
import os

# file path and name to csv data, var assigned: file_to_load
file_to_load = os.path.join("Resources", "election_results.csv")

# Create/Open a file for analysis output and prepare it for 'w'riting, var assigned: file_to_save
file_to_save = os.path.join("analysis", "election_analysis.txt")

# declare variables
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate =""
winning_count = 0

# Open results and read the csv file
with open(file_to_load) as election_data:
    # use reader function to read election_data and print each row
    file_reader = csv.reader(election_data)
    
    # skip over header row
    headers=next(file_reader)
    # calculate vote count
    for row in file_reader:
        total_votes += 1
    # retrieve each candidate name from each row
        candidate_name = row[2]

    #add the candidate name to a candidate_options list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1

# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage: .1f} % of the vote.")
    # winning candidate and winning count tracker

    if (votes>winning_count):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.


