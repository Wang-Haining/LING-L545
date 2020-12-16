"""
1. Why should we split punctuation from the token it goes with ?
Answer: Because punctuation and word are different in semantics and functionality. We usually care more about the words
and the semantics they carry. But sometimes we also concern the use of punctuation, e.g. author profiling.

2. Should abbreviations with space in them be written as a single token or two tokens ?
Answer: In one token is fine. If we treat each word as the minimum semantic unit. I don't see any good to split them.
Though I found some pre-trained model (like BERT) would harness the substrings if the word is not in the model, this is
more like a expediency.

3. How about numerals like 134 000 ?
Answer: It should remain in one word if we uphold the "atomic semantic unit" principle :).

4. If you have a case suffix following punctuation, how should it be tokenised ?
Answer: As far as I know, some linguists treat "I'm" as one token (e.g. NLTK) but others would split it into "I'" and
"m" (e.g. spaCy). It seems splitting them is better since the spaCy is a latter one. But I don't know why...
know which is better. But

5. Should contractions and clitics be a single token or two (or more) tokens ?
Answer: I prefer one token.

"""


import sys

# for c in sys.stdin.read():
#     raw = c

def tokeniser(raw):
    """
    A simple approach, and the one we are going to first, would simply be to replace every space ' ' with a newline
    character '\n'. Following that you can use the replace() function to preprocess the text to add a space before or
    after certain punctuation characters like ',', ':', '(' and ')'.

    Args:
        raw: a string
    Return:
        a segmented string
    """
    print(raw.replace(",", " ,").replace(":", " :").replace("(", " (").replace(")", " )").replace(' ', '\n'))


if __name__ == "__main__":
    raw = sys.argv[1]
    tokeniser(raw)
