#"""### **TASK 8: Check to see if the length of the word is greater than 2**"""

def check_length(text):
    text = text.split()
    contain = []

    for words in text:
        if len(words) > 2:
            contain.append(words)

    final = ' '.join(contain)
    return final

DF['Text'] = DF['Text'].apply(check_length)

DF.head()