def most_frequent_ip(lines: list) -> str:
    if not lines:
        return 0
    
    ip_frequency_map = {}
    
    for line in lines:
        ip_address = line.split(" ")[0]
        # if ip_address not in map
        if ip_address not in ip_frequency_map:
            ip_frequency_map[ip_address] = 1
            continue
        # add ip address to map, with freq 1
        else:
            ip_frequency_map[ip_address] += 1
        # else increase frequency by plus 1
    # sort the map, return a formatted string
    # "10.0.0.1,10.0.0.2"
    max_freq = max(ip_frequency_map.values())
    ties = []
    for key, value in ip_frequency_map.items():
        
        if value == max_freq:
            ties.append(key)
            
    return ",".join(sorted(ties))

def do_tests_pass() -> bool:
    lines1 = [
        "10.0.0.1 - GET 2020-08-24",
        "10.0.0.1 - GET 2020-08-24",
        "10.0.0.2 - GET 2020-08-20"
    ]
    assert most_frequent_ip(lines1) == "10.0.0.1"
    
    # tie case
    lines2 = [
        "10.0.0.1 - GET 2020-08-24",
        "10.0.0.2 - GET 2020-08-24",
    ]
    assert most_frequent_ip(lines2) == "10.0.0.1,10.0.0.2"
    
    # single entry
    lines3 = ["10.0.0.1 - GET 2020-08-24"]
    assert most_frequent_ip(lines3) == "10.0.0.1"
    
    return True

if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")