def highest_average_score(scores: list) -> int:
    scores_map = {}
    
    for student_result in scores:
        if student_result[0] not in scores_map:
            scores_map[student_result[0]] = []
        scores_map[student_result[0]].append(student_result[1])
    
    # find the average of each key and update the values in the map
    for student_id, scores_list in scores_map.items():
        average_score = sum(scores_list) // len(scores_list)
        
        scores_map[student_id] = average_score
    
    highest_score = max(scores_map.values())
    ties = []
    
    for student_id, average_score in scores_map.items():
        if average_score == highest_score:
            ties.append(student_id)
    
    winner = min(ties)
    
    return winner
        

def do_tests_pass() -> bool:
    # Basic case
    scores1 = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 61]]
    assert highest_average_score(scores1) == 2  # avg: 1->76, 2->89

    # Tie - return smaller ID
    scores2 = [[1, 100], [2, 100]]
    assert highest_average_score(scores2) == 1

    # Single student
    scores3 = [[1, 85], [1, 90]]
    assert highest_average_score(scores3) == 1

    # From your original list
    scores4 = [[1, 87], [2, 35], [1, 52], [3, 35], [2, 55], [4, 99]]
    assert highest_average_score(scores4) == 4  # Jessica=99, avg: 1->69, 2->45, 3->35, 4->99

    return True

if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")