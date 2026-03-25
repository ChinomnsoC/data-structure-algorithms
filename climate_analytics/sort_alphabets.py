
letters = [
    "a",
    "b",
    "c",
    "ch",
    "d",
    "dd",
    "e",
    "f",
    "ff",
    "g",
    "ng",
    "h",
    "i",
    "l",
    "ll",
    "m",
    "n",
    "o",
    "p",
    "ph",
    "r",
    "rh",
    "s",
    "t",
    "th",
    "u",
    "w",
    "y"
]
# **Sort Alphabets / Welsh Alphabet (IDB)**

# You're sorting words according to the Welsh alphabet order. Welsh has digraphs — 
# two characters treated as a single letter.

# **Welsh alphabet order:**
# `a, b, c, ch, d, dd, e, f, ff, g, ng, h, i, l, ll, m, n, o, p, ph, r, rh, s, t, th, u, w, y`

# **Rules:**
# - Digraphs take priority — `dd` is always one letter, never `d` + `d`
# - Longer matches take precedence

# ```
#         [6,21], [17,1,12], [5,7,1] [6], [11,1,12]
# Input:  ["ddr", "nah", "dea", "dd", "ngah"]
# Output: ["dea", "dd", "ddr", "ngah", "nah"]
# ```



def sort_alphabets(input):
    welsh_alphabet_map = {}
    
    for i, char in enumerate(letters):
        welsh_alphabet_map[char] = i + 1
        
    
    
    def create_tokens(word):
        i = 0
        word_token = []
        while i < len(word):
            if i + 1 < len(word) and word[i:i+2] in welsh_alphabet_map:
                word_token.append(word[i:i+2])
                i+=2
            else:
                word_token.append(word[i])
                i+= 1
        return word_token

    def get_key(word):
        tokens = create_tokens(word)
        
        return [welsh_alphabet_map[token] for token in tokens ]
    
    return sorted(input, key=get_key)

        
    
print(sort_alphabets(["ddr", "nah", "dea", "dd", "ngah"]))
    

