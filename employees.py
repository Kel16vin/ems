employees = []

def menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. View Demo Page")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            demo_employees()
        elif choice == '6':
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
    
    # Display formatted employee page
    print("\n" + "="*80)
    print(" "*25 + "EMPLOYEE DIRECTORY")
    print("="*80)
    print(f"{'ID':<6} | {'Name':<20} | {'Role':<20} | {'Salary':<12}")
    print("-"*80)
    
    for emp in employees:
        print(f"{emp['id']:<6} | {emp['name']:<20} | {emp['role']:<20} | ${emp['salary']:<11}")
    
    print("="*80)
    print(f"Total Employees: {len(employees)}")
    print("="*80)

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

def demo_employees():
    demo_data = [
        {"id": "001", "name": "John Smith", "role": "Software Engineer", "salary": "95000"},
        {"id": "002", "name": "Sarah Johnson", "role": "Product Manager", "salary": "110000"},
        {"id": "003", "name": "Michael Chen", "role": "UX Designer", "salary": "85000"},
        {"id": "004", "name": "Emily Davis", "role": "Marketing Manager", "salary": "88000"},
        {"id": "005", "name": "Robert Wilson", "role": "DevOps Engineer", "salary": "105000"},
    ]
    
    # Display the demo employee page
    print("\n" + "="*80)
    print(" "*25 + "EMPLOYEE DIRECTORY")
    print("="*80)
    print(f"{'ID':<6} | {'Name':<20} | {'Role':<20} | {'Salary':<12}")
    print("-"*80)
    
    for emp in demo_data:
        print(f"{emp['id']:<6} | {emp['name']:<20} | {emp['role']:<20} | ${emp['salary']:<11}")
    
    print("="*80)
    print(f"Total Employees: {len(demo_data)}")
    print("="*80)

if __name__ == "__main__":
    menu()