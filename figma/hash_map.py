# 🔴 Question 3 (Hierarchical Data): Parent Lookup
# You are given a list of employees and their managers. Build a hash map to quickly look up the manager of any given employee.

# Input:

# python
# Copy
# Edit
relationships = [
    ("Alice", "Bob"),     # Alice reports to Bob
    ("Bob", "Catherine"), # Bob reports to Catherine
    ("David", "Bob")
]
# Your Task:
# Build a employee_to_manager dictionary.
# Write a function: get_manager(employee: str) -> str
# Write a function: get_top_manager(employee: str) that recursively finds the highest-level manager (like the CEO).


class RelationshipManager:
    def __init__(self, relationships):
        self.employee_to_manager = {}
    
        for employee, manager in relationships:
            self.employee_to_manager[employee] = manager
            
    def get_manager(self, employee,):
        return self.employee_to_manager.get(employee)
    
    def get_top_manager(self, employee):
        # another solution
        # while self.get_manager(employee):
        #     employee = self.get_manager(employee)
            
        # return employee
        manager = self.get_manager(employee)
        if not manager:
            return employee
        
        return self.get_top_manager(employee)
            
            
        
        