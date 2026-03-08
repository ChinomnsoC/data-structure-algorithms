def highest_average_score(scores: list) -> int:
    scores_map = {}
    
    if not scores:
        return 0
    
    for student_result in scores:
        if not student_result:
            return 0
        student_name = student_result[0]
        if student_name not in scores_map:
            scores_map[student_name] = [0, 0]
        
        score = int(float(student_result[1]))

        # scores_map = {"name": [total_score, count]}
        scores_map[student_name][0] += score
        scores_map[student_name][1] += 1
        
    return max(total_score // count for total_score, count in scores_map.values())
        

def do_tests_pass() -> bool:
    # Basic case
    scores1 = [["Ben", "91"], ["Murray", "92"], ["Bruce", "93"], ["Angela", "97"], ["Ben", "60"], ["Murray", "77"], ["Bruce", "61"]]
    
    print(highest_average_score(scores1))
    assert highest_average_score(scores1) == 97  # avg: 1->76, 2->89

    # Tie - return smaller ID
    scores2 = [[]]
    assert highest_average_score(scores2) == 0

    # # Single student
    scores3 = [["Ben", "-91"], ["Murray", "-92"], ["Bruce", "93"], ["Angela", "-7"], ["Ben", "60"], ["Murray", "77"], ["Bruce", "61"]]
    print(highest_average_score(scores3))
    assert highest_average_score(scores3) == 77

    # # From your original list
    scores4 = [["Ben", "-91"], ["Murray", "-92"], ["Bruce", "-93"], ["Angela", "-7.5"], ["Ben", "-60"], ["Murray", "-77"], ["Bruce", "-61"]]
    print(highest_average_score(scores4))
    assert highest_average_score(scores4) == -7
    
    scores5 = []
    assert highest_average_score(scores5) == 0
    
    scores6 = [["Ben", "-91"]]
    assert highest_average_score(scores6) == -91
    
    scores7 = [["Ben", "0"], ["Murray", "0"], ["Bruce", "0"]]
    assert highest_average_score(scores7) == 0

    return True

if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")
        
        
#  scores1 = [["Bob", "87"], ["Mike", "35"], ["Bob", "52"]]