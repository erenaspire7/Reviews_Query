#pylint:disable=W0312
import re

def apply(text):
	return re.sub("<([^<])+>", "", text)
