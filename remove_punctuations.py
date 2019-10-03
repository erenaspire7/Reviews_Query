#pylint:disable=W0312
import re

def apply(text):
	text = re.sub("[-\.]+", " ", text)
	return re.sub("[^A-z0-9\s]+", "", text)
