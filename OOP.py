class Employee:
    # constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSallery(self):
        return {
            self.name,
            self.salary
        }


newEmployee =  Employee("XYZ", 40000)
print(newEmployee.getSallery())