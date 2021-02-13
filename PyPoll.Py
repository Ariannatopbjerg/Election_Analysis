#Data that needs to be retrieved 
#1. Total number of votes cast
#2. A complete list of canidadates who recieved votes
#3. The percentage of votes each canidate won
#4. The total number of votes each canidate won
#5. The winner of the election based on popular vote.

import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter for counting votes; this variable is called an accumulator
total_votes = 0

#Candidate Options (list) -> []
candidate_options = []

#Empty dictionary for candidates(key) and their vote count(value). (dictionary) -> {}
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
   
    #To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    #Print the header row the CSV file.
    headers = next(file_reader)
    #print(f"Election Results Headers : {headers}")
    
    for row in file_reader:
        #print(row)
       
        #Add to the total vote count -> counting votes
        total_votes = total_votes + 1        #or can write as -> total_votes += 1
        #Print total votes
        #print(total_votes)
    #print each rows ballot ID 
    
        #print("Ballot ID is: {0}".format(row[0]))
        
        #Print the candidate name from each row
        candidate_name = row[2]

        #Add the candidate name to the candidate list: candidate_options
        #candidate_options.append(candidate_name)

#Print the candidate list -> show every candidate from each row... don't want. Soultions -> make if statement
#print(candidate_options)
        
       
        #If candidate does not match any existing candidates...    #the 'not in' membership operator will check if the candidate has been added to the list, if they have, it will not be added.
        if candidate_name not in candidate_options:
            
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        
            #Add a vote to that candidate's count.            #Make sure not in if statement but in the for loop when the loop is counting through the rows.
        candidate_votes[candidate_name] += 1                   #Needs to be flush with the if statement; not within if statement for this line to work.
#Print the candidate list.
#print(candidate_votes)

#Save results to text file
with open(file_to_save, "w") as txt_file:

    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"  #the ',' is a thousands seperator
        f"--------------------------\n")
    print(election_results, end="")        # 'end=""' is a parameter indicating is equal to an empty string -> Anything printed after will be printed on a newline

    #Save the final vote count to the text file.
    txt_file.write(election_results)
    
    #Determine the percentage of votes for each candidate by looping through the counts.
    #Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes    #Converting 'votes' and 'total_votes' from integers to floating-point decimal numbers for calculation
        vote_percentage = float(votes)/float(total_votes)*100
        
        #To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        #Save candidate results to text file.
        txt_file.write(candidate_results)

        #Determine winning vote count and candidate
        #Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage 
            #Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    
    #Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    #Save the winning candidate's results to text file.
    txt_file.write(winning_candidate_summary)

   
   
   
    #Print the candidate name and percentage of votes
    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote")       #':.1f' indicates rounding to 1 decimal place (can change number for how many decimal places you like.)

