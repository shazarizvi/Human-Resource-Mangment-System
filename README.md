# Human Resource Management System (HRMS)

A comprehensive command-line Human Resource Management System built with Python and MySQL for managing employee data efficiently.

## ✨ Features

- **Employee Management**: Add, delete, and update employee records
- **Advanced Search**: Search employees by ID, name, department, or position
- **Status Management**: Update employee status (Active, On Leave, Resigned)
- **Salary Analytics**: Calculate total salary expenses by department or company-wide
- **Data Sorting**: Sort employees by name, salary, or hire date
- **Reporting**: Generate comprehensive employee reports by department
- **Data Backup**: Export employee data to CSV format
- **User-Friendly Interface**: Interactive menu-driven console application

## 🔧 Prerequisites

Before running this application, ensure you have the following installed:

- **Python 3.6+**
- **MySQL Server**
- **Required Python packages**:
  - `mysql-connector-python`
  - `tabulate`

## 🚀 Installation

1. **Clone or download the project**
2. **Install required packages**:
   ```bash
   pip install mysql-connector-python tabulate
   ```
3. **Start MySQL server** and log in as root
4. **Create the database**:
   ```sql
   CREATE DATABASE HumanResourceManagmentSystem;
   ```
5. **Update the credentials** in the script to match your MySQL setup
6. **Run the program**:
   ```bash
   python hrms.py
   ```

## 🗄️ Database Setup

1. **Start MySQL server** and log in as root user
2. **Create the database**:
   ```sql
   CREATE DATABASE HumanResourceManagmentSystem;
   ```
3. **Update database connection settings** in the script:
   ```python
   db = mysql.connector.connect(
       host="localhost",
       user="root",  # Replace with your MySQL username
       password="12345",  # Replace with your MySQL password
       database="HumanResourceManagmentSystem",
       auth_plugin="mysql_native_password"
   )
   ```
4. **Run the application** - it will automatically create the required table and populate sample data

## 💻 Usage

1. **Run the application**:
   ```bash
   python hrms.py
   ```
2. **Navigate through the menu** using the numbered options
3. **Follow the prompts** for each operation

## 📖 Menu Options

| Option | Function | Description |
|--------|----------|-------------|
| 1 | Add Employee | Add a new employee to the system |
| 2 | Delete Employee | Remove an employee by ID |
| 3 | Update Employee Status | Change employee status (Active/On Leave/Resigned) |
| 4 | Search Employee | Search by ID, name, department, or position |
| 5 | Calculate Total Salary Expense | View salary expenses by department or company-wide |
| 6 | Sort Employees | Sort by name, salary, or hire date |
| 7 | Generate Employee Report | View department-wise employee statistics |
| 8 | Backup Employee Data to CSV | Export all data to CSV file |
| 9 | Exit | Close the application |

## 🏗️ Database Schema

The employee table contains the following fields:

| Field | Type | Description |
|-------|------|-------------|
| Employee_ID | VARCHAR(5) | Primary Key - Unique employee identifier |
| First_Name | VARCHAR(50) | Employee's first name |
| Last_Name | VARCHAR(50) | Employee's last name |
| Department | VARCHAR(50) | Department (IT, HR, Finance, Marketing, Sales) |
| Position | VARCHAR(50) | Job position/title |
| Salary | INT | Annual salary |
| Date_of_Hire | DATE | Employee hire date (YYYY-MM-DD) |
| Email | VARCHAR(100) | Employee email address |
| Phone_Number | VARCHAR(20) | Contact phone number |
| Address | VARCHAR(100) | Employee address |
| Status | VARCHAR(20) | Employment status (Active/On Leave/Resigned) |

## ⚠️ Important Notes

- Ensure MySQL server is running before starting the application
- Update database credentials in the code before first run
- The application will create the database table automatically on first run
- CSV backup files are saved in the same directory as the script

## 🐛 Troubleshooting

**Common Issues**:

1. **MySQL Connection Error**: Verify MySQL server is running and credentials are correct
2. **Module Not Found**: Install required packages using `pip install mysql-connector-python tabulate`
3. **Permission Denied**: Ensure proper database user permissions

## 📌 Project Status

This project was originally created as my **Class 12 Computer Science final project**.
That said — it's now archived and will **no longer be actively maintained or updated**.
I'm keeping it here as a record of where I started.

## 👩‍💻 Author

**Created by Shaza Rizvi**
- GitHub: [shazarizvi](https://github.com/shazarizvi)
- Email: rizvishaza@gmail.com
