from typing import Optional, List
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
        
    def find_topmost_accessible_node(self, user_id):
        topmost_accessible_nodes= []
        roots = []
        
        
        for node_id, node in self.file_system_nodes.items():
            if node.parent_id is None:
                roots.append(node)
        
        # for root in roots, is this node accessible by userid?
        for root in roots:
            self._process_node(root, user_id, topmost_accessible_nodes)
        # if yes, append to topmost_accessible_nodes
        # if no, get the children of root, and process again from top.
        return topmost_accessible_nodes
    
    def _process_node(self, node, user_id, topmost_accessible_nodes):
        if node.is_accessible_by(user_id):
            topmost_accessible_nodes.append(node)
        
        else:
            children = self._get_children(node)
            for child in children:
                self._process_node(child, user_id, topmost_accessible_nodes)           
            
    def _get_children(self, node):
        children = []
        
        for child_id, parent_id in self.parent_map.items():
            if parent_id == node.id:
                children.append(self.file_system_nodes[child_id ])
        
        return children
    
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
        print(f"- {node.name} ({node.type}), whole node: {result}")  # Expected: folder1  