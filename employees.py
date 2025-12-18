employees = []

def menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def add_employee():
    emp_id = input("Enter ID: ")
    name = input("Enter Name: ")
    role = input("Enter Role: ")
    salary = input("Enter Salary: ")
    
    employee = {
        "id": emp_id,
        "name": name,
        "role": role,
        "salary": salary
    }
    employees.append(employee)
    print(f"Employee {name} added successfully!")

def view_employees():
    if not employees:
        print("\nNo employees found.")
        return
    
    print("\nID | Name | Role | Salary")
    print("-" * 30)
    for emp in employees:
        print(f"{emp['id']} | {emp['name']} | {emp['role']} | ${emp['salary']}")

def update_employee():
    emp_id = input("Enter the ID of the employee to update: ")
    for emp in employees:
        if emp['id'] == emp_id:
            emp['name'] = input(f"Enter new name ({emp['name']}): ") or emp['name']
            emp['role'] = input(f"Enter new role ({emp['role']}): ") or emp['role']
            emp['salary'] = input(f"Enter new salary ({emp['salary']}): ") or emp['salary']
            print("Update complete!")
            return
    print("Employee ID not found.")

def delete_employee():
    emp_id = input("Enter the ID of the employee to delete: ")
    global employees
    employees = [emp for emp in employees if emp['id'] != emp_id]
    print("Employee removed if ID existed.")

if __name__ == "__main__":
    menu()