import os
import re

par1path = os.path.join('paragraph_1.txt')
with open(par1path, 'r') as par1pathtext:
    lines1 = par1pathtext.read()
    
    
    #remove /n frmo end of strign
    linesNon = lines1.replace("\n", '')

    #convert paragraph into list of words
    par1list = []
    par1list = re.split("[, \-!?:<>()]+", linesNon)
    
    #wordcount
    wordcount = 0
    for word in par1list:
        wordcount += 1

    #average word length
    wordlen = []
    for word in par1list:
        wordlen.append(int(len(word)))

    avgwordlen = round((sum(wordlen) / len(wordlen)), 2)
    
    
    #number of sentences
    sentlist = []
    sentlist = re.split("(?<=[.!?]) +", linesNon)
    numsent = len(sentlist)
    
    #average sentence length
    sentlen = []
    for sentence in sentlist:
        sentlen.append(len(re.split("[, \-!?:<>()]+", sentence)))
    

    avgsentlen = round((sum(sentlen) / len(sentlen)), 2)
   
    print('Paragraph Analysis')
    print('-----------------')
    print(f'Approximate Word Count: {wordcount}')
    print(f'Approximate Sentence Count: {numsent}')
    print(f'Average Letter Count: {avgwordlen}')
    print(f'Average Sentence Length: {avgsentlen}')