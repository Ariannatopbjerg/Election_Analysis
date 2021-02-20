# Election_Analysis
## Purpose of Analysis
The purpose of this election analysis audit is to be presented to the Colorado Board of Elections. 

Requested data by the election commission:
- *Candidate data*
   - Total number of votes cast 
   - All the candidates who received votes
   - The candidates vote count and percentage of votes 
   - Which candidate won the election based on popular vote
- *County data*
   - The vote turnout for each county 
   - Percentage of votes from each county out of the total count
   - Lastly, the county with the highest turnout. 
   
## Resources
Python 3.9.0 & Visual Studio Code 1.53

## Election-Audit Results
- Total votes cast in the congressional election
``` 
Total Votes: 369,711
```
- Number of votes and percentage of total votes for each county in the precinct
```
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)
```
- County with the largest number of votes
```
County with largest turnout: Denver
```
- Number of votes and precentages of the total votes for each candidate received
```
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
```
- Winner of the election - their vote count and percentage of the total votes
```
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
```
## Election-Audit Summary
This python script not only works efficiently with this election audit in finding candidate and county results but will work with any election. With slight modification to the code, you can change the script to your preference. For example:
- You can remove code to only find specific candidate data, or specific county data. For instance, if you only want to look at information on the candidates, simply take out the `for` loop that is extracting county data. Or if the data has states included, you can add another `for` loop within the script to now look through three different categories. 
- You can alter the way you would like the text file to show the results of any election by using other formating code. 
- You can also switch value names and variable names to best suit the election.

