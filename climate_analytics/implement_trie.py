# All three are O(n) where n is the length of the word/prefix. None are O(1) — they all loop through characters.
# Space for the entire Trie is O(n × m) where n is number of words and m is average word length.

class TrieNode():
    def __init__(self):
        self.children_dict = {}
        self.is_end = False
        
# insert(word) — walk down, create nodes as needed
# search(word) — walk down, return True if path exists AND is_end is True
# startsWith(prefix) — walk down, return True if path exists (don't check is_end)

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        
        for char in word:
            if char not in node.children_dict:
                node.children_dict[char] = TrieNode()
            
            node = node.children_dict[char]
        
        node.is_end = True
    
    def search(self, word):
        current_node = self.root
        
        for char in word:
            
            if char not in current_node.children_dict:
                return False
            
            current_node = current_node.children_dict[char]
            
        
        return current_node.is_end
    
    def startsWith(self, prefix):
        current_node = self.root
        
        
        for char in prefix:
            if char not in current_node.children_dict:
                return False
            
            current_node = current_node.children_dict[char]
        
        return True
