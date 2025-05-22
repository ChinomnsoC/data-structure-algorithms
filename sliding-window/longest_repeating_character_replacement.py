from collections import defaultdict


def longest_repeating_character_replacement(s, k):
    if k == len(s):
        return k
    if len(set(s)) == 1:  # checking for the same characters in the string
        return len(s)
    length_of_string = len(s)
    character_freq = defaultdict(int)
    left, right, max_frequency = 0, 0, 0
    max_repeating_character_count = 0

    for right in range(length_of_string):
        character_freq[s[right]] += 1
        print(character_freq)
        max_frequency = max(max_frequency, character_freq[s[right]])
        print(max_frequency, character_freq[s[right]])

        window_size = right - left + 1
        print(window_size)
        character_to_change = window_size - max_frequency
        print(character_to_change)

        if character_to_change > k:
            character_freq[s[left]] -= 1
            left += 1

        max_repeating_character_count = max(
            max_repeating_character_count, right - left + 1
        )

    print(max_repeating_character_count)
    return max_repeating_character_count


# Example usage
sample = "aaacbbbaabab"
longest_repeating_character_replacement(sample, 2)

