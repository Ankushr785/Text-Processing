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