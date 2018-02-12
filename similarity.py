from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords,wordnet
from nltk.stem import WordNetLemmatizer
from itertools import product
import numpy

# str1 = "Abhishek is a good boy."
# str2 = "Abhishek is not a bad boy."
# str1 = "Cat is drinking water."
# str2 = "Lions eat flesh."
# str1 = "He loves to play football."
# str2 = "Football is his favourite sport."
# str1 = "Many consider Maradona as the best player in soccer history."
# str2 = "Maradona is one of the best soccer player."

str1 = "I was given a card by her in the garden."
str2 = "In the garden, she gave me a card."

# str1 = "Ballmer has been vocal in the past warning that Linux is a threat to Microsoft."
# str2 = "In the memo, Ballmer reiterated the open-source threat to Microsoft."
# str1 = "The boy is fetching water from the well."
# str2 = "The lion is running in the forest."
# str1 = "A school is a place where kids go to study."
# str2 = "School is an institution for children who want to study."
# str1 = "The world knows it has lost a heroic champion of justice and freedom."
# str2 = "The earth recognizes the loss of a valiant champion of independence and justice."
# str1 = "A cemetery is a place where dead people's bodies or their ashes are buried."
# str2 = "A graveyard is an area of land ,sometimes near a church, where dead people are buried." 

##---------------Defining stopwords for English Language---------------##
stop_words = set(stopwords.words("english"))

##---------------Initialising Lists---------------##
filtered_sentence1 = []
filtered_sentence2 = []
lemm_sentence1 = []
lemm_sentence2 = []
sims = []
temp1 = []
temp2 = []
simi = []
final = []
same_sent1 = []
same_sent2 = []
#ps = PorterStemmer()

##---------------Defining WordNet Lematizer for English Language---------------##
lemmatizer  =  WordNetLemmatizer()

#myfile =  open('Text1.txt', 'r') 
#data=myfile.read().replace('\n', '')
##print(sent_tokenize(example_text))
##
##print(word_tokenize(example_text))

##---------------Tokenizing and removing the Stopwords---------------##

for words1 in word_tokenize(str1):
    if words1 not in stop_words:
        if words1.isalnum():
            filtered_sentence1.append(words1)

##---------------Lemmatizing: Root Words---------------##

for i in filtered_sentence1:
    lemm_sentence1.append(lemmatizer.lemmatize(i))
    
#print(lemm_sentence1)


##---------------Tokenizing and removing the Stopwords---------------##

for words2 in word_tokenize(str2):
    if words2 not in stop_words:
        if words2.isalnum():
            filtered_sentence2.append(words2)

##---------------Lemmatizing: Root Words---------------##

for i in filtered_sentence2:
    lemm_sentence2.append(lemmatizer.lemmatize(i))
    
#print(lemm_sentence2)

##---------------Removing the same words from the tokens----------------##
##for word1 in lemm_sentence1:
##    for word2 in lemm_sentence2:
##        if word1 == word2:
##            same_sent1.append(word1)
##            same_sent2.append(word2)
##            
##if same_sent1 != []:
##   for word1 in same_sent1:
##    lemm_sentence1.remove(word1)
##if same_sent2 != []:
##   for word2 in same_sent2:
##    lemm_sentence2.remove(word2)
##            
##print(lemm_sentence1)
##print(lemm_sentence2)

##---------------Similarity index calculation for each word---------------##
for word1 in lemm_sentence1:
    simi =[]
    for word2 in lemm_sentence2:
        sims = []
       # print(word1)
        #print(word2)
        syns1 = wordnet.synsets(word1)
        #print(syns1)
        #print(wordFromList1[0])
        syns2 = wordnet.synsets(word2)
        #print(wordFromList2[0])
        for sense1, sense2 in product(syns1, syns2):
            d = wordnet.wup_similarity(sense1, sense2)
            if d != None:
                sims.append(d)
    
        #print(sims)
        #print(max(sims))
        if sims != []:        
           max_sim = max(sims)
           #print(max_sim)
           simi.append(max_sim)
             
    if simi != []:
        max_final = max(simi)
        final.append(max_final)

#print(final)

#        if max_sim >= 0.7:
#           print(word1)
#           print(word2)
#           print('\n')
           
#           if word1 not in temp1:
#              temp1.append(word1)
#           if word2 not in temp2:
#              temp2.append(word2)   
           #lemm_sentence1.remove(word1)
           #lemm_sentence2.remove(word2)          
        #if wordFromList1 and wordFromList2: #Thanks to @alexis' note
          #  s = wordFromList1[0].wup_similarity(wordFromList2[0])
           # list.append(s)
#for word1 in temp1:
#    lemm_sentence1.remove(word1)

#for word2 in temp2:
#    lemm_sentence2.remove(word2)
    
#print(lemm_sentence1)
#print(lemm_sentence2)


##---------------Final Output---------------##

similarity_index = numpy.mean(final)
similarity_index = round(similarity_index , 2)
print("Sentence 1: ",str1)
print("Sentence 2: ",str2)
print("Similarity index value : ", similarity_index)

if similarity_index>0.8:
    print("Similar")
elif similarity_index>=0.6:
    print("Somewhat Similar")
else:
    print("Not Similar")