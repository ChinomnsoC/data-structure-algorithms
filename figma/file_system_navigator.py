# Given this JSON representing a file system, build a navigator:
json_data = {
  "root": {
    "type": "folder",
    "children": {
      "documents": {
        "type": "folder", 
        "children": {
          "resume.pdf": {"type": "file", "size": 1024},
          "cover_letter.doc": {"type": "file", "size": 512}
        }
      },
      "photos": {
        "type": "folder",
        "children": {
          "vacation.jpg": {"type": "file", "size": 2048}
        }
      },
      "readme.txt": {"type": "file", "size": 256}
    }
  }
}

# Build a FileSystemNavigator class with:
# - load_from_json(json_data) - build internal tree structure
# - find_file(filename) - return full path to file (e.g., "/root/documents/resume.pdf")
# - get_folder_size(folder_path) - return total size of all files in folder
# - add_file(folder_path, filename, size) - add new file to existing folder

# Use hashmaps for fast lookups and tree structure for hierarchy.

class FileSystemNode:
    def __init__(self, name, node_type, children, size):
        self.name = name
        self.type = node_type
        self.children = children
        self.size = size
        
        
class FileSystemNavigator:
    def __init__(self, json_data):
        self.file_system_nodes = {}
        self.parent_map = {}
        
        self._parse_json_object(json_data, parent_name=None)
        
        
    def _parse_json_object(self, json_object, parent_name):
        
        for node_name, node_data in json_object.items():
            node = FileSystemNode(
                name=node_name,
                node_type=node_data["type"],
                children=node_data.get("children", {}),
                size=node_data.get("size", 0)
            )
            
            self.file_system_nodes[node_name] = node
        
        if parent_name:
            self.parent_map[node_name] = parent_name
            
        if "children" in node_data:
            self._parse_json_object(node_data["children"], parent_name=node_name)
    
    
    # find_file(filename) - return full path to file (e.g., "/root/documents/resume.pdf")       
    def find_file(self, filename):
        # My idea is that first we check that file name exists in self.file system nodes. 
        # If it does, we recursively find its parents and grandparents until we get to the root, 
        # then we do some string manipulation merge the names of all the ancestors separated by a "/". 
        
        if filename not in self.file_system_nodes:
            return None
        
        node = self.file_system_nodes[filename]
        if node.node_type != "file":
            print(f"{filename} is note a file")
            return None
        
        parts_of_path = []
        current_name = filename
        
        while current_name:
            parts_of_path.append(current_name)
            current_name = self.parent_map.get(current_name) 
        
        parts_of_path.reverse()
        
        return "/"+"/".join(parts_of_path)
    
    # - get_folder_size(folder_path) - return total size of all files in folder
    def get_folder_size(self, folder_path):
        folder_name = folder_path.split("/")[-1]
        
        # Of course, I'll first check if the folder exists in the node, 
        # and if it has children at all, and if there are already sizes at that level. What do you think?
        
        if folder_name not in self.file_system_nodes:
            print(f"{folder_name} doesn't exist in the file system node")
            return 0
        
        total_size = self._internal_folder_size(folder_name)
        
        return total_size
    
    def _internal_folder_size(self, folder_name):
        node = self.file_system_nodes[folder_name]
        
        if node.type != "folder":
            return 0
        
        total_size = 0
        
        for child_name, child_data in node.children.items():
            if child_data["type"] == "file":
                total_size += child_data["size"]
            
            else:
                total_size += self._internal_folder_size(child_name)
        
        return total_size
    
    # add_file(folder_path, filename, size) - add new file to existing folder
    
    def add_file(folder_path, filename, size):
        