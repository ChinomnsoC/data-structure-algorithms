def josephus(n: int, k: int) -> int:

    def josephus_recursion(people, current_position, k):

        if len(people) == 1:
            return people[0]

        position_to_be_del = (current_position + (k - 1) ) % len(people)
        if position_to_be_del < len(people) - 1:
            next_person = people[position_to_be_del + 1]
        else:
            next_person = people[0]

        people.remove(people[position_to_be_del])
        return josephus_recursion(people, people.index(next_person), k)

    people = list(range(1, n + 1))
    print(people)
    current_person = 0

    return josephus_recursion(people, current_person, k)


def do_tests_pass() -> bool:
    assert josephus(1, 1) == 1
    assert josephus(4, 2) == 1
    assert josephus(5, 2) == 3
    assert josephus(6, 2) == 5
    assert josephus(7, 3) == 4
    return True


if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")
