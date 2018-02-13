## Carter Merenstein
## Middlebury College
''' Reads in text files downloaded from factiva, filters out common words
stems words, and then outputs a csv of article, date, and frequency of words.'''


import csv
import os
import re
from nltk import PorterStemmer

pattern = re.compile('\W|\d') # not an alphanumeric

articles = {} #articles with words
article_dates = {}
all_words = {}
article_sources = {} #document number corresponds to source

txt_paths =  "C:\\CDocs\\Annas_thesis\\txtgroups"

def isNewArticle(line_arr):
    ''' the easiest identifier for a new article is that they start with a wordcount, e.g. "999 words"
    takes in a line already split into a list'''
    try:
        condition2 = (line_arr[1].strip('\n') == 'words') ## needs to be separate
    except:
        return False # an error occurs if there is < 2 words. In this case we know it's not a new article
    return (re.match('[0-9]', line_arr[0]) != None and condition2)

for txt in os.listdir(txt_paths):
    started = False #can't classify things before the title
    new_article = False #used to pull name, source, date from articles
    filename = txt_paths + '\\' + txt
    with open(filename, 'r', encoding = "utf8") as group:
        i = 0
        article_title = ''  #separate out by article
        two_lines_ago = ''      #always hold this to be able to snatch the title
        last_line = ''
        date = '' #always after wordcount
        source = txt.strip('.txt') # just a number, Anna can sort later
        for line in group:
            line_arr = line.split(' ')
            if isNewArticle(line_arr):
                article_title = two_lines_ago
                articles[article_title] = {}
                i += 1
                started = True # so we don't get an error on the first few lines
                new_article = True
            elif started: #just if we're past the first 2 lines of the document
                for word in line_arr:
                    if new_article:
                        date = line
                        article_dates[article_title] = date
                        new_article = False
                        article_sources[article_title] = source
                    else:
                        word = re.sub(pattern, '', word) #get rid of commas and stuff
                        word = word.lower()
                        word = PorterStemmer().stem_word(word) #get root of word
                        try:
                            articles[article_title][word] += 1
                            all_words[word] += 1
                        except:
                            articles[article_title][word] = 1
                            try:
                                all_words[word] += 1
                            except:
                                all_words[word] = 0
            two_lines_ago = last_line
            last_line = line


with open('stemmedWordFreq.csv ', 'w', newline='', encoding="utf8") as out:
    w = csv.writer(out)
    article_names = []
    header = ['']
    for article in articles.keys():
        article_names.append(article)
        header.append(article)
    w.writerow(header)
    article_dates_row = [''] #another row for the dates
    for article in article_names:
        article_dates_row.append(article_dates[article]) #put the date in the row below the article
    w.writerow(article_dates_row)
    article_source_row = ['']
    for article in article_names:
        article_source_row.append(article_sources[article])
    w.writerow(article_source_row)
    for word in all_words.keys():
        if all_words[word] >= 100:
            line = [word]
            for article in article_names:
                try:
                    line.append(articles[article][word])
                    
                except KeyError:
                    line.append(0)
w.writerow(line)