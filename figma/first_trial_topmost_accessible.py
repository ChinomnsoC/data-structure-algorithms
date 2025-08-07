# id: "2",
# parentId: "1",
# type: "folder",
# name: "folder1",
# accessibleBy: ["user1", "user2"]

# build the tree where map node object to the node id, parent to child
# find all accessible nodes for each user
# for each accessible node, find out if its ancestor is accessible
# if the ancestor is not accessible, append node to list,
# return list of topmost accessible nodes


# build the tree where map node object to the node id, parent to child

from typing import Optional, List

class FileSystemNode:
    def __init__(self, id: str, parent_id: Optional[str], node_type: str, name: str, accessible_by: List[str]):
        self.user_id = id
        self.parent_id = parent_id
        self.type = node_type
        self.name = name
        self.accessible_by = set(accessible_by)
    
    def is_accessible_by(self, user_id):
        return user_id in self.accessible_by
    
class FileSystemManager:
    def __init__(self, file_system_data):
        self.file_system_node = {}
        self.parent_map = {}
        
        for node_data in file_system_data:
            node = FileSystemNode(
                id=node_data["id"],
                parent_id=node_data["parentId"],
                node_type=node_data["type"],
                name=node_data["name"],
                accessible_by=node_data["accessible_by"]
            )
            
        self.file_system_node[node.id] = node
        self.parent_map[node.id] = node.parent_id
    
    # find all accessible nodes for each user
    def find_all_accessible_nodes(self, user_id):
        accessible_nodes = set()
        
        for node in self.file_system_node.values():
            if node.is_accessible_by(user_id):
                accessible_nodes.add(node)
                
        return accessible_nodes
    
    # for each accessible node, find out if its ancestor is accessible
    def _is_ancestor_accessible(self, user_id, accessible_set):
        current_id = self.parent_map.get(user_id)
        
        while current_id:
            if current_id in accessible_set:
                return True
            current_id = self.parent_map.get(current_id)
        
        return False
    
    def find_topmost_accessible_node(self, user_id):
        
        accessible_nodes = self.find_all_accessible_nodes(user_id)
        
        accessible_ids = {node.id for node in accessible_nodes} 
        
        topmost_accessible_node = []
        
        for accessible_node in accessible_nodes:
            if not self._is_ancestor_accessible(accessible_node.id, accessible_ids):
                topmost_accessible_node.append(accessible_node)
        
        return topmost_accessible_node
