# Build the tree to establish parent-> child relationship
# Start from the root(parent), drop down left
# For each node, if the user has access to this node, add node to result, go back up, then go right.
# If the user doesn't have access to this node, process the children of this node.
# left, root, and then right
# Return result.

# team. -> folder -> subfolder -> file

class Team:
  def __init__(self, uuid, folder_ids, file_ids, user_ids):
    self.uuid = uuid
    self.folder_ids = folder_ids
    self.file_ids = file_ids
    self.user_ids = user_ids

class Folder:
  def __init__(self, uuid, folder_ids, file_ids, user_ids):
    self.uuid = uuid
    self.folder_ids = folder_ids
    self.file_ids = file_ids
    self.user_ids = user_ids

class File:
  def __init__(self, uuid, user_ids):
    self.uuid = uuid
    self.user_ids = user_ids


class HierarchyManager:
    def __init__(self):
        self.parent_map = {}
        self.id_to_node = {}
        
    def has_access(self, node, user_id):
        return user_id in node.user_ids
    
        
    def init_function(self, teams, folders, files):
        
        for file in files:
            self.id_to_node[file.uuid] = file
        
        
        for folder in folders:
            self.id_to_node[folder.uuid] = folder
            
            for sub_folder_ids in folder.folder_ids:
                self.parent_map[sub_folder_ids] = folder.uuid
            
            for file_id in folder.file_ids:
                self.parent_map[file_id] = folder.uuid
            
        for team in teams:
            self.id_to_node[team.uuid] = team
            
            for folder_id in team.folder_ids:
                self.parent_map[folder_id] = team.uuid
            
            for file_id in team.file_ids:
                self.parent_map[file_id] = team.uuid
        # See all keys in id_to_node
        print("All node IDs:", list(self.id_to_node.keys()))

        # See all key-value pairs in id_to_node  
        for node_id, node_obj in self.id_to_node.items():
            print(f"'{node_id}' -> {type(node_obj).__name__} with users {node_obj.user_ids}")

        # See all parent-child relationships
        for child_id, parent_id in self.parent_map.items():
            print(f"'{child_id}' has parent '{parent_id}'")

    def get_fewest(self, user_id):
        # if the node is not in parent map, then its a root
        # for all the roots, check if the user has access, 
        # if the user doesn't, we check the children.
        minimum_access_nodes = []
        roots = []
        
        
        for node_id, node in self.id_to_node.items():
            if node_id not in self.parent_map:
                roots.append(node)
                
        for root in roots:
            self._process_node(root, user_id, minimum_access_nodes)   
        
        return minimum_access_nodes
                
    def _process_node(self, node, user_id, minimum_access_nodes):
        if self.has_access(node, user_id):
            minimum_access_nodes.append(node)
        else:
            children = self._get_children(node)
            for child in children:
                self._process_node(child, user_id, minimum_access_nodes)
            
    
    def _get_children(self, node):
        print(node.uuid)
        children = []
        for child_id, parent_id in self.parent_map.items():
                if parent_id == node.uuid:
                    children.append(self.id_to_node[child_id])
        
        return children
    
    
    
# =================== USAGE EXAMPLE ===================
def test_complex_hierarchy():
    # =================== FILES (Bottom Layer) ===================
    files = [
        File("report.pdf", ["Alice"]),           # In Marketing/Campaigns
        File("budget.xlsx", ["Bob"]),            # In Marketing/Campaigns  
        File("design.fig", ["Alice", "Bob"]),    # In Development/Frontend/Components
        File("api.py", ["Bob"]),                 # In Development/Backend/Services
        File("readme.txt", ["Alice"]),           # Directly in Operations folder
        File("notes.md", ["Alice", "Bob"]),       # In Development/Backend/Services/Utils
        File("show.txt", ["Bob"]), 
    ]
    
    # =================== FOLDERS (Multiple Layers) ===================
    folders = [
        # Layer 4 - Deepest subfolders
        Folder("Components", [], ["design.fig"], ["Alice"]),
        Folder("Services", ["Utils"], ["api.py"], []),          # No direct access
        Folder("Utils", [], ["notes.md"], ["Bob"]),
        Folder("Campaigns", [], ["report.pdf", "budget.xlsx"], ["Alice"]),
        
        # Layer 3 - Mid-level folders  
        Folder("Frontend", ["Components"], [], ["Bob"]),
        Folder("Backend", ["Services"], [], []),                # No direct access
        
        # Layer 2 - Top-level folders under team
        Folder("Marketing", ["Campaigns"], [], []),             # No direct access
        Folder("Development", ["Frontend", "Backend"], ["readme.txt"], ["Alice"]),  
        Folder("Operations", [], ["show.txt"], ["Bob"])       # Folder with direct file
    ]
    
    # =================== TEAMS (Root Layer) ===================
    team = [
        Team("CompanyRoot", ["Marketing", "Development", "Operations"], [], [])
    ]
    
    # Test the hierarchy
    manager = HierarchyManager()
    manager.init_function(team, folders, files)
    
    print("\n" + "="*60)
    print("TESTING get_fewest with Alice:")
    print("="*60)
    result = manager.get_fewest("Alice")
    results = manager.get_fewest("Bob")
    for node in result:
        print(f"- {node.uuid}, whole node: {result}") 
    # for node in results:
    #     print(f"- {node.uuid}, whole node: {results}") 

if __name__ == "__main__":
    test_complex_hierarchy()