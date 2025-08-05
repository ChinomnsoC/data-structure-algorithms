# Implement a class to manage a system of layers, where:

# - Each layer has an ID (like 1, 2, 3)
# - Each layer contains properties stored as key-value pairs
# - Example of a layer: **`Layer(1, {"color": "green"})`**

# ## **Part 1: Basic Operations**

# Implement a class with the following operations:

# - **`init()`**
# - **`apply(layer)`**
# - **`undo()`**

# ### **Example Flow:**

# ```python
# # Operation 1
# apply(Layer(1, {"color": "green"}))

# # Operation 2
# apply(Layer(2, {"shape": "triangle", "color": "blue"}))

# # Operation 3
# apply(Layer(1, {"color": "pink"}))

# # After these operations, system state is:
# # Layer 1: {"color": "pink"}
# # Layer 2: {"shape": "triangle", "color": "blue"}

# # After one undo(), system state becomes:
# # Layer 1: {"color": "green"}
# # Layer 2: {"shape": "triangle", "color": "blue"}

# # After another undo(), system state becomes:
# # Layer 1: {"color": "green"}

# ```

# ## **Part 2: Batch Operations**

# Add support for batch operations with these additional features:

# - **`commit_batch()`**: Groups preceding operations into a single batch
# - Undo should work at batch level

# ### **Example Flow with Batches:**

# ```python
# # Batch 1
# apply(Layer(1, {"color": "green"}))
# apply(Layer(2, {"shape": "triangle", "color": "blue"}))
# apply(Layer(1, {"color": "pink"}))
# commit_batch()

# # Batch 2
# apply(Layer(1, {"color": "blue"}))
# apply(Layer(1, {"color": "white"}))
# commit_batch()

# # Final state after both batches:
# # Layer 1: {"color": "white"}
# # Layer 2: {"shape": "triangle", "color": "blue"}

# # After one undo() (reverting Batch 2):
# # Layer 1: {"color": "pink"}
# # Layer 2: {"shape": "triangle", "color": "blue"}

# ```

# ## **Part 3: Redo Functionality**

# Add redo capability:

# - New method: **`redo()`**
# - Restores previously undone operations
import copy

class Layer:
    def __init__(self, id, properties):
        self.layer_id = id
        self.properties = properties

class LayerSystem:
    def __init__(self):
        self.layer_nodes = {}
        self.undo_stack = []
        self.pending_operations = []
        self.batch_start_state = None
        self.redo_stack = []
    
    def apply(self, layer: Layer):
        layer_id = layer.layer_id
        new_layer_properties = layer.properties
        
        if not self.pending_operations:
            self.batch_start_state = copy.deepcopy(self.layer_nodes)
        
        if layer_id in self.layer_nodes:
            old_layer_properties = self.layer_nodes[layer_id]
            operation = (layer_id, old_layer_properties, "apply")
            
        else:
            operation = (layer_id, None, "apply")
        
        self.undo_stack.append(operation)
        self.pending_operations.append(operation)
        
        self.layer_nodes[layer_id] = new_layer_properties
        self.redo_stack.append((layer_id, new_layer_properties, "apply"))
        
        return self.layer_nodes
    
    
    def commit_batch(self):
        if not self.pending_operations:
            print("No batch to commit")
            return
        
        num_operations = len(self.pending_operations)
        for _ in range(num_operations):
            self.undo_stack.pop()
            self.redo_stack.pop()
        
        # Add single batch entry using the saved start state
        batch_entry = ("batch", self.batch_start_state, "batch")
        self.undo_stack.append(batch_entry)
        self.redo_stack.append(batch_entry)
        
        # Clear pending operations and reset batch start state
        self.pending_operations = []
        self.batch_start_state = None
        
        print(f"Committed batch with {num_operations} operations, new state: {self.layer_nodes}")
        print("apply result", self.layer_nodes)
        
    def undo(self):
        if not self.undo_stack:
            print("nothing to undo")
            return
        
        last_operation = self.undo_stack.pop()
        
        if last_operation[2] == "batch":
            action, last_saved_state, action = last_operation
            self.layer_nodes = copy.deepcopy(last_saved_state)
            print("Undid the last batch operation")
        
        if last_operation[2] == "apply":
            layer_id, old_layer_properties, action = last_operation
            if old_layer_properties is None:
                del self.layer_nodes[layer_id]
            else:
                self.layer_nodes[layer_id] = old_layer_properties
            
            if last_operation in self.pending_operations:
                    self.pending_operations.remove(last_operation)
        
            print(f"Undid operation on layer {layer_id}")
        print("undo stack", self.undo_stack)
        
    def redo(self):
        if not self.redo_stack:
            print("nothing to redo")
            return
        
        most_recent_operation = self.redo_stack.pop()
        

        if most_recent_operation[2] == "batch":
            action, last_saved_state, action = most_recent_operation
            self.layer_nodes = copy.deepcopy(last_saved_state)
            print("Undid the last batch operation")
        
        elif most_recent_operation[2] == "apply":
            layer_id, old_layer_properties, action = most_recent_operation
            self.layer_nodes[layer_id] = old_layer_properties
            
            if most_recent_operation in self.pending_operations:
                self.pending_operations.remove(most_recent_operation)
        
        return self.layer_nodes
        



layer = Layer(1, {"color": "green"})
layers = Layer(2, {"color": "yellow"})
layersa = Layer(3, {"color": "purple"})
layering = Layer(2, {"color": "pink"})
layersaa = Layer(3, {"color": "grey"})
lay_sys = LayerSystem()
lay_sys.apply(layer)
lay_sys.apply(layers)
lay_sys.commit_batch()
lay_sys.apply(layersa)
lay_sys.apply(layering)
lay_sys.commit_batch()
lay_sys.apply(layersaa)
lay_sys.undo()
print(lay_sys.redo())
        
        
        
        