# Import os and csv file
import os
import csv

# Imported debugger to see if code was working 
#import pdb

# Find relative path
csv_pypoll = ('./Resources/election_data.csv')

# Create lists and dictionaries for variables for data to be stored
ballot_id = []
candidate_options = []
candidate_votes = {}
percent_votes = {}
winning_candidates = {}

# Open and read csv file. Skip header row. 
with open(csv_pypoll) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)


# Read through rows in csvfile
    for row in csvreader:

# Find total votes
        ballot_id.append(row[0])

# Find unique names of candidates and find corresponding number of votes and percent of votes for each candidate   
        candidate_name = row[2]
        unique_votes = []

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

            percent_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name]+1
        percent_votes[candidate_name] = f"{round((candidate_votes[candidate_name]/len(ballot_id) * 100),3)}%"
 
    
# Merge the candidate_votes and percent_votes dictionaries into one
    dict_1 = candidate_votes
    dict_2 = percent_votes

    def mergeDictionary(dict_1,dict_2):
        dict_3 = {**dict_1, **dict_2}
        for key, value in dict_3.items():
            if key in dict_1 and key in dict_2:
                dict_3[key] = [value, dict_1[key]]
        return dict_3
    dict_3 = mergeDictionary(dict_1, dict_2)


# Finding each candidate name in dictionary and the associated values for candidate votes and percent votes in the merged dictionary. Format output.
    for items in dict_3:
        if items == "Charles Casper Stockham":
            candidate_Charles = (f"{items} : {'{0}'.format('%s' %  '('.join(map(str,(dict_3[(items)]))))}) ")
 
        elif items == "Diana DeGette":
            candidate_Diana = (f"{items} : {'{0}'.format('%s' %  '('.join(map(str,(dict_3[(items)]))))}) ")
        
        elif items == "Raymon Anthony Doane":
            candidate_Raymon = (f"{items} : {'{0}'.format('%s' %  '('.join(map(str,(dict_3[(items)]))))}) ")


# Retrieve winning candidate's name        
    max_val = 0
    max_key = None
    for values in percent_votes:
        if percent_votes[values] > percent_votes[candidate_name]:
            max_val = percent_votes[values]
            max_key = values


## CAN SET DEBUGGER - TRIALLED THROUGH TO SEE IF CODE WORKED.
    #pdb.set_trace()


# Print data and re-format output as appropriate
print("Election Results")
print("----------------------------------")
print(f"Total Votes: {len(ballot_id)}")
print("----------------------------------")
print(str('[%s]' % ','.join(map(str, candidate_Charles))).replace(',',""))
print(('[%s]' % ','.join(map(str, candidate_Diana))).replace(',',""))
print(('[%s]' % ','.join(map(str, candidate_Raymon))).replace(',',""))
print("----------------------------------")
print(f"Winner: {max_key}")


# Write and export to txt.file in Analysis Folder
output_path = ('./Analysis/PyPoll_ElectionResults.txt')

with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------------"])
    csvwriter.writerow([f"Total Votes: {len(ballot_id)}"])
    csvwriter.writerow(["----------------------------------"])
    csvwriter.writerow([(('[%s]' % ','.join(map(str, candidate_Charles))).replace(',',""))])
    csvwriter.writerow([('[%s]' % ','.join(map(str, candidate_Diana))).replace(',',"")])
    csvwriter.writerow([('[%s]' % ','.join(map(str, candidate_Raymon))).replace(',',"")])
    csvwriter.writerow(["----------------------------------"])
    csvwriter.writerow([f"Winner: {max_key}"])
