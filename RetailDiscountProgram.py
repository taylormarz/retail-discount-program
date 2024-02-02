import re
# Menu Page
menuDesign = ("----------------------------------------\n" +
              "|   Welcome back, Taylor!              |\n" +
              "----------------------------------------\n" +
              "|   1 - Create a New Employee          |\n" +
              "|   2 - Create an Item                 |\n" +
              "|   3 - Make a Purchase                |\n" +
              "|   4 - All Employee Summary           |\n" +
              "|   5 - Exit                           |\n" +
              "----------------------------------------")
print(menuDesign)
menuSelection = input("|   Enter Menu Option Selection:       |")

# List to store employee info
employee_list = []

# Create a New Employee Function
def create_employee():
    # employee_id creation + validation
    while True:
        employee_id = (input("|   Enter 4-Digit Employee ID: "))
        if employee_id.isnumeric() and len(employee_id) == 4:
            break
        print("|   Error! Employee ID must be 4-digit integer.")

    #employee_discount creation + validation
    while True:
        employee_name = (input("|   Enter Employee First and Last Name: "))
        if re.match(r'^[a-zA-Z]+([\' -][a-zA-Z]+)*$', employee_name):
            break
        print("|   Error! Employee name must be alphanumeric.")

    # employee_type creation + validation
    while employee_type not in ["Hourly", "Manager"]:
        employee_type = (input("|   Enter Employee Type (Hourly/Manager): "))
        print("|   Error! Employee Type must be Hourly or Manager.")
        if employee_type == "Hourly" or employee_type == "Manager":
            break

    # employee_type creation + validation
    employee_type = (input("|   Enter Employee Type (Hourly/Manager): "))
    while employee_type.lower() not in ["hourly", "manager"]:
        print("|   Error! Employee Type must be Hourly or Manager.")
        employee_type = (input("|   Enter Employee Type (Hourly/Manager): "))

create_employee()


