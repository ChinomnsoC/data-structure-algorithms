# Build a simple text editor that supports:
# - insert_char(position, char) 
# - delete_char(position)
# - undo()
# - redo()

# Your editor stores text as a list of characters: ['H', 'e', 'l', 'l', 'o']

# Requirements:
# - Use stacks for undo/redo with command pattern
# - Each operation should store enough info to reverse itself
# - Support inserting/deleting at any position
# - Print the current text after each operation



#  h, insert at 0
#  i, insert at 1
# h, deleted from 0

delete_action = "was deleted from"
insert_action = "was inserted at"

class TextEditor:
    def __init__(self):
        self.text_list = []
        self.undo_stack = []
        self.redo_stack = []
        
    def insert_char(self, position, char):
        if not self.text_list:
            self.text_list = []
            if position != 0:
                print(f"you need to insert {char} at 0 because this should be the first character in the list")
                return
            self.text_list.append(char)
            print("insert", self.text_list)
        else:
            self.text_list.insert(position, char)
            self.undo_stack.append((char, insert_action, position))
            print("insert", self.text_list)
    
    def _internal_insert_char(self, position, char):
        if not self.text_list:
            self.text_list = []
            if position != 0:
                print(f"you need to insert {char} at 0 because this should be the first character in the list")
                return
            self.text_list.append(char)
            self.undo_stack.append((char, insert_action, position))  # ADD THIS LINE
            self.redo_stack.clear() 
            print("insert", self.text_list)
        else:
            self.text_list.insert(position, char)
            self.undo_stack.append((char, insert_action, position))  # ADD THIS LINE
            self.redo_stack.clear() 
    
    def delete_char(self, position):
        if not self.text_list:
            print("The list is empty, there's nothing to delete")
            return
        if position >= len(self.text_list):
            print(f"The list is not as long as having {position} characters")
            return
        
        char = self.text_list[position]
        del self.text_list[position]
        self.undo_stack.append((char, delete_action, position))
        print("delete", self.text_list)
    
    def _internal_delete_char(self, position):
        if not self.text_list:
            print("The list is empty, there's nothing to delete")
            return
        if position >= len(self.text_list):
            print(f"The list is not as long as having {position} characters")
            return
        
        char = self.text_list[position]
        del self.text_list[position]
    
    def undo(self):
        if not self.undo_stack:
            print("nothing to undo")
            return
        
        char, action, position = self.undo_stack.pop()
        self.redo_stack.append((char, action, position))
        
        if action == delete_action:
            self._internal_insert_char(position, char)
        if action == insert_action:
            self._internal_delete_char(position)
    
    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo")
            return
        char, action, position = self.redo_stack.pop()
        self.undo_stack.append((char, action, position))
        
        if action == delete_action:
            self._internal_delete_char(position)
        if action == insert_action:
            self._internal_insert_char(position, char)
        

# Example usage:
editor = TextEditor()
editor.insert_char(0, 'o')  # ['H']
editor.insert_char(1, 'i')  # ['H', 'i'] 
editor.insert_char(2, 'K')
editor.insert_char(3, 'u')
editor.delete_char(0)       # ['i']
editor.undo()              # ['H', 'i']
editor.insert_char(4, 'u')
editor.undo()              # ['H']
editor.insert_char(3, 'x')
editor.undo()
editor.redo()
editor.insert_char(6, 'x')

