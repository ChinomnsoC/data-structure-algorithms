# pythontrainingData = [
#     ["I", "am", "Sam"],
#     ["Sam", "I", "am"],
#     ["Green", "Eggs", "I", "like"],
#     ["Green", "Eggs", "and", "ham"]
# ]
# ```

# Implement a class `AutoComplete` with:


# **Part 1:**
# - `__init__(self, trainingData, badWords)` — initialise the model
# - `getBestWord(self, inputString)` — return the most frequent next word for a given input word, or empty string if none exists
# ```
# getBestWord("I") → "am"  # "am" follows "I" twice, "like" once
# getBestWord("Green") → "Eggs"
# getBestWord("xyz") → ""

# Part 2:

# updateTrainingData(self, newTrainingData) — update model with new sentences

# Part 3:

# Filter out bad words — if either word in a pair appears in badWords, ignore that pair

from collections import defaultdict, Counter

training_data = [
    ["I", "am", "Sam"],
    ["Sam", "I", "am"],
    ["Green", "Eggs", "I", "like"],
    ["Green", "Eggs", "and", "ham"]
]
class Autocomplete():
    def __init__(self, trainingData, badWords):
        self.trainingData = trainingData
        self.badWords = badWords
        
        self.data_map = defaultdict(Counter)
        
        self._build_map(self.trainingData)
        


    def getBestWord(self, inputString):
        inputString = inputString.lower()
        if inputString not in self.data_map:
            return ""
        
        freq_dict = self.data_map[inputString]
        
        return max(freq_dict, key=freq_dict.get)
    
    def updateTrainingData(self, newTrainingData):
        
        self._build_map(newTrainingData)
    
    def _build_map(self, trainingData):
        
        for sentence in trainingData:
            for i in range(len(sentence) - 1):
                current_word = sentence[i].lower()
                next_word = sentence[i+ 1].lower()
                
                if current_word not in self.badWords and next_word not in self.badWords:
                    self.data_map[current_word][next_word] += 1
        
        print(self.data_map)

autocomplete = Autocomplete(trainingData=training_data, badWords=["ugly"])

print(autocomplete.getBestWord("I"))
print(autocomplete.getBestWord("Am")) 