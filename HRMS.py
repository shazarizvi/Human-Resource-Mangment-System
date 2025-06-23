import mysql.connector

# Establishing the connection with mysql_native_password as the auth plugin
db = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="12345",  
    database="HumanResourceManagmentSystem",  # for database made previously
    auth_plugin="mysql_native_password"
)

# Creating a cursor object
cursor = db.cursor()

# Creating the employee table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee (
        Employee_ID VARCHAR(5) PRIMARY KEY,
        First_Name VARCHAR(50),
        Last_Name VARCHAR(50),
        Department VARCHAR(50),
        Position VARCHAR(50),
        Salary INT,
        Date_of_Hire DATE,
        Email VARCHAR(100),
        Phone_Number VARCHAR(20),
        Address VARCHAR(100),
        Status VARCHAR(20)
    )
""")

employees = [
    ("E001", "John", "Doe", "IT", "Software Engineer", 75000, "2021-03-15", "john.doe@example.com", "555-1234", "123 Elm St", "Active"),
    ("E002", "Jane", "Smith", "HR", "HR Manager", 82000, "2019-07-22", "jane.smith@example.com", "555-5678", "456 Oak St", "Active"),
    ("E003", "Bob", "Johnson", "Finance", "Accountant", 60000, "2020-01-12", "bob.johnson@example.com", "555-8765", "789 Pine St", "Active"),
    ("E004", "Alice", "Williams", "Marketing", "Marketing Specialist", 65000, "2022-09-10", "alice.williams@example.com", "555-2345", "321 Maple St", "Active"),
    ("E005", "Charlie", "Brown", "IT", "System Administrator", 70000, "2018-05-30", "charlie.brown@example.com", "555-4321", "654 Cedar St", "Active"),
    ("E006", "Eva", "Green", "Sales", "Sales Representative", 55000, "2020-12-03", "eva.green@example.com", "555-3456", "987 Birch St", "Active"),
    ("E007", "Frank", "Harris", "IT", "Data Analyst", 72000, "2021-10-08", "frank.harris@example.com", "555-6789", "147 Spruce St", "On Leave"),
    ("E008", "Grace", "Lee", "HR", "Recruiter", 58000, "2020-07-25", "grace.lee@example.com", "555-9876", "258 Fir St", "Active"),
    ("E009", "Henry", "Adams", "Finance", "Financial Analyst", 69000, "2019-11-13", "henry.adams@example.com", "555-4567", "369 Walnut St", "Resigned"),
    ("E010", "Ivy", "Miller", "Marketing", "Social Media Manager", 67000, "2021-02-19", "ivy.miller@example.com", "555-7654", "741 Willow St", "Active"),
    ("E011", "Jack", "White", "Sales", "Sales Manager", 80000, "2022-04-22", "jack.white@example.com", "555-1122", "852 Poplar St", "Active"),
    ("E012", "Kayla", "Davis", "IT", "Network Engineer", 74000, "2019-03-08", "kayla.davis@example.com", "555-3344", "963 Ash St", "Active"),
    ("E013", "Liam", "Baker", "HR", "HR Assistant", 52000, "2020-09-15", "liam.baker@example.com", "555-5566", "174 Cypress St", "Active"),
    ("E014", "Mia", "Clark", "Finance", "Accountant", 60000, "2018-12-29", "mia.clark@example.com", "555-7788", "285 Redwood St", "On Leave"),
    ("E015", "Noah", "Evans", "Marketing", "Content Writer", 53000, "2021-06-18", "noah.evans@example.com", "555-9900", "396 Sequoia St", "Active"),
    ("E016", "Olivia", "Hughes", "Sales", "Sales Representative", 55000, "2019-10-05", "olivia.hughes@example.com", "555-1133", "507 Magnolia St", "Active"),
    ("E017", "Paul", "Scott", "IT", "Software Engineer", 76000, "2022-02-27", "paul.scott@example.com", "555-2244", "618 Palm St", "Active"),
    ("E018", "Quinn", "Morris", "HR", "HR Specialist", 61000, "2020-04-09", "quinn.morris@example.com", "555-3355", "729 Sycamore St", "Active"),
    ("E019", "Rachel", "Walker", "Finance", "Chief Financial Officer", 120000, "2018-07-16", "rachel.walker@example.com", "555-4466", "840 Dogwood St", "Active"),
    ("E020", "Sam", "Young", "Marketing", "Brand Manager", 68000, "2021-11-05", "sam.young@example.com", "555-5577", "951 Hickory St", "Active")
]


cursor.executemany("""
    INSERT INTO employee (Employee_ID, First_Name, Last_Name, Department, Position, Salary, Date_of_Hire, Email, Phone_Number, Address, Status)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""", employees)
db.commit()

# Menu-based program functions

from tabulate import tabulate
import csv

# Establishing the connection with mysql_native_password as the auth plugin
import getpass

db = mysql.connector.connect(
    host="localhost",
    user=input("Enter MySQL username: "),
    password=getpass.getpass("Enter MySQL password: "),
    database="HumanResourceManagmentSystem",
    auth_plugin="mysql_native_password"
)


# Creating a cursor object
cursor = db.cursor()

# Function to create employee table if not already exists
def create_employee_table():
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS employee (
            Employee_ID VARCHAR(5) PRIMARY KEY,
            First_Name VARCHAR(50),
            Last_Name VARCHAR(50),
            Department VARCHAR(50),
            Position VARCHAR(50),
            Salary INT,
            Date_of_Hire DATE,
            Email VARCHAR(100),
            Phone_Number VARCHAR(20),
            Address VARCHAR(100),
            Status VARCHAR(20)
        )
    """)

# Function to add an employee
def add_employee():
    emp_id = input("Enter Employee ID: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    department = input("Enter Department: ")
    position = input("Enter Position: ")
    salary = int(input("Enter Salary: "))
    date_of_hire = input("Enter Date of Hire (YYYY-MM-DD): ")
    email = input("Enter Email: ")
    phone_number = input("Enter Phone Number: ")
    address = input("Enter Address: ")
    status = input("Enter Status (Active/On Leave/Resigned): ")
    
    cursor.execute("""
        INSERT INTO employee (Employee_ID, First_Name, Last_Name, Department, Position, Salary, Date_of_Hire, Email, Phone_Number, Address, Status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (emp_id, first_name, last_name, department, position, salary, date_of_hire, email, phone_number, address, status))
    db.commit()
    print("Employee added successfully!")

# Function to delete an employee
def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    cursor.execute("DELETE FROM employee WHERE Employee_ID = %s", (emp_id,))
    db.commit()
    print("Employee deleted successfully!")

# Function to update employee status
def update_status():
    emp_id = input("Enter Employee ID to update status: ")
    new_status = input("Enter new status (Active/On Leave/Resigned): ")
    cursor.execute("UPDATE employee SET Status = %s WHERE Employee_ID = %s", (new_status, emp_id))
    db.commit()
    print("Employee status updated successfully!")

# Function to search employees by various criteria
def search_employee():
    search_by = input("Search by (ID/Name/Department/Position): ").lower()
    if search_by == "id":
        emp_id = input("Enter Employee ID to search: ")
        cursor.execute("SELECT * FROM employee WHERE Employee_ID = %s", (emp_id,))
    elif search_by == "name":
        name = input("Enter Employee Name to search: ")
        cursor.execute("SELECT * FROM employee WHERE First_Name LIKE %s OR Last_Name LIKE %s", ('%' + name + '%', '%' + name + '%'))
    elif search_by == "department":
        department = input("Enter Department to search: ")
        cursor.execute("SELECT * FROM employee WHERE Department = %s", (department,))
    elif search_by == "position":
        position = input("Enter Position to search: ")
        cursor.execute("SELECT * FROM employee WHERE Position = %s", (position,))
    else:
        print("Invalid search criteria!")
        return

    employees = cursor.fetchall()
    if employees:
        print(tabulate(employees, headers=["Employee_ID", "First_Name", "Last_Name", "Department", "Position", "Salary", "Date_of_Hire", "Email", "Phone_Number", "Address", "Status"], tablefmt="pretty"))
    else:
        print("No employees found.")

# Function to calculate total salary expense
def calculate_salary_expense():
    department = input("Enter Department to calculate total salary (or press Enter for all): ")
    if department:
        cursor.execute("SELECT SUM(Salary) FROM employee WHERE Department = %s AND Status = 'Active'", (department,))
    else:
        cursor.execute("SELECT SUM(Salary) FROM employee WHERE Status = 'Active'")
    total_salary = cursor.fetchone()[0]
    print("Total salary expense: " + str(total_salary) if total_salary else "No active employees found.")

# Function to sort employees by criteria
def sort_employees():
    sort_by = input("Sort by (Name/Salary/Date): ").lower()
    if sort_by == "name":
        cursor.execute("SELECT * FROM employee ORDER BY First_Name, Last_Name")
    elif sort_by == "salary":
        cursor.execute("SELECT * FROM employee ORDER BY Salary DESC")
    elif sort_by == "date":
        cursor.execute("SELECT * FROM employee ORDER BY Date_of_Hire")
    else:
        print("Invalid sorting criteria!")
        return

    employees = cursor.fetchall()
    print(tabulate(employees, headers=["Employee_ID", "First_Name", "Last_Name", "Department", "Position", "Salary", "Date_of_Hire", "Email", "Phone_Number", "Address", "Status"], tablefmt="pretty"))

# Function to generate employee report
def generate_report():
    cursor.execute("SELECT Department, COUNT(*), SUM(Salary) FROM employee WHERE Status = 'Active' GROUP BY Department")
    report = cursor.fetchall()
    print("Employee Report by Department:")
    print(tabulate(report, headers=["Department", "Number of Employees", "Total Salary"], tablefmt="pretty"))

# Function to backup data to CSV
def backup_to_csv():
    cursor.execute("SELECT * FROM employee")
    employees = cursor.fetchall()
    with open('employee_backup.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Employee_ID", "First_Name", "Last_Name", "Department", "Position", "Salary", "Date_of_Hire", "Email", "Phone_Number", "Address", "Status"])
        writer.writerows(employees)
    print("Backup successful. Data saved to 'employee_backup.csv'.")

# Menu-based program
def menu():
    while True:
        print("\nShaza Rizvi's Human Resource Management System Menu:")
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. Update Employee Status")
        print("4. Search Employee")
        print("5. Calculate Total Salary Expense")
        print("6. Sort Employees")
        print("7. Generate Employee Report")
        print("8. Backup Employee Data to CSV")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            delete_employee()
        elif choice == '3':
            update_status()
        elif choice == '4':
            search_employee()
        elif choice == '5':
            calculate_salary_expense()
        elif choice == '6':
            sort_employees()
        elif choice == '7':
            generate_report()
        elif choice == '8':
            backup_to_csv()
        elif choice == '9':
            confirm = input("Are you sure you want to exit? (y/n): ")
            if confirm.lower() == 'y':
                print("Exiting the program...")
                cursor.close()
                db.close()
                exit()
            else:
                print("Returning to menu...")
        else:
            print("Invalid choice! Please try again.")



# Starting the program
menu()


cursor.close()
db.close()


