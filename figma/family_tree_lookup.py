# from typing import List
class FamilyTree:
    def __init__(self, id, parent_id, children):
        self.id = id #user id
        self.parent_id = parent_id #their parent's id
        self.children = children # their children, a list of ids, or empty


class FamilyLookUp:
    def __init__(self, family_tree_data):
        self.family_generation_map = {}
        self.family_tree_data_node = {}

        flat_list = self._flatten_family_tree(family_tree_data)

        for node_data in flat_list:
            family_tree_node = FamilyTree(
                id=node_data["id"],
                parent_id=node_data["parent_id"],
                children=node_data["children"]
            )
            self.family_tree_data_node[family_tree_node.id] = family_tree_node
            self.family_generation_map[family_tree_node.id] = family_tree_node.parent_id

            print(self.family_generation_map)
    
    def _flatten_family_tree(self, node, parent_id=None):
        flat_list = [{
            "id": node["id"],
            "parent_id": parent_id,
            "children": [child["id"] for child in node["children"]]
        }]
        for child in node["children"]:
            flat_list.extend(self._flatten_family_tree(child, node["id"]))
        return flat_list
    

    def get_parent(self, person_id):
        return self.family_generation_map.get(person_id)

    # Write a function get_member(member_id) that returns the node (object) for a specific person.  
    def get_member(self, person_id):
        return self.family_tree_data_node.get(person_id)


    # Write a function rename_member(member_id, new_id) that changes the member’s ID.
    def rename_member(self, person_id, new_id):
        person_node = self.get_member(person_id)
        parent_id_of_person = self.get_parent(person_id)

        if not person_node:
            return f"{person_id} not found"

        #  then update the map to say that the parent of person id is now the parent of new id instead.
        self.family_generation_map.pop(person_id, None)
        self.family_generation_map[new_id] = parent_id_of_person


        # if person node, update the node to have the new id
        if person_node:
            del self.family_tree_data_node[person_id]
            # self.family_tree_data_node[person_node.id] = new_id
            person_node.id = new_id
            self.family_tree_data_node[new_id] = person_node
       

        # then update children
        if parent_id_of_person and parent_id_of_person in self.family_tree_data_node:
            parent_node = self.family_tree_data_node[parent_id_of_person]

            parent_node.children = [
                new_id if child_id == person_id else child_id for child_id in parent_node.children
            ]
        
        for child_id in person_node.children:
            self.family_generation_map[child_id] = new_id

        return self.get_member(new_id)
            



family_data = {
    "id": "grandparent",
    "children": [
        {
            "id": "parent1",
            "children": [
                {"id": "child1", "children": []},
                {"id": "child2", "children": []}
            ]
        },
        {
            "id": "parent2",
            "children": [
                {"id": "child3", "children": []}
            ]
        }
    ]
}

fs = FamilyLookUp(family_tree_data=family_data)
result = fs.get_member("child1")
print("result.id", result.id, result.parent_id, result.children)

results = fs.rename_member("child1", "child4")
print("results.id", results.parent_id, results.children)