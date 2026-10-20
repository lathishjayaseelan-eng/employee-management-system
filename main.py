employees = []

def add_employee():
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    department = input("Enter department: ")

    employee = {
        "name": name,
        "salary": salary,
        "department": department
    }

    employees.append(employee)
    print("Employee added successfully!")

def view_employees():
    for employee in employees:
        print(employee)

while True:
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
