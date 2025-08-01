# 🔴 Question 3 (Hierarchical Data): Parent Lookup
# You are given a list of employees and their managers. Build a hash map to quickly look up the manager of any given employee.

# Input:

# python
# Copy
# Edit
relationships = [
    ("Alice", "Bob"),     # Alice reports to Bob
    ("Bob", "Catherine"), # Bob reports to Catherine
    ("David", "Bob")
]
# Your Task:
# Build a employee_to_manager dictionary.
# Write a function: get_manager(employee: str) -> str
# Write a function: get_top_manager(employee: str) that recursively finds the highest-level manager (like the CEO).


class RelationshipManager:
    def __init__(self, relationships):
        self.employee_to_manager = {}
    
        for employee, manager in relationships:
            self.employee_to_manager[employee] = manager
        
        print(self.employee_to_manager)
            
    def get_manager(self, employee,):
        return self.employee_to_manager.get(employee)
    
    def get_top_manager(self, employee):
        # another solution
        # while self.get_manager(employee):
        #     employee = self.get_manager(employee)
            
        # return employee
        manager = self.get_manager(employee)
        if not manager:
            return employee
        
        return self.get_top_manager(employee)

rtt = RelationshipManager(relationships)

# ====================================================
# 🟡 Question 2: Counting Occurrences
# You are given a list of words. Count how many times each word appears using a hash map.

# Input:

# python
# Copy
# Edit
from collections import Counter, defaultdict
from typing import List
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# Your Task:

# Use a dictionary (or collections.Counter) to map each word to its count.

# Output: {"apple": 3, "banana": 2, "orange": 1}

# Using counter
words_dict = Counter(words)
print(words_dict)


# Using a simple function
def create_word_dict(words: List[str]):
    word_dicts = defaultdict(int)
    
    for word in words:
        word_dicts[word] += 1
        
    return word_dicts
print(create_word_dict(words))

# Using OOP
class WordDictionary:
    def __init__(self, words):
        self.word_dictionary = {}
        
        for word in words:
            if word not in self.word_dictionary:
                self.word_dictionary[word] = 0
            self.word_dictionary[word] += 1
            print("self.word_dictionary", self.word_dictionary)
            
    def get_word_count(self, word):
        word_count = self.word_dictionary.get(word, 0)
        return word_count

# ====================================================
# 🟢 Question 1: Basic Key-Value Lookup
# You are given a list of cities and their temperatures. 
# Build a hash map and write a function that returns the temperature for a given city.

# Input:

# python
# Copy
# Edit
city_data = [("Lagos", 30), ("Cairo", 35), ("Nairobi", 25)]
# Your Task:
# Build a city_to_temp hash map.
# Write a function: get_temperature(city: str) -> int

class CityTemperatures:
    def __init__(self, city_data):
        self.city_to_temp = {}
        
        for city, temperature in city_data:
            self.city_to_temp[city] = temperature
            
    def get_temperature(self, city):
        return self.city_to_temp.get(city)