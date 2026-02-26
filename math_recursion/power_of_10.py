def is_power_of_ten(n: int) -> bool:
    if n < 0:
        return False
    
    while n > 1:
        if n % 10 != 0:
            False
        n //= 10
        
    return True


def do_tests_pass() -> bool:
    assert is_power_of_ten(1) == True  # 10^0
    assert is_power_of_ten(10) == True
    assert is_power_of_ten(100) == True
    assert is_power_of_ten(1000) == True
    assert is_power_of_ten(0) == False
    assert is_power_of_ten(-10) == False
    assert is_power_of_ten(11) == False
    assert is_power_of_ten(99) == False
    return True


if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")
