# hw56@iu.edu

"""
This module implements a left-to-right longest-match algorithm for Japanese as described in Section 3.9.1 in Jurafsky
and Martin (2nd Edition).

First I construct a Japanese wordlist from UD_Japanese-GSD/ja_gsd-ud-train.conllu. If wordlist.json is not present in
the current directory, run generate_wordlist() before

Then I build a Maxmatch class to tokenize Japanese.

Please note, before running, set the current working directory as the course repo ".../LING-L545".

```python

# Usage

mm = Maxmatch()

raw = "三島 由紀夫 (1925年 - 1970年）は、日本の小説家・劇作家・随筆家・評論家・政治活動家・皇国主義者。戦後の日本文学界を代表する作家の一\
人であると同時に、ノーベル文学賞候補になるなど、日本語の枠を超え、海外においても広く認められた作家である。代表作は『仮面の告白』『潮騒』『金閣寺\
』『近代能楽集』『サド侯爵夫人』などがある。"

mm.maxmatch(raw)

```

"""
import os
import conllu
import json
from functools import reduce

CONLLU_TRAIN_DIR = './01_Tokenisation/ja_gsd-ud-train.conllu'
CONLLU_TEST_DIR = './01_Tokenisation/ja_gsd-ud-test.conllu'
WORDLIST_DIR = './01_Tokenisation/wordlist.json'
REFERENCE_DIR = './01_Tokenisation/reference.txt'
HYPOTHESIS_DIR = './01_Tokenisation/hypothesis.txt'
# the longest Japanese word contains 19 chars in the file ja_gsd-ud-train.conllu
MAX_WORDLEN = 19


class Maxmatch(object):
    """
    This module implements a left-to-right longest-match algorithm as described in Section 3.9.1 in Jurafsky and Martin
 (2nd Edition).
    """
    def __init__(self):
        self.wordlist = json.load(open(WORDLIST_DIR, 'r'))
        # check if the wordlist already in place, if not, generate one
        if not os.path.exists('./01_Tokenisation/wordlist.json'):
            generate_wordlist(input_dir=CONLLU_TRAIN_DIR, output_dir=WORDLIST_DIR)

    def maxmatch(self, sent):
        """
        This function does the heavy lifting.
        No explicit check of the input language will be executed, but we do assume the user only feed in a
        Japanese string.

        Args:
            sent: A Japanese English raw text (in string type).

        Returns:
            A list of strings, each string represents a token.
        """
        tokens = []
        index = 0

        while index < len(sent):
            success = False
            for i in range(MAX_WORDLEN, 0, -1):
                candidate = sent[index: index + i]
                if candidate in self.wordlist:
                    tokens.append(candidate)
                    success = True
                    break
            # if the token is not in the wordlist, segment as unigram
            if not success:
                tokens.append(sent[index])
                i = 1

            index += i
        return tokens


def generate_wordlist(input_dir, output_dir):
    """
    This function generate a wordlist in json format by taking in a .conllu file and extracting unique words from
    it.
    Args:
        input_dir: the position of the input .conllu file.
        output_dir: the position of the output wordlist.json.

    Returns:
        A list of strings, each string represents a token.
    """
    source = conllu.parse(open(input_dir, 'r').read())

    wordlist = []

    for item in source:
        wordlist.extend([a['form'] for a in item])

    wordlist = list(set(wordlist))

    with open(output_dir, 'w') as f:
        json.dump(wordlist, f)


def generate_hypothesis_reference(input_dir=CONLLU_TEST_DIR):
    """
    This function return a reference and a hypothesis (list) by taking in a .conllu file.

    Args:
        input_dir: the position of the input .conllu file.

    Returns:
        `reference` contains the right for WER computing.
        `hypothesis` contains the raw Japanese that will be tokenized by the maxmatch and checked against the `reference`
    """
    source = conllu.parse(open(input_dir, 'r').read())

    hypothesis = [(reduce(lambda x, y: x + y, [token['form'] for token in tokenlist])) for tokenlist in source]
    reference = [(reduce(lambda x, y: x + " " + y, [token['form'] for token in tokenlist])) for tokenlist in source]

    return reference, hypothesis

