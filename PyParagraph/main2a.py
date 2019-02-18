import os
import re

parpath = os.path.join('paragraph_2.txt')
with open(parpath, 'r') as parpathtext:
   lines = parpathtext.readlines()
    
   
   #attempt at removing \n.  What is going on with these things?
   linelist = []
   for line in lines:
      linelist.append(line.replace('\n', ' '))

   #removing extra white lines from list
   while ' ' in linelist:
      linelist.remove(' ')

   #make the text one string
   paragraph = ''
   for line in linelist:
      paragraph = paragraph + line

   #Remove quotes from paragraph
   parnoquote = paragraph.replace('"', '')

   
   #remove the apostrophies from string
   #THIS IS THE FINAL STRING TO USE
   paragraphnoap = parnoquote.replace("'", '')

   #convert paragraph into list of words
   wordlist = []
   wordlist = re.split('[, \-!?:<>()]+', paragraphnoap)

    
   #wordcount
   wordcount = 0
   for word in wordlist:
      wordcount += 1
   
   #average word length
   wordlen = []
   for word in wordlist:
      wordlen.append(int(len(word)))

   avgwordlen = round((sum(wordlen) / len(wordlen)), 2)

   #number of sentences
   sentlist = []
   sentlist = re.split('(?<=[.!?]) +', paragraphnoap)
   numsent = len(sentlist)
   #PROBLEM, Anne V. Coates is separating the sentence.  How could you separate this without knowing it's a middle initial?


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