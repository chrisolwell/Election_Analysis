#We need to find out each candidate in the election
#determine how many total votes were cast
#determine how many votes were cast for each candidate
#determine the percentage of the total votes cast each candidate recieved
#determine which candidate won the election
import csv
import os
#assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources/election_results.csv')
#Open the elections results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze the data here.
   file_reader = csv.reader(election_data)
   #print the header row
   headers =next(file_reader)
   print(headers)

#     #To do: perform analysis.
#     print(election_data)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# #Use the open statemment to open the file as a text file.
# outfile = open(file_to_save, "w")
# #write some data to the file.
# outfile.write("Counties in the Election\n------------------------------\nAraphaoe\nDenver\nJefferson")

# #Close the file.
# outfile.close()


