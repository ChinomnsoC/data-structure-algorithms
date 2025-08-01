# 🟡 Question 2: Company Departments (from list)
# You are given a list of tuples representing employees and their departments:

employees = [
    ("Alice", "HR"),
    ("Bob", "Engineering"),
    ("Charlie", "Engineering"),
    ("Diana", "HR"),
    ("Eve", "Finance")
]
# Your tasks:
# Build a hash map of department → list of employees.

# {
#     "HR": ["Alice", "Diana"],
#     "Engineering": ["Bob", "Charlie"],
#     "Finance": ["Eve"]
# }
# Write a function get_employees(department) to return all employees in that department.

# Write a function transfer_employee(employee_name, new_department) that moves an employee to a new department (update both lists and the mapping).

# ✅ Both of these force you to:
# Use lists to hold children/employees
# Use hash maps (dict) for fast lookups
# Think in tree terms (hierarchy in Q1) and grouping terms (Q2)

class CompanyDepartments:
    def __init__(self, employees):
        self.department_to_employee = {}
        self.employee_to_department = {}
        
        for employee, dept in employees:
            if dept not in self.department_to_employee:
                self.department_to_employee[dept] = []
            self.department_to_employee[dept].append(employee)
            
            self.employee_to_department[employee] = dept
        
        print(self.department_to_employee)
    
    def get_employees(self, department):
        return self.department_to_employee.get(department, [])
    
    def get_employee_department(self, employee):
        for dept, employees in self.department_to_employee.items():
            if employee in employees:
                return dept
        return None
        
    def transfer_employee(self, employee_name, new_department):
        
        employee_department = self.get_employee_department(employee_name)
        
        # find employee in department
        if employee_department:
            # print("self.department_to_employee[dept]", self.department_to_employee[dept])
            # delete employee from department
            self.department_to_employee[employee_department].remove(employee_name)
            print("self.department_to_employee[dept]", self.department_to_employee[employee_department])
        
        # write employee to new department
        if new_department not in self.department_to_employee.keys():
            self.department_to_employee[new_department] = []
        self.department_to_employee[new_department].append(employee_name)
            
        # update map
        self.employee_to_department[employee_name] = new_department
        
        
        return self.department_to_employee
        

emp = CompanyDepartments(employees)
# print(emp.get_employees("HR"))
print(emp.transfer_employee("Diana", "Engineering"))
# print("get_employee_department", emp.get_employee_department("Diana"))
        

