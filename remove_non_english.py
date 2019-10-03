#pylint:disable=W0312
import re

def apply(text):
	return re.sub("[^a-zA-Z\s]", "", text)
