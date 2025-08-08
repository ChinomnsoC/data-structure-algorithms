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


# start from the root, and check if user has access, if it doesn't check its child.
# return the first occurring node(s) from the root of the tree which the user has access to.
# init_function and get_fewest()


# build the tree, node_object is mapped to its id, and we establish parent child relationship.
class HierarchyManager:
    def __init__(self):
        self.id_to_node = {}
        self.parent_map = {}
        
    def has_access(self, user_id, node):
        print("user_id", user_id)
        # print("node here", node.uuid)
        return user_id in node.user_ids
    

    def init_function(self, teams, folders, files):

        # map file node object to its file id
        for file in files:
            self.id_to_node[file.uuid] = file

        # map folder node object to its folder id
        for folder in folders:
            self.id_to_node[folder.uuid] = folder
            # map the folder as parent to its child folder
            for sub_folder_id in folder.folder_ids:
                self.parent_map[sub_folder_id] = folder.uuid
            # map the folder as parent to its child file
            for file_id in folder.file_ids:
                self.parent_map[file_id] = folder.uuid

        # map team node object to its team id
        for team in teams:
            self.id_to_node[team.uuid] = team
            # map the team as parent to its child folder
            for folder_id in team.folder_ids:
                self.parent_map[folder_id] = team.uuid
            # map the team as parent to its child file
            for file_id in team.file_ids:
                self.parent_map[file_id] = team.uuid

        print(list(self.id_to_node.keys()))
        for child_id, parent_id in self.parent_map.items():
            print(f"{child_id} is the child of {parent_id}")
    
    def get_fewest(self, user_id):
        
        minimum_access_nodes = []
        roots = []
        
        for node_id, node in self.id_to_node.items():
            if node_id not in self.parent_map:
                roots.append(node)
        
        for root in roots:
            print("roots", root.folder_ids)
            self._process_node(user_id, root, minimum_access_nodes)
        # for root in roots, if the user has access to the root, append to the list minimum_access_nodes.
        # if not, get the children of root and repeat the process.
        # repeat this process until we've found all the first occurrences in each branch.
        return minimum_access_nodes
    def _process_node(self, user_id, node, minimum_access_nodes):
        print("checking access", user_id)
        if self.has_access(user_id, node):
            minimum_access_nodes.append(node)
        else:
            children = self._get_children(node)
            for child in children:
                print("child", child)
                self._process_node(user_id, child, minimum_access_nodes)
    
    def _get_children(self, node):
        children = []
        for child_id, parent_id in self.parent_map.items():
            print("parent id", parent_id)
            if parent_id == node.uuid:
                children.append(self.id_to_node[child_id])
                print(f"the children of {parent_id} are {children}")
            
        return children
                


file = [
    File("file1", ["userB"]),
    File("file2", ["userB"]),
    File("file3", ["userC"]),
    File("file4", ["userC", "userA"]),
    File("file5", ["userA"]),
]
folders = [
    Folder("Engineering", [], ["file1", "file2"], ["userB"]),
    Folder("Design", ["Marketing"], ["file3", "file4"], ["userC"]),
    Folder("Marketing", [], ["file5"], ["userA"]),
]
team = [Team("Team1", ["Engineering", "Design"], [], [])]


manager = HierarchyManager()
output = manager.init_function(team, folders, file)
fewest = manager.get_fewest("userB")
for node in fewest:
    print("output", node.uuid)