# Election_Analysis
 
## Project Overview
The Colorado Board of Elections has requested an audit to review election results of a local congressional election.

## Resources
### Data Source:
- election_results.csv - *provided by the Colorado Board of Elections*

### Software Used:
+ Python 3.9.5.  
+ Visual Studio Code, 1.57.1

## Summary
The analysis of the election shows there were a total of ***369,711*** votes cast in this election. This project pulls out the unique names of the candidates, and tabulates their individual votes across all counties.
![/Resources/PNG/Total_Votes.png]

#### The candidates were:
1. Charles Casper Stockham    
2. Diana DeGette    
3. Raymon Anthony Doane

#### The candidate results were:
![Resources/PNG/Candidate_Results.png]  

### Challenge Overview
As a request from the election commission, county analysis is requested to be provided along with the candidate analysis. This will provide insight into participation by county by considering voter turnout by ballots cast. Futhermore, the county with the largest turnout is to be identified separately.

#### Challenge Summary
County participation was calculated from the election_results.csv data source and provided as
a part of the whole analysiss presented herein. Each individual county name was pulled and total votes tabulated on the county name.

#### The turnout by county with percentage of total participation in district:
![Resources/PNG/County_Results.png]

### Overall Summary
Denver County had the most influence in the election as 82.8% of all ballots cast were from
this one county.

Candidate Diana DeGette won in a landslide by securing 73.8% of all votes tallied in the district.

#### Analyst's Note:
This code can be modified to work with any csv file that is in a column format of "ballot_id,county_name, candidate_name" as the line item results. You can also modify the output destination by pointing to anotther path and filename if you choose.
![Resources/PNG/target_code.png]
