#pylint:disable=W0312
import nltk

def apply(text):
	from nltk.corpus import stopwords
	from nltk.stem import SnowballStemmer 
	
	snowball_stemmer = SnowballStemmer('english')
	word_tokens = nltk.word_tokenize(text)
	stemmed_word = [snowball_stemmer.stem(word) for word in word_tokens]
	return " ".join(stemmed_word)

