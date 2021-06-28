# PyPoll with Python

## Project Overview
The Colorado Board of Elections has requested an audit to review election results of a local congressional election.

## Resources
### Data Source:
- election_results.csv - *provided by the Colorado Board of Elections*

### Software Used:
+ Python 3.9.5.  
+ Visual Studio Code, 1.57.1

## Summary
The analysis of the election shows there were a total of ***369,711*** votes cast in this election. 

![Total Votes](Resources/PNG/Total_Votes.png)

This project pulls out the unique names of the candidates, and tabulates their individual votes across the entire district.
#### The candidates were:
1. Charles Casper Stockham
2. Diana DeGette
3. Raymon Anthony Doane

#### The candidate results were:
![Candidate Results](Resources/PNG/Candidate_Results.png)

Candidate Diana DeGette won in a landslide by securing 73.8% of all votes tallied in the district.

## Challenge Overview
As a request from the election commission, county analysis is requested to be provided along with the candidate analysis. This will provide insight into participation by county by considering voter turnout by ballots cast. Futhermore, the county with the largest turnout is to be identified separately.

#### Challenge Summary
County participation was calculated from the election_results.csv data source and provided as
a part of the whole analysis presented here. Each individual county name was pulled and total votes tabulated on the county name.

#### The turnout by county with percentage of total participation in district:
![County Results](Resources/PNG/County_Results.png)

Denver County had the most influence in the election as 82.8% of all ballots cast were from
this one county.


#### Analyst's Note:
- This code can be modified to work with any csv file that is in a column format of "ballot_id,county_name, candidate_name" as the line item results.
- You can also modify the output destination by pointing to another path and filename of your choice.
![Code Snippet](Resources/PNG/target_code.png)


