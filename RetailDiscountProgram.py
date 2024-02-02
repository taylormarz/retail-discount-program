import re
import sys

# List to store employee info
employee_data = []

# Menu Page
menuDesign = ("----------------------------------------\n" +
              "|   Main Menu:                         |\n" +
              "----------------------------------------\n" +
              "|   1 - Create a New Employee          |\n" +
              "|   2 - Create an Item                 |\n" +
              "|   3 - Make a Purchase                |\n" +
              "|   4 - All Employee Summary           |\n" +
              "|   5 - Exit                           |\n" +
              "----------------------------------------")
print(menuDesign)


# Create a New Employee Function
def create_employee():
    print("----------------------------------------\n"
          "|   You are creating a new employee.   |\n"
          "----------------------------------------")

    employee_information = []

    while True:
        try:
            employee_id = int(input("    Enter 4-Digit Employee ID: "))
            if len(str(employee_id)) == 4:
                break
            else:
                print("    Error! Employee ID must be 4-digit integer.")
        except ValueError:
            print("    Error! Employee ID must be 4-digit integer.")

    # employee_discount creation + validation
    while True:
        employee_name = (input("    Enter Employee First and Last Name: "))
        if re.match(r'^[a-zA-Z]+([\' -][a-zA-Z]+)*$', employee_name):
            break
        print("    Error! Employee name must be alphanumeric.")

    # employee_type creation + validation
    employee_type = (input("    Enter Employee Type (Hourly/Manager): "))
    while employee_type.lower() not in ["hourly", "manager"]:
        print("    Error! Employee Type must be Hourly or Manager.")
        employee_type = (input("    Enter Employee Type (Hourly/Manager): "))

    # years_worked creation + validation
    while True:
        try:
            years_worked = int(input("    Enter Number of Years Employee has Worked: "))
            break
        except ValueError:
            print("    Error! Employee Years must be an integer.")

    # employee_purchases creation + set to 0 to start
    employee_purchases = 0

    # total_discount creation + set to 0 to start
    total_discount = 0

    # employee_discount creation + validation
    while True:
        try:
            employee_discount = int(input("    Enter Employee Discount: "))
            break
        except ValueError:
            print("    Error! Employee Discount must be an Integer.")

    # Adding input for new employee to employee_information list
    employee_information.append([employee_id, employee_name, employee_type, years_worked,
                                 employee_purchases, total_discount, employee_discount])
    employee_data.append(employee_information)


# Menu Selection Function
def menu_options():
    while True:
        menu_selection = input("    Enter Menu Option Selection: ")
        if menu_selection == "1":
            create_employee()
        elif menu_selection == "2":
            print("----------------------------------------\n"
                  "|   Printing Employees in System.      |\n"
                  "----------------------------------------")
            print(employee_data)
        elif menu_selection == "5":
            print("----------------------------------------\n"
                  "|   You are exiting the program. Bye!  |\n"
                  "----------------------------------------")
            sys.exit()
        print(menuDesign)


menu_options()

