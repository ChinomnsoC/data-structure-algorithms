# **Auto Corrector (IDB)**

# Design a data structure initialised with a dictionary of words. 
# Given a search word, if it exists return it. If not, check if you can change **exactly one character** to match any word in the dictionary. If yes, return the corrected word. If no match found, return the original word.

# ```python
dictionary = ["cat", "bat", "hat", "car"]

# correct("cat") → "cat"   # exists
# correct("bat") → "bat"   # exists  
# correct("bad") → "bat"   # one char change: d→t
# correct("can") → "cat"   # one char change: n→t  
# correct("xyz") → "xyz"   # no match, return original
# ```
from typing import List

class AutoCorrector:
    def __init__(self, words: List):
        self.dictionary_of_words = words
        
    def correct(self, search_word):
        for word in self.dictionary_of_words:
            if len(word) != len(search_word):
                continue
            
            false_counter = 0
            for i in range(len(word)):
                if word[i] != search_word[i]:
                    false_counter += 1
                    if false_counter > 1:
                        break
            
            if false_counter <= 1:
                return word

        return search_word
                
                
                
auto_corrector = AutoCorrector(dictionary)
# auto_corrector.dictionary_of_words = dictionary

print(auto_corrector.correct("avuuu"))
print(auto_corrector.correct("tab"))
print(auto_corrector.correct("bad"))