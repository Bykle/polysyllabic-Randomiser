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
    
    def replaceWord(self, word, firstLetters=2, keepCaptial=True, keepPunctuation=True):
        # Count how many syllables are in this word
        syllableCount = countSyllables(word)
        
        # Search for similar words
        try:
            potentialWords = self.dictionary[word[0:firstLetters].lower()][str(syllableCount)]
        except KeyError:
            # If no replacement word exists, then just return the same word :(
            return word
        
        # Select one at random
        newWord = potentialWords[random.randint(0, len(potentialWords))]
        
        # If our original word was capitalised, then capitalise this one too.
        if keepCaptial and word[0].isupper():
            newWord = newWord.title()
        
        # TODO: Support brackets (){}[]
        # If our original word had some sort of punctuation, then copy it over.
        if keepPunctuation and word[-1] in ['?','.',',','!']:
            newWord += str(word[-1])

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

    def interactiveInput(self, exitTerm=""):
        try:
            sentence = input('> ')
            while sentence != exitTerm:
                print(self.replaceSentence(sentence))
                sentence = input('> ')
        except EOFError:
            # Catch if a user pressed CTRL+D (EOF)
            print("")
            return
        except KeyboardInterrupt:
            # Catch if a user pressed CTRL+C (SIGINT)
            print("")
            return
            
if __name__=="__main__":
    Randomiser("dictionary.json").interactiveInput()