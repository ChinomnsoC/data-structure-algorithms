from typing import Optional, List

# In terms of approach, here's how I'm thinking I can solve it:
# 1. Find all accessible nodes for the user
# 2. For each accessible node, check if any of its ancestors are also accessible
# 3. If an ancestor is accessible, remove this node from result
# 4. Return remaining nodes. This will return the topmost accessible node(s) for each user.

class FileSystemNode:
    def __init__(self, id: str, parent_id: Optional[str], node_type: str, name: str, accessible_by: List[str]):
        self.id = id
        self.parent_id = parent_id
        self.type = node_type
        self.name = name
        self.accessible_by = set(accessible_by)
    
    def is_accessible_by(self, user_id):
        return user_id in self.accessible_by
    
class FileSystem:
    def __init__(self, file_system_node_data):
        self.file_system_nodes = {}
        self.parent_map = {}
        
        
        for node_data in file_system_node_data:
            node = FileSystemNode(
                id=node_data["id"],
                parent_id=node_data["parentId"],
                node_type=node_data["type"],
                name=node_data["name"],
                accessible_by=node_data["accessibleBy"]
            )
            self.file_system_nodes[node.id] = node
            self.parent_map[node.id] = node.parent_id
    
    def _is_ancestor_accessible(self, node_id, accessible_set):
        current_id = self.parent_map.get(node_id)
        while current_id:
            if current_id in accessible_set:
                return True
            current_id = self.parent_map.get(current_id)
        return False
    

    def find_topmost_accessible_node(self, user_id):
        
        # for this user id, find all accessible nodes
        accessible_nodes = self.find_accessible_nodes(user_id)
        
        accessible_ids = {node.id for node in accessible_nodes}
        
        topmost_node = []
        # for each accessible node, check if the parent node is accessible
        for accessible_node in accessible_nodes:
            if not self._is_ancestor_accessible(accessible_node.id, accessible_ids):
                topmost_node.append(accessible_node)
            
            print("topmost_node", topmost_node)
            # check if the parent node is accessible
        
        
        return topmost_node
        #  if the parent node is accessible, remove current node
        # return remaining accessible node(s)
    
    def find_accessible_nodes(self, user_id):
        accessible = set()
        
        for node in self.file_system_nodes.values():
            if node.is_accessible_by(user_id):
                accessible.add(node)
        return accessible
        
# ---------- 🧪 Test Case ----------
if __name__ == "__main__":
    file_system_data = {
        "nodes": [
            {
                "id": "1",
                "parentId": None,
                "type": "folder",
                "name": "root",
                "accessibleBy": ["user1"]
            },
            {
                "id": "2",
                "parentId": "1",
                "type": "folder",
                "name": "folder1",
                "accessibleBy": ["user1", "user2"]
            },
            {
                "id": "3",
                "parentId": "2",
                "type": "file",
                "name": "file1",
                "accessibleBy": ["user2"]
            }
        ]
    }
    fs = FileSystem(file_system_data["nodes"])
    result = fs.find_topmost_accessible_node("user2")

    print("Topmost accessible nodes for user2:")
    for node in result:
        print(f"- {node.name} ({node.type})")  # Expected: folder1         