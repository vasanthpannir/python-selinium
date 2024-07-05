class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total Employees: {cls.count}")

# Example usage
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)
Employee.display_count()  # Output: Total Employees: 2