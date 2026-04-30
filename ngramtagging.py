text = "social media analytics helps detect trends"
words = text.split()
print("Original Text :", text)
print("Words List    :", words)
unigrams = words
print("\nUnigrams (1-word each):")
for u in unigrams:
    print(u)
bigrams = list(zip(words, words[1:]))
print("\nBigrams (2-word pairs):")
for b in bigrams:
    print(b)
trigrams = list(zip(words, words[1:], words[2:]))
print("\nTrigrams (3-word groups):")
for t in trigrams:
    print(t)
