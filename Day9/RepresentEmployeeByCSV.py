import csv 


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    
    def __str__(self) -> str:
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}"
    

def create_employee_from_csv(file_path):
    employees = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            name, position, salaey = row
            employee = Employee(name, position, salaey)
            employees.append(employee)

    return employees



file_path = "employee.csv"
employees = create_employee_from_csv(file_path)
for employee in employees:
    print(employee)
        

