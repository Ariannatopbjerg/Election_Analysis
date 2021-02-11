print("Hello World")
counties = ["Ara","Den","Jeff"]

#How to construct a if statement
if counties[1] == 'Den': ## == Boolean operator which means "equal to"
    print(counties[1])

# How to construct a if-else statement
temperature = int(input("What is the temp outside?")) #int() method will ocnvert the user input data type from a stirng to an integer. The integer is used to assess the if-else statement.
if temperature > 80:
    print("Turn on the AC.")
else:
    print("open the windows.")

#How to construct a nested if-else statement "if-elif-else statements"
#What is the score?
score = int(input("What is your test score?"))

#Dtermine the grade.
if score >= 90:
    print('Your grade is an A')
elif score >= 80:
    print('Your grade is a B')
elif score >= 70:
    print('Your grade is a C')
elif score >= 60:
    print('Your grade is a D')
else:
     print('Your grade is an F')

#Using membership operators
counties = ["Ara","Den","Jeff"]
if "El Paso" in counties:
    print("ElPaso is in the list of counties")
else:
    print("El Paso is not in the list of counties")
counties

#Using compound membership and logical operation; use the "and"/"or" operator
if "Ara" in counties and "El Paso" in counties:
    print("Both are in the list of counties")
else:
    print("wrong")
if "Ara" in counties or "El Paso" in counties:
    print("Both are in the list of counties")
else:
    print("wrong")

#while statement
x = 0 
while x <= 5:
    print(x)
    x = x + 1 
# For loops
counties = ["Ara","Den","Jeff"]
for county in counties:
    print(county)

numbers = [0,1,2,3,4]
for num in numbers:
	print(num)

#Using range function
for number in range(5):
    print(number)


counties = ["Ara","Den","Jeff"]
for i in range(len(counties)):
    print(counties[i])

#Iterate through a dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#Get keys 
for county in counties_dict: #or write -> for county in counties_dict. keys():
                                              #print(county)
    print(county)
#Get values
for voters in counties_dict.values(): #or can write -> dictionary_name[key]
    print(voters)
#For counties list
for county in counties_dict: #or write -> for county in counties_dict: print(counties_dict.get(county))
    print(counties_dict[county])

#for key, value in dictionary_name.items():
    #print(key, value)

for county, voters in counties_dict.items():
    print(county, voters)
#Get seperate dictionary in a list of dicts
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#get values from a list of dicts -> use nested for loop
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
#To get number of registered voters
for county_dict in voting_data:
    print(county_dict['registered_voters'])
#print just county name
for county_dict in voting_data:
    print(county_dict['county'])

#Using f-strings w/ dicts
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

#Format floating-point decimals
##f'{value:{width}.{precision}}'
###width specifies the number of characters used to display the value. However, if a value needs more space than the width specifies, the additional space is used.
###precision indicates the number of decimal places to format the value. to format the interest to two decimal places, we would use .2f, where f means "floating-point decimal format
###When formatting a number, we can also add a thousands separator with a comma, using the following format. The comma is placed after the {width}.
####f'{value:{width},.{precision}}'
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
#For data practice
#Assign a varibale for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

#Using with statement to open file instesd of open()and close() functions -> with open(filename) as file_variable:
## Open the election results and read the file.
with open(file_to_load) as election_data:
    #To do: perform analysis.
    print(election_data)

# Code to open a file to write code in new cleaner code in Py.Polly.py
#Before running the code below, first create new folder called "analysis" within folder election_analysis.
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
outfile = open(file_to_save, "w")
#Write data to the file
outfile.write("What's up peeps")
#Close the file
outfile.close() 