import os
import re

parpath = os.path.join('paragraph_2.txt')
with open(parpath, 'r') as parpathtext:
    lines = parpathtext.read()
    
    
    
    #remove /n frmo end of strign
    linesNon = lines.replace("\n",'')


    #convert paragraph into list of words
    parlist = []
    parlist = re.split("[, \-!?:<>()]+", linesNon)
    
  
    #wordcount
    wordcount = 0
    for word in parlist:
        wordcount += 1

    #average word length
    wordlen = []
    for word in parlist:
        wordlen.append(int(len(word)))

    avgwordlen = round((sum(wordlen) / len(wordlen)), 2)
    
    
    #number of sentences
    sentlist = []
    sentlist = re.split("(?<=[.!?]) +", linesNon)
    numsent = len(sentlist)

    #average sentence length
    sentlen = []
    for sentence in sentlist:
        sentlen.append(int(len(sentence)))
    
    avgsentlen = round((sum(sentlen) / len(sentlen)), 2)
   
    print('Paragraph Analysis')
    print('-----------------')
    print(f'Approximate Word Count: {wordcount}')
    print(f'Approximate Sentence Count: {numsent}')
    print(f'Average Letter Count: {avgwordlen}')
    print(f'Average Sentence Length: {avgsentlen}')