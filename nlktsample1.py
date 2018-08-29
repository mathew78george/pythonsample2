# import nltk
# nltk.download()
from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
print(example_text)
tokens = sent_tokenize(example_text)
sentence = word_tokenize(example_text)
print(tokens)
print(sentence)