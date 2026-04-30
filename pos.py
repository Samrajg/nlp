import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
sentence = "Godwin is learning Natural Language Processing"
words = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(words)
print(pos_tags)
