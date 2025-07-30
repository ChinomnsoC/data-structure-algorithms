# // Example 1:
# Input: keyword = "fig", text = "figma"
# Output: "<b>fig</b>ma"

# // Example 2:
# Input: keyword = "ana", text = "banana"
# Output: "b<b>anana</b>"  
# // NOT "b<b>ana</b>na" - we want to bold the maximum coverage
class KeywordHighlighter:
    def __init__(self, keyword):
        self.keyword = keyword
    
    def highlight_keywords(self, text: str):
        
        matches = self.find_matches(text=text)
        merged_intervals = self.merge_intervals_in_matches(matches=matches)
        
        result = ""
        lastIndex = 0
        
        for start, end in merged_intervals:
            result += text[lastIndex:start]
            print("result 1 and lastIndex 1", result, lastIndex)
            result += f"<b>{text[start:end + 1]}</b>"
            print("result 2 and lastIndex 2", result, lastIndex)
            lastIndex = end + 1
            print("result 3 and lastIndex 3", result, lastIndex)
        
        
        print("merged intervals", merged_intervals)
        return result
        
        
    def find_matches(self, text: str):
        matches = []
    
        for i in range(len(text) - len(self.keyword)+1):
            print("checking")
            if text[i:i + len(self.keyword)] == self.keyword:
                matches.append((i, i + len(self.keyword)-1))
                print(matches)
        if not matches:
            return text
        
        return matches
    
    def merge_intervals_in_matches(self, matches):
        merged_intervals = [matches[0]]
        
        for match in matches[1:]:
            if match[0] <= merged_intervals[-1][1]:
                merged = [min(match[0], merged_intervals[-1][0]), max(match[1], merged_intervals[-1][1])]
                merged_intervals[-1] = merged
            else:
                merged_intervals.append(match)

        return merged_intervals
    


def find_matches(keyword: str, text: str):
    matches = []
    
    for i in range(len(text) - len(keyword)+1):
        print("checking")
        if text[i:i + len(keyword)] == keyword:
            matches.append((i, i + len(keyword)-1))
            print(matches)
    
    if not matches:
        return text
        
    merged_intervals = [matches[0]]
        
    for match in matches[1:]:
        if match[0] <= merged_intervals[-1][1]:
            merged = [min(match[0], merged_intervals[-1][0]), max(match[1], merged_intervals[-1][1])]
            merged_intervals[-1] = merged
        else:
            merged_intervals.append(match)
            
    # use the values in the tuples in matches to add the B tags.
    # // Build result string with bold tags
    result = ""
    lastIndex = 0
    
    for start, end in merged_intervals:
        result += text[lastIndex:start]
        print("result 1 and lastIndex 1", result, lastIndex)
        result += f"<b>{text[start:end + 1]}</b>"
        print("result 2 and lastIndex 2", result, lastIndex)
        lastIndex = end + 1
        print("result 3 and lastIndex 3", result, lastIndex)
        
        
    print("merged intervals", merged_intervals)
    return result
                    
                    
# print(find_matches("ana", "bananaavocadoana"))
highlight = KeywordHighlighter(keyword="ana")
print(highlight.highlight_keywords(text="bananaavocadoana"))