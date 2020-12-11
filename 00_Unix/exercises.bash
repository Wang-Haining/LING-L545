# below results are computed from datadump of Aragonese on 20201201

# 1. Exercises with grep


# How many uppercase words are there in the Aragonese Wikipedia? Lowercase? Hint: wc -l or grep -c
# there are 124,526 uppercase words
gsed 's/[^a-zA-Z]\+/\n/g' < wiki.txt | grep -c '^[A-Z]\+$'

# there are 5,705,152 lowercase words
gsed 's/[^a-zA-Z]\+/\n/g' < wiki.txt | grep -c '^[a-z]\+$'

# How many 4-letter words?
# 512,463 4-letter words
gsed 's/[^a-zA-Z]\+/\n/g' < wiki.txt | grep -ic '^[a-z]\{4\}$'

# Are there any words with no vowels?
# Yes, there are 791,573 of them. But most of them are abbreviations
# like d, y, km, etc.
gsed 's/[^a-zA-Z]\+/\n/g' < wiki.txt | grep -ic '^[^aeiou]\+$'

# Find ‘’1-syllable’’ words (words with exactly one vowel)
# There are 2,554,330 of them.
gsed 's/[^a-zA-Z]\+/\n/g' < wiki.txt | grep -ic '^[^aeiou]*[aeiou][^aeiou]*$'

# Find ‘’2-syllable’’ words (words with exactly two vowels)
# there are 1,358,390 of them
gsed 's/[^a-zA-Z]\+/\n/g' < wiki.txt | grep -ic '^[^aeiou]*[aeiou][^aeiou]*[aeiou][^aeiou]*$'

# 2. Exercises with sed

# Count word initial consonant sequences: tokenise by word, delete the vowel and the rest of the word, and count
gsed 's/[^A-Za-z]\+/\n/g' < wiki.txt |
gsed -e 's/^[aeiouAEIOU]\+//g' -e 's/[aeiouAEIOU]\+.*$//g' |
sort -r | uniq -c | sort -r > initial-consonants.hist

# Count word final consonant sequences

gsed 's/[^A-Za-z]\+/\n/g' < wiki.txt |
gsed -E 's/^.*([^aeiouAEIOU]+)[aeiouAEIOU]+$|^.*([^aeiouAEIOU])+$|^[aeiouAEIOU]*$/\1\2/' |
sort -r | uniq -c | sort -r > final-consonants.hist