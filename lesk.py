import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('wordnet')
sentence="He went to the bank to deposit money"
words=word_tokenize(sentence)
sense=lesk(words,"bank")
print(sense)
print(sense.definition())
