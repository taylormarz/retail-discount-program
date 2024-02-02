import re
def createEmployee():
    global employee_type
    while True:
        employee_id = (input("|   Enter 4-Digit Employee ID: "))
        if employee_id.isnumeric() and len(employee_id) == 4:
            break
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


createEmployee()