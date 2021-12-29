import os
import csv

# Grab CSV file from the Resources folder
pypoll = os.path.join('.', 'Resources', 'election_data.csv')

data = []
# Read the CSV file
with open(pypoll, 'r') as datafile:
    csvreader = csv.reader(datafile, delimiter=',')
    header = next(csvreader)

    # Put data into a list 'data'
    for row in csvreader:
        data.append(row)

    # print(header)

Candidate = [row[2] for row in data]

# Find the total number of votes
totalvotes = len(Candidate)

# Find all Candidates
Candidates = set(Candidate)
print(f"Candidates: {Candidates}")

# Find number of votes each candidate received
Correy = len([elem for elem in Candidate if elem == "Correy"])
OTooley = len([elem for elem in Candidate if elem == "O'Tooley"])
Khan = len([elem for elem in Candidate if elem == "Khan"])
Li = len([elem for elem in Candidate if elem == "Li"])

# Percentage of votes won by each candidate
def percentage(name):
    return "{:.0%}".format((name/totalvotes))

# Winner by popular vote
def winner(CandidateList):
    return max(set(CandidateList), key = CandidateList.count)

print(f"Winner: {winner(Candidate)}")
print(" ")
print("Election Results")
print("---------------------")
print(f"Total Votes: {totalvotes}")
print("---------------------")
print(f"Khan: {percentage(Khan)} ({Khan}) ")
print(f"Correy: {percentage(Correy)} ({Correy})")
print(f"Li: {percentage(Li)} ({Li})")
print(f"O'Tooley: {percentage(OTooley)} ({OTooley})")
print("---------------------")
print(f"Winner: {winner(Candidate)}")
print("---------------------")

# Create output txt file in Analysis folder
output = os.path.join(".", "Analysis", "output.csv")
with open(output, 'w', newline='') as output_file:
    csvwriter = csv.writer(output_file, delimiter=',')
    csvwriter.writerow(['Voter ID', 'County', 'Candidate'])
    csvwriter.writerows(data)