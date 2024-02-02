import re
def createEmployee():
    global employee_type

    while True:
        try:
            employee_id = int(input("|   Enter 4-Digit Employee ID: "))
            if len(str(employee_id)) == 4:
                break
            else:
                print("|   Error! Employee ID must be 4-digit integer.")
        except ValueError:
            print("|   Error! Employee ID must be 4-digit integer.")

    # employee_discount creation + validation
    while True:
        employee_name = (input("|   Enter Employee First and Last Name: "))
        if re.match(r'^[a-zA-Z]+([\' -][a-zA-Z]+)*$', employee_name):
            break
        print("|   Error! Employee name must be alphanumeric.")

    # employee_type creation + validation
    employee_type = (input("|   Enter Employee Type (Hourly/Manager): "))
    while employee_type.lower() not in ["hourly", "manager"]:
        print("|   Error! Employee Type must be Hourly or Manager.")
        employee_type = (input("|   Enter Employee Type (Hourly/Manager): "))

    # years_worked creation + validation
    while True:
        try:
            years_worked = int(input("|   Enter Number of Years Employee has Worked: "))
            break
        except ValueError:
            print("|   Error! Employee Years must be an integer.")


createEmployee()