from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

example_text = "This is a sample sentence, showing off the stop words filtration."

words = word_tokenize(example_text);
stop_words = set(stopwords.words("english"))

filtered_words = [w for w in words if not w in stop_words]
# for w in words:
#     if w not in stop_words:
#         filtered_words.append(w)
    
print(filtered_words)
    
    

