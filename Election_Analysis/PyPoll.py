# #We need to find out each candidate in the election
# #determine how many total votes were cast
# #determine how many votes were cast for each candidate
# #determine the percentage of the total votes cast each candidate recieved
# #determine which candidate won the election

# Add our dependencies.
import csv
import os
from types import ClassMethodDescriptorType
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
total_votes = 0
#extract a list of candidates.
candidate_options = []
#declare an empty dictionary to count votes for each candidate.
candidate_votes = {}
#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
        #print the candidate name from each row.
        candidate_name = row[2]
        #candidate_options.append(candidate_name)
        #disregard duplicate candidate names.
        if candidate_name not in candidate_options:
            #add candidate name to candidate list.
            candidate_options.append(candidate_name)
            #track each candidate's votes
            candidate_votes[candidate_name] = 0
        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #print each candidate's voter count and percentage to the text file.
        print(candidate_results)
        # Save the candidate results to a text file.
        txt_file.write(candidate_results)
        #Determine winning vote count and candidate
        #1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #2. If true, set winning_count to = votes and winning_percent = 
            #vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #3. set the winnning_candidate equal to the candidate's name
            winning_candidate = candidate_name
    #to do: print out the winning candidate, vote count and percentage to terminal
    winning_candidate_summary = (
        f"_------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------\n")
    print(winning_candidate_summary)
    #Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
