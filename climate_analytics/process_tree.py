# **Process Tree (IDB)**

# An operating system has these rules:
# - Each process is spawned from a parent process (except the first)
# - If a parent process is aborted, all child processes are aborted too
# - One process crashed and brought down all its descendants

# You're given the full list of crashed processes with their immediate children. 
# Find the ID of the process that crashed first (the root of the crash).

# ```python
crashed_processes = [
    {"id": 10, "children": [15, 9]},
    {"id": 15, "children": [1, 2]},
    {"id": 1,  "children": []},
    {"id": 2,  "children": []},
    {"id": 9,  "children": [4]},
    {"id": 4,  "children": []}
]

# Output: 10
# ```

def process_tree(crashed_processes):
    if not crashed_processes:
        return
    children = set()
    
    # ids in id that are not in children
    
    for process in crashed_processes:
        for child in process['children']:
            children.add(child)
    
    for process in crashed_processes:
        if process['id'] not in children:
            return process['id']    
        
print(process_tree(crashed_processes))
