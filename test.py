def createEmployee():
    while True:
        employee_id = (input("|   Enter 4-Digit Employee ID: "))
        if employee_id.isnumeric() and len(employee_id) == 4:
            break
        print("|   Error! Employee ID must be 4-digit integer.")


createEmployee()