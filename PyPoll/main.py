# imports
import os
import csv

# join the cvs
electionCSV = os.path.join("Resources", "election_data.csv")

# variables
voteCount = 0
name = ""   # temporary holder for candidate name

# lists
candidateNames = []

# dictionary for candidate votes
candidateVotes = {
    
}

# read csv
with open(electionCSV, "r") as electionData:
    csvreader = csv.reader(electionData, delimiter=",")

    # skip header
    header = next(electionData)

    for row in csvreader:
        
        # +1 to total votes
        voteCount += 1
        # get candidate name
        name = row[2]

        # boolean for 'is in list'
        inNameList = False

        # check if candidate name is in the list
        if name in candidateNames:
            inNameList = True
        # if not, add to the list
        if inNameList == False:
            candidateNames.append(name)
            
        # add vote to dictionary for candidate total
        if name not in candidateVotes:
            candidateVotes[name] = 0
        if name in candidateVotes:
            candidateVotes[name] += 1
            

# find candidate with top votes using a zip function
topVotes = max(zip(candidateVotes.values(), candidateVotes.keys()))[1]


# print results
print(f"\nElection Results")
print(f"\n--------------------")
print(f"\nTotal Votes: {voteCount}")
print(f"\n--------------------")
print(f"\n{candidateNames[0]}: {round(candidateVotes[candidateNames[0]] / voteCount * 100, 3)}% ({candidateVotes[candidateNames[0]]})")
print(f"\n{candidateNames[1]}: {round(candidateVotes[candidateNames[1]] / voteCount * 100, 3)}% ({candidateVotes[candidateNames[1]]})")
print(f"\n{candidateNames[2]}: {round(candidateVotes[candidateNames[2]] / voteCount * 100, 3)}% ({candidateVotes[candidateNames[2]]})")
print(f"\n--------------------")
print(f"\nWinner: {topVotes}")
print(f"\n--------------------")

# write results to text file
outputFile = os.path.join("Analysis", "electionResults.txt")
with open(outputFile, "w") as electionResults:
    electionResults.write(f"Election Results")
    electionResults.write(f"\n--------------------")
    electionResults.write(f"\nTotal Votes: {voteCount}")
    electionResults.write(f"\n--------------------")
    electionResults.write(f"\n{candidateNames[0]}: {round(candidateVotes[candidateNames[0]] / voteCount * 100, 3)}% ({candidateVotes[candidateNames[0]]})")
    electionResults.write(f"\n{candidateNames[1]}: {round(candidateVotes[candidateNames[1]] / voteCount * 100, 3)}% ({candidateVotes[candidateNames[1]]})")
    electionResults.write(f"\n{candidateNames[2]}: {round(candidateVotes[candidateNames[2]] / voteCount * 100, 3)}% ({candidateVotes[candidateNames[2]]})")
    electionResults.write(f"\n--------------------")
    electionResults.write(f"\nWinner: {topVotes}")
    electionResults.write(f"\n--------------------")