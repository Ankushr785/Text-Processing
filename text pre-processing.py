# -*- coding: utf-8 -*-
"""
Created on Wed May  3 20:02:53 2017

@author: Ankush Raut
"""





noise_list = ['is', 'a', 'this', 'that', 'etc']

def remove_noise(input_speech):
    words = input_speech.split() 
    noise_free_words = [word  
    for word in words 
    if word not in noise_list] 
    noise_free_text = " ".join(noise_free_words) 
    return noise_free_text

remove_noise("this is a sample text")



# Sample code to remove a regex pattern 
import re 

def _remove_regex(input_text, regex_pattern):
    urls = re.finditer(regex_pattern, input_text) 
    for i in urls: 
        input_text = re.sub(i.group().strip(), '', input_text)
    return input_text

regex_pattern = "#[\w]*"  

_remove_regex("remove this #hashtag from analytics vidhya", regex_pattern)

from nltk.stem.wordnet import WordNetLemmatizer 
lem = WordNetLemmatizer()

from nltk.stem.porter import PorterStemmer 
stem = PorterStemmer()

word = "multiplying" 
lem.lemmatize(word, "v")

stem.stem(word)




lookup_dict = [{'rt':'Retweet', 'dm':'direct message', "awsm" : "awesome", "luv" :"love"}]
def _lookup_words(input_text):
    words = input_text.split() 
    new_words = [] 
    for word in words:
        if word.lower() in lookup_dict:
            word = lookup_dict[word.lower()]
        new_words.append(word) 
        new_text = " ".join(new_words) 
    return new_text

_lookup_words("RT this is a retweeted tweet by Shivam Bansal")


#  Convert text to lowercase
input_str = "The 5 biggest countries by population in 2017 are China, India, United States, Indonesia, and Brazil."
input_str = input_str.lower()
print(input_str)

# Remove stop words
input_str = "NLTK is a leading platform for building Python programs to work with human language data."
stop_words = set(stopwords.words(‘english’))
from nltk.tokenize import word_tokenize
tokens = word_tokenize(input_str)
result = [i for i in tokens if not i in stop_words]
print (result)
# A scikit-learn tool also provides a stop words list:
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
# It’s also possible to use spaCy, a free open-source library:
from spacy.lang.en.stop_words import STOP_WORDS

# Stemming using NLTK
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
stemmer= PorterStemmer()
input_str="There are several types of stemming algorithms."
input_str=word_tokenize(input_str)
for word in input_str:
    print(stemmer.stem(word))
    
# Part-of-speech tagging using TextBlob
input_str="Parts of speech examples: an article, to write, interesting, easily, and, of"
from textblob import TextBlob
result = TextBlob(input_str)
print(result.tags)

# Chunking using NLTK
input_str="A black television and a white stove were bought for the new apartment of John."
from textblob import TextBlob
result = TextBlob(input_str)
print(result.tags)

# Named-entity recognition using NLTK
from nltk import word_tokenize, pos_tag, ne_chunk
input_str = "Bill works for Apple so he went to Boston for a conference."
print ne_chunk(pos_tag(word_tokenize(input_str)))
