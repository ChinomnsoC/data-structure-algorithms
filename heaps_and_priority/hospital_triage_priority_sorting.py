def treatment_order(severities: list, k: int) -> int:
    """
    In a hospital emergency room, patients are treated based on severity.
    Given an array of severities and an index k, return the treatment order (1-based) of the patient at index k.

    Higher severity is treated first
    If same severity, earlier arrival (smaller index) is treated first

    Args:
        severities (list): _description_
        k (int): _description_

    Returns:
        int: _description_
    """
    if not severities or k >= len(severities):
        return 0

    severities_to_position_pair_list = sorted(enumerate(severities), key=lambda x: (-x[1], x[0]))
    
    return next(i + 1 for i, (indx, _) in enumerate(severities_to_position_pair_list) if indx == k)

    # for i in range(len(severities)):
    #     severities_to_position_pair_list.append((severities[i], i))



    # severities_to_position_pair_list.sort(key=lambda x: (-x[0], x[1]))
    
    # for i, pair in enumerate(severities_to_position_pair_list):
    #     if pair[1] == k:
    #         return i + 1
    
    


def do_tests_pass() -> bool:
    # Basic case
    print(treatment_order([3, 1, 4, 4, 2], 2))
    assert treatment_order([3, 1, 4, 4, 2], 2) == 1  # severity 4, treated first
    assert treatment_order([3, 1, 4, 4, 2], 3) == 2  # severity 4, arrived later
    assert treatment_order([3, 1, 4, 4, 2], 0) == 3  # severity 3, treated third
    assert treatment_order([3, 1, 4, 4, 2], 4) == 4  # severity 2
    assert treatment_order([3, 1, 4, 4, 2], 1) == 5  # severity 1, treated last
    assert treatment_order([5], 0) == 1  # single patient
    assert treatment_order([1, 1, 1], 1) == 2  # all same severity
    return True


if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")
