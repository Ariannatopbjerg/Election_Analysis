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
#Open the election results and read the file.
with open(file_to_load) as election_data:
    #To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #Print the header row the CSV file.
    headers = next(file_reader)
    print(headers)



