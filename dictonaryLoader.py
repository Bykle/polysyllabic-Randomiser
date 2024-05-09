#!/usr/bin/env python3

# Generates an organised dictionary for use with the randomiser

from common import countSyllables
import requests
import json

# Compatible source dictionaries.
sources = {
    # Contains a list of over 470k words, might have some weird ones
    "ALL_WORDS":"https://github.com/dwyl/english-words/raw/master/words_alpha.txt",
    # Contains more common words, could be less interesting but might make sentences that generally just make more sense.
    "COMMON_WORDS":"https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt"
}

# Select a dictionary here.
listUrl = sources["COMMON_WORDS"]

# We will save our dictionary file here.
dictionaryFile = 'dictionary.json'

def fetchWords(url):
    request = requests.get(url)
    delimeter = '\n'
    
    if request.status_code != 200:
        raise Exception(f"HTTP: {request.status_code} - Failed to request word list.")

    try:
        return request.text.split(delimeter)
    except:
        raise Exception("Could not split word list. Is this a valid list?")

def generateDict(words, firstLetters=2):
    dictionary = {}
    
    for word in words:
        word = word.strip()
        
        # Don't process any empty lines
        if len(word) == 0:
            continue
        
        # Count how many syllables are in this word.
        syllableCount = countSyllables(word)
        
        # Add a new first letters index to our dict if it does not exist
        if not word[0:firstLetters] in dictionary:
            dictionary[word[0:firstLetters]] = {}
        
        # Add a syllable count to our index if it does not exist
        if not syllableCount in dictionary[word[0:firstLetters]]:
            dictionary[word[0:firstLetters]][syllableCount] = []
        
        # Add the word to our dict, sorted by first letters and syllable count
        dictionary[word[0:firstLetters]][syllableCount].append(word)
    
    return dictionary

def main(url, file):
    print(f"Fetching words from: {url}")
    words = fetchWords(url)
    
    print(f"Got {len(words)} words. Generating dictionary file.")
    dictionary = generateDict(words)

    print(f"Generated dictionary, writing contents to {file}.")
    with open(file, 'w') as handle:
        json.dump(dictionary, handle, indent=4)

if __name__=="__main__":
    main(url=listUrl,
        file=dictionaryFile)