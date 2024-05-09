#!/usr/bin/env python3

from common import countSyllables
import json
import random

class Randomiser:
    def __init__(self, dictionaryPath):
        self.dictionaryPath = dictionaryPath
        self.dictionary = self.loadDictionary(self.dictionaryPath)

    def loadDictionary(self, path):
        with open(path,'r') as handle:
            return json.load(handle)
    
    def replaceWord(self, word, keepCaptial=True):
        # Count how many syllables are in this word
        syllableCount = countSyllables(word)
        
        # Search for similar words
        potentialWords = self.dictionary[word[0].lower()][str(syllableCount)]
        
        # Select one at random
        newWord = potentialWords[random.randint(0, len(potentialWords))]
        
        # If our original word was capitalised, then capitalise this one too.
        if keepCaptial and word[0].isupper():
            newWord = newWord.title()
        
        # Return our new word
        return newWord
    
    def replaceSentence(self, sentence, minSyllables=1, keepCaptials=True):
        # Get a list of our words in the sentence
        words = sentence.split(' ')

        # Enumerate over them
        for idx, word in enumerate(words):
            
            # If our word has enough syllables, then replace it, retaining capitalisation.
            if countSyllables(word) > minSyllables:
                words[idx] = self.replaceWord(word, keepCaptial=keepCaptials)
        
        # Join and return our new funky string
        return ' '.join(words)

if __name__=="__main__":
    randomiser = Randomiser("dictionary.json")
    print(randomiser.replaceSentence('For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element, a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.'))