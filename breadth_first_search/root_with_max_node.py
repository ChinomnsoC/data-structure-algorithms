def find_largest_tree_root(forest: dict) -> int:
    if not forest:
        return 0
    children = set(forest.keys())
    parents = set(forest.values())
    print("children", children)
    print("parents", parents)

    root_count = {}

    for child in forest.keys():
        current = child
        while current in forest:
            current = forest[current]

        root_count[current] = root_count.get(current, 0) + 1

    # if there's no tie:
    answer = max(root_count.items(), key=lambda x: (x[1], -x[0]))[0]

    return answer


def do_tests_pass() -> bool:
    # No tie - tree rooted at 2 has 3 nodes (1,3,4), tree rooted at 4 has 1 node... wait
    # {1:2, 3:2, 4:2} -> root 2, size 3
    assert find_largest_tree_root({1: 2, 3: 2, 5: 6, 7: 6, 9: 6}) == 6

    # Tie - two trees of equal size, return smaller root
    # {1:2, 3:4} -> root 2 (size 1), root 4 (size 1) -> tie, return 2
    assert find_largest_tree_root({1: 2, 3: 4}) == 2

    return True


if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")
