class Employee:
    def get_input(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.salary = float(input("Enter Salary: "))
        self.address = input("Enter Address: ")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


class Manager(Employee):
    pass

managers = []
for i in range(10):
    print("\nEnter details of Manager", i+1)
    m = Manager()
    m.get_input()
    managers.append(m)

print("\nManager Details:")
for i, m in enumerate(managers, start=1):
    print("\nManager", i)
    m.display()