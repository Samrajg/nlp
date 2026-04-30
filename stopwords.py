import nltk
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
sentence="Godwin is learning Natural Language Processing and it is fun"
words=nltk.word_tokenize(sentence)
stop_words=set(stopwords.words('english'))
filtered_words=[word for word in words if word.lower() not in stop_words]
print(filtered_words)
