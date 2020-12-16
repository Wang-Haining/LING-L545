"""
This module is used to build a naive segmenter.

Questions
1. How should you segment sentences with semi-colon? As a single sentence or as two sentences? Should it depend on
context?
Answer: Yes, context matters. It depends on whether the initial after the semi-colon is capitalized or not and whether
the following clause is grammarly complete.

2. Should sentences with ellipsis... be treated as a single sentence or as several sentences?
Answer: I always treat ellipsis as the ending of a single sentence.

3. If there is an exclamation after the first word in the sentence should it be a separate sentence? How about if there
is a comma?
Answer: If there is an exclamation after the first word, then there are two sentences. But if there is a comma instead,
it should be one sentence. The first situation is common when the first word is a vocative ("John! watch out!"). The
second situation is very common with a adjective ("Frankly, there is no evidence.").

4.Can you think of some hard tasks for the segmenter?
Answer: If there many abbreviations in the middle of a sentence, it would cause confusion to a naive segmenter.
"""
import sys


def segmenter(raw):
    """
    Replaces every full stop '.' followed by a space ' ' with a full stop and a newline character '\n'.

    Args:
        raw: a string
    Return:
        print out a segmented string
    """
    print(raw.replace(". ", ".\n"))


if __name__ == "__main__":
    raw = sys.argv[1]
    segmenter(raw)
