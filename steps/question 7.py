#"""### **TASK 7: Check if the word is made up of English letters and is not alpha-numeric**"""

def letters_only(text):
    """substitutes alphanumeric"""
    return re.sub("[^a-zA-Z\s]", "", text)

DF['Text'] = DF['Text'].apply(letters_only)

DF.head()