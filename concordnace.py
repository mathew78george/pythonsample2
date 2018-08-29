import nltk
nltk.download()
def get_all_phases_containing_tar_wrd(target_word, tar_passage, left_margin=10, right_margin=10):
    """
        Function to get all the phases that contain the target word in a text/passage tar_passage.
        Workaround to save the output given by nltk Concordance function

        str target_word, str tar_passage int left_margin int right_margin --> list of str
        left_margin and right_margin allocate the number of words/pununciation before and after target word
        Left margin will take note of the beginning of the text
    """

    ## Create list of tokens using nltk function
    tokens = nltk.word_tokenize(tar_passage)
    print("Tokenns------------->",tokens)

    ## Create the text of tokens
    text = nltk.Text(tokens)
    print("Text----",text)
    ## Collect all the index or offset position of the target word
    c = nltk.ConcordanceIndex(text.tokens, key=lambda s: s.lower())

    ## Collect the range of the words that is within the target word by using text.tokens[start;end].
    ## The map function is use so that when the offset position - the target range < 0, it will be default to zero
    concordance_txt = (
    [text.tokens[map(lambda x: x - 5 if (x - left_margin) > 0 else 0, [offset])[0]:offset + right_margin]
     for offset in c.offsets(target_word)])

    ## join the sentences for each of the target phrase and return it
    return [''.join([x + ' ' for x in con_sub]) for con_sub in concordance_txt]


## Test the function

raw = """The way to get along in the world is to do things as well as you can.&amp;amp;quot; Fortunately for that little pig,\
          he learned that lesson. And he just lived happily ever after!"""

tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
text.concordance('words')  # default text.concordance output

## output:


print
print
'Results from function'
results = get_all_phases_containing_tar_wrd('words', raw)
for result in results:
    print
    result

## output:
## Results from function
