# import all libraries
import pandas as pd
import numpy
import sqlite3
from pandasgui import show
# connect to database
conn = sqlite3.connect("database.sqlite")
# read the sql
df = pd.read_sql_query("""select UserId, ProductId,
                          ProfileName, Time,
                          Score, Text, COUNT(*)
                          FROM reviews
                          WHERE Score != 3
                          GROUP BY UserId
                          HAVING COUNT(*) > 1""", conn)
# answer to number one and two question
ONE_AND_TWO = df
show(ONE_AND_TWO.head())

df.sort_values('ProductId', inplace=True)
df.drop_duplicates(subset="ProductId",
                   keep=False, inplace=True)
# answer to number three question
THREE = df
show(THREE.head())
# answer to number four question
POSITIVE_REVIEWS = df['Score'].value_counts()[5] + df['Score'].value_counts()[4]
NEGATIVE_REVIEWS = df['Score'].value_counts()[2] + df['Score'].value_counts()[1]

print("The number of positive reviews are " + str(POSITIVE_REVIEWS), 'reviews')
print("The number of negative reviews are " + str(NEGATIVE_REVIEWS), 'reviews')

from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)
# answer to number five question
def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

df['Text'] = df['Text'].apply(strip_tags)

FIFTH = df
show(FIFTH.head())

import re
# answer to number six question
def remove_characters(text):
    return re.sub("[^A-z0-9\s]+", "", text)

df['Text'] = df['Text'].apply(remove_characters)

SIXTH = df
show(SIXTH.head())
# answer to number seven question
def remove_non_english(text):
    return re.sub("[^a-zA-Z\s]", "", text)

df['Text'] = df['Text'].apply(remove_non_english)

SEVENTH = df
show(SEVENTH.head())
# answer to number eight question
def check_length(text):
    text = text.split()
    contain = []

    for words in text:
        if len(words) > 2:
            contain.append(words)

    final = ' '.join(contain)
    return final

df['Text'] = df['Text'].apply(check_length)

EIGHT = df
show(EIGHT.head())
# answer to number nine question
def lower_case(text):
    return text.lower()

df['Text'] = df['Text'].apply(lower_case)

NINTH = df
show(NINTH.head())
# answer to number ten question
import nltk

def remove_stopwords(text):
    try:
        from nltk.corpus import stopwords
        from nltk.tokenize import word_tokenize
        stop_words = set(stopwords.words( 'english' ))
        word_tokens = word_tokenize(text)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]

    except:
        print("Downloading NLTK resources")
        nltk.download("stopwords")
        nltk.download("punkt")
        return remove_stopwords(text)

    return " ".join(filtered_sentence)

df['Text'] = df['Text'].apply(remove_stopwords)

TENTH = df
show(TENTH.head())
# answer to number eleven question
# answer to number eleven question
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import nltk
def stem_thy_words(text):

    snowball_stemmer = SnowballStemmer('english')
    word_tokens = nltk.word_tokenize(text)
    stemmed_word = [snowball_stemmer.stem(word) for word in word_tokens]
    return " ".join(stemmed_word)

df['Text'] = df['Text'].apply(stem_thy_words)

ELEVENTH = df
show(ELEVENTH.head())
