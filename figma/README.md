# Questions

## Topmost Accessible Node

Context: We have a hierarchical file system where design files and folders are organized in a tree structure (similar to how files/folders are organized in Figma). Each file/folder has specific user access permissions. We need to build a system to efficiently determine what content is accessible to users.

Problem Statement: Given a file system tree where each node (file/folder) has:

- A unique ID
- Parent ID (null for root)
- Type (file or folder)
- Access permissions (list of user IDs who can access this item)
- Name

Write a function that finds all the "topmost" accessible files/folders for a given user. "Topmost" means if a user has access to both a parent and child, only return the parent.

Example:

```
const fileSystem = {
  nodes: [
    {
      id: "1",
      parentId: null,
      type: "folder",
      name: "root",
      accessibleBy: ["user1"]
    },
    {
      id: "2",
      parentId: "1",
      type: "folder",
      name: "folder1",
      accessibleBy: ["user1", "user2"]
    },
    {
      id: "3",
      parentId: "2",
      type: "file",
      name: "file1",
      accessibleBy: ["user2"]
    }
  ]
};
```

// For user2, should return only node "2" (folder1)
// Even though user2 has access to file1, it's under folder1 which they can access
Follow-up: If we move a file/folder to a different location in the tree, how would this affect the "topmost accessible files" results?

Another variant
You are given three data structures: Team, Folder, and Files. Each file and folder has an attribute that contains a list of user IDs, representing the users who have access to that team, folder, or file.

If a user has access to a higher-level team, folder, or file, they also have access to all its sub-files and sub-folders.

You need to implement two APIs: init and get_fewest(), which determine the minimum number of teams, files, or folders required to grant the user access to everything they are authorized to access.

```
              Team1     
             /       \
    Folder1(A)      Folder2
        /      \            |
 file1(A)   file2    Folder3(A)
```
here should return Folder1 and Folder3

```
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

def init_function(teams, folders​, files):
  pass

def get_fewest(user_id):
  pass

init_function(
  [Team("Team1", ["Folder1", "Folder2"], [], ["userA"])],
  [Folder("Folder1", [], ["File1", "File2"], ["userA"]), Folder("Folder2", ["Folder3"], [], []), Folder("Folder3", [], [], ["userA"])],
  [File("File1", ["userA"]), File("File2", [])]
)
```
Don't see what you're looking for? Let us know on Discord!
