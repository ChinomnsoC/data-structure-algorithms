from collections import defaultdict


def find_duplicate(paths):
    directory_map = defaultdict(list)
    result = []

    for path in paths:
        splitted_path = path.split(" ")
        directory = splitted_path[0]

        for i in range(1, len(splitted_path)):
            filename_and_content = splitted_path[i]
            key = filename_and_content.split("(")[1].split(")")[0]
            filename = filename_and_content.split("(")[0]
            directory_reconstructed = directory + "/" + filename
            if key not in directory_map:
                directory_map[key] = []
            directory_map[key].append(directory_reconstructed)
    for key, value in directory_map.items():
        if len(value) >= 2:
            result.append(value)
    return result


# Example usage
# paths = [
#     "root/projectA 1.py(script1)",
#     "root/projectB 2.py(script2)",
#     "root/projectB/module 3.py(script3)",
#     "root/projectC/module 4.py(script1)",
#     "root/projectC 5.py(script2)",
# ]

# expected_output = [
#     ["root/projectA/1.py", "root/projectC/module/4.py"],
#     ["root/projectB/2.py", "root/projectC/5.py"],
# ]
