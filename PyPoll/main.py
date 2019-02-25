import os
import csv

voterID = []
county = []
candidates = []
#set path for election data csv
electionpath = os.path.join('election_data.csv')
#open election data csv
with open(electionpath, newline='') as electionfile:
    #read election data csv as a csv file
    electionreader = csv.reader(electionfile, delimiter=',')
    #remove header
    csvheader = next(electionreader)

    # for loop to get lists
    for row in electionreader:
        voterID.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
    
    # count total number of votes
    totalvotes = len(voterID)

    # individual candidates
    indcan = list(set(candidates))

    #Dictoinary to create individual candidates with a 0 vote start
    votedic = {}
    for i in range(len(indcan)):
        votedic.update({indcan[i]:0})

    #Dictionary to track votes per individual candidate
    for i in range(len(candidates)):
        votedic[candidates[i]] += 1

    #dicitonary to get vote percentages
    percentdic = {}
    for i in range(len(indcan)):
        percentdic[indcan[i]] =  round(((votedic[indcan[i]] / totalvotes) * 100), 2)
       
    #found function to get max vote key
    winner_name = max(votedic, key=votedic.get)

    #print results
    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {totalvotes}')
    print('-------------------------')
    for i in range(len(indcan)):
        print(f'{indcan[i]}: {percentdic[indcan[i]]}% ({votedic[indcan[i]]})')
    print('-------------------------')
    print(f'winner: {winner_name}')
    print('-------------------------')

    #print to text.
    output_path = os.path.join('pypolloutput.txt')
    with open(output_path, 'w', newline='') as outputfile:
        
        outputfile.writelines('Election Results\n')
        outputfile.writelines('-------------------------\n')
        outputfile.writelines(f'Total Votes: {totalvotes}\n')
        outputfile.writelines('-------------------------\n')
        for i in range(len(indcan)):
            outputfile.writelines(f'{indcan[i]}: {percentdic[indcan[i]]}% ({votedic[indcan[i]]})\n')
        outputfile.writelines('-------------------------\n')
        outputfile.writelines(f'winner: {winner_name}\n')
        outputfile.writelines('-------------------------\n')