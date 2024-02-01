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

# Create a New Employee Function
def create_employee():
    # employee_id creation + validation
    while True:
        employee_id = (input("|   Enter 4-Digit Employee ID: "))
        if employee_id.isnumeric() and len(employee_id) == 4:
            break
        print("|   Error! Employee ID must be 4-digit integer.")


create_employee()


