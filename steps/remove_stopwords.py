#pylint:disable=W0312
import nltk

def apply(text):
	try:
		from nltk.corpus import stopwords
		from nltk.tokenize import word_tokenize
		stop_words = set(stopwords.words( 'english' ))
		word_tokens = word_tokenize(text)
		filtered_sentence = [w for w in word_tokens if not w in stop_words]
	except :
		print("Downloading NLTK resources")
		nltk.download("stopwords")
		nltk.download("punkt")
		return apply(text)
	return " ".join(filtered_sentence)
		
