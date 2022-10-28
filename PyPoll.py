# The data we need to retrieve.
# 1. The total number of votes cas
# 2. A complete list of candidates who reveived votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#Resources/election_results.csv

# import csv
# dir(csv)

# Assign a variable for the file to load and the path

# file_to_load = 'Resources/election_results.csv'

# opne the election results and read the file.

# election_data = open(file_to_load, 'r')

# to do: perform analysis

# close the file.

# election_data.close()

# Open the election results and read the file

# with open(file_to_load) as election_data:

    # to do: perform analysis

  #  print(election_data)

# import os

# dir(os)

# dir(os.path)

# import csv
# import os

# Assing a variable for the file to load and the path

# file_to_load = os.path.join("Resources", "election_results.csv")

# open the election results and read the file.

# with open(file_to_load) as election_data:

    #print the file object.
    # print(election_data)

# create a filename variable to a direct or indirect path to the file.

# file_to_save = os.path.join("analysis",  "election_analysis.txt")

# using the with statement open the file as a text file.

# with open(file_to_save, "w") as txt_file:
    # Write some data to the file
    # txt_file.write("Hello you stinky World")

    # write three counties to the file.

    # txt_file.write("Arapahoe, ")

    # txt_file.write("Denver, ")

    # txt_file.write("Arapahoe, Denver, Jefferson")

    # txt_file.write("Arapahoe\nDenver\nJefferson")

  #   txt_file.write("Counties in the Election\n---------------------\nArapahoe\nDenver\nJefferson")


#  trimming down to simplify
# ------------------------------------

# add our dependencies
import csv
import os

# Assign a variable to load a file from the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis",  "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # to do: read and analyze the data here.
    # read the file object with the reader function
    file_reader = csv.reader(election_data)
    #print the header row
    headers = next(file_reader)
    print(headers)
    # print each row in the csv file
    #for row in file_reader:
     #   print(row)


# read the file object with the reader function



