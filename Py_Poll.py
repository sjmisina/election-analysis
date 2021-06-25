#   Libraries
import csv
import os

# file path and name to csv data
file_to_load = os.path.join("Resources", "election_results.csv")

# Create/Open a file for analysis and prepare it for 'w'riting
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open results and read the csv file
with open(file_to_load) as election_data:
    # use reader function to read election_data and print each row
    file_reader = csv.reader(election_data)
    
    #read and print header row
    headers = next(file_reader)
    print(headers)

    #for row in file_reader:
    #   print(row)

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.


