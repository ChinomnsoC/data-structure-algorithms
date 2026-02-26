import re


def shortest_distance(document: str, word1: str, word2: str) -> float:
    if not document:
        return 0

    min_distance = float("inf")

    word1_midpoints = []
    word2_midpoints = []
    
    # if no match for either word 1 or word 2, return -1.0
    

    for match in re.finditer(word1, document, re.IGNORECASE):
        start_position = match.start()

        mid_point_wd1 = start_position + len(word1) / 2
        word1_midpoints.append(mid_point_wd1)
        
        

    for match in re.finditer(word2, document, re.IGNORECASE):

        start_position = match.start()
        mid_point_wd2 = start_position + len(word2) / 2
        word2_midpoints.append(mid_point_wd2)
        
    if not word1_midpoints or not word2_midpoints:
        return -1.0         

    for p in word1_midpoints:
        for q in word2_midpoints:
            distance = abs(p - q)

            min_distance = (
                distance
                if min_distance == float("inf")
                else min(distance, min_distance)
            )

    return float(min_distance)


def do_tests_pass() -> bool:

    assert (
        shortest_distance("This is a sample document we just made up", "we", "just")
        == 4.0
    )
    assert (
        shortest_distance("This is a sample document we just made up", "is", "a") == 2.5
    )
    assert shortest_distance("cat dog cat dog", "cat", "dog") == 4.0
    assert shortest_distance("hello world", "hello", "nothere") == -1.0
    return True


if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")
