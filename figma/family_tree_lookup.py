# Question 1: Family Tree Lookup (from JSON)
# You are given a JSON-like object representing a simple family tree:

# family_data = {
#     "id": "grandparent",
#     "children": [
#         {
#             "id": "parent1",
#             "children": [
#                 {"id": "child1", "children": []},
#                 {"id": "child2", "children": []}
#             ]
#         },
#         {
#             "id": "parent2",
#             "children": [
#                 {"id": "child3", "children": []}
#             ]
#         }
#     ]
# }
# Your tasks:
# - Build a tree structure (classes + hash map for fast ID lookup).
# - Write a function get_member(member_id) that returns the node (object) for a specific person.
# - Write a function rename_member(member_id, new_id) that changes the member’s ID.

