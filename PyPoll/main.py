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
    #had to print to find the number of candidates.  Is there a way to create dictionaries with length of lists?

    

    # votes per candidate
    indcanvotedic = {indcan[0]:0, indcan[1]:0, indcan[2]:0, indcan[3]:0}

    for can in candidates:
        if can == indcan[0]:
            indcanvotedic[indcan[0]] +=1
        elif can == indcan[1]:
            indcanvotedic[indcan[1]] +=1
        elif can == indcan[2]:
            indcanvotedic[indcan[2]] +=1
        elif can == indcan[3]:
            indcanvotedic[indcan[3]] +=1
    
  

    #can I add this to the dictionary above?  number key for percentage?
    #can I make a for loop that creates new variables each loop?
    percent0 = round((indcanvotedic[indcan[0]] * 100 / totalvotes), 2)
    percent1 = round((indcanvotedic[indcan[1]] * 100 / totalvotes), 2)
    percent2 = round((indcanvotedic[indcan[2]] * 100 / totalvotes), 2)
    percent3 = round((indcanvotedic[indcan[3]] * 100 / totalvotes), 2)


    #this is tough to read.  I could put the dictionary values to individual variables after calculations in the foor loop.
    #if I made new variables I'd have to add them if the candidate number changed.  Ask TAs.
    winner = ''
    if indcanvotedic[indcan[0]] > indcanvotedic[indcan[1]] and \
    indcanvotedic[indcan[0]] > indcanvotedic[indcan[2]] and \
    indcanvotedic[indcan[0]] > indcanvotedic[indcan[3]]:
        winner = indcan[0] 
    if indcanvotedic[indcan[1]] > indcanvotedic[indcan[0]] and \
    indcanvotedic[indcan[1]] > indcanvotedic[indcan[2]] and \
    indcanvotedic[indcan[1]] > indcanvotedic[indcan[3]]:
        winner = indcan[1] 
    if indcanvotedic[indcan[2]] > indcanvotedic[indcan[1]] and \
    indcanvotedic[indcan[2]] > indcanvotedic[indcan[2]] and \
    indcanvotedic[indcan[2]] > indcanvotedic[indcan[3]]:
        winner = indcan[2]
    if indcanvotedic[indcan[3]] > indcanvotedic[indcan[1]] and \
    indcanvotedic[indcan[3]] > indcanvotedic[indcan[2]] and \
    indcanvotedic[indcan[3]] > indcanvotedic[indcan[3]]:
        winner = indcan[3]


    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {totalvotes}')
    print('-------------------------')
    print(f'{indcan[0]}: {percent0}% ({indcanvotedic[indcan[0]]})')
    print(f'{indcan[1]}: {percent1}% ({indcanvotedic[indcan[1]]})')
    print(f'{indcan[2]}: {percent2}% ({indcanvotedic[indcan[2]]})')
    print(f'{indcan[3]}: {percent3}% ({indcanvotedic[indcan[3]]})')
    print('-------------------------')
    print(f'winner: {winner}')
    print('-------------------------')

    output_path = os.path.join('pypolloutput.txt')
    with open(output_path, 'w', newline='') as outputfile:
        
        outputfile.writelines('Election Results')
        outputfile.writelines('-------------------------')
        outputfile.writelines(f'Total Votes: {totalvotes}')
        outputfile.writelines('-------------------------')
        outputfile.writelines(f'{indcan[0]}: {percent0}% ({indcanvotedic[indcan[0]]})')
        outputfile.writelines(f'{indcan[1]}: {percent1}% ({indcanvotedic[indcan[1]]})')
        outputfile.writelines(f'{indcan[2]}: {percent2}% ({indcanvotedic[indcan[2]]})')
        outputfile.writelines(f'{indcan[3]}: {percent3}% ({indcanvotedic[indcan[3]]})')
        outputfile.writelines('-------------------------')
        outputfile.writelines(f'winner: {winner}')
        outputfile.writelines('-------------------------')