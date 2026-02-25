import string

def missing_characters(sentence: str) -> str:
    
    alphabets_set = set(string.ascii_lowercase)
    
    if not sentence:
        return "".join(sorted(alphabets_set))
    
    i = 0
    
    # "this is a boy"
    for char in sentence:
        if char.isalpha():
            alphabets_set.discard(char.lower())
    
    # at this point we have a set of alphabets not in the string.
    return "".join(sorted(alphabets_set))

print(missing_characters("The quick brown fox jumps over the lazy dog") == "")
print(missing_characters("The quic brown fox jumps over the lazy dog") == "k")
print(missing_characters("") == "abcdefghijklmnopqrstuvwxyz")