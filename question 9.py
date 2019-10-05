#"""### **TASK 9: Convert the word to lowercase**"""

def lower_case(text):
    """forces lowercase"""
    return text.lower()

DF['Text'] = DF['Text'].apply(lower_case)

DF.head()