import re
import sys

# Menu Page
menuDesign = ("------------------------------------------------------------\n" +
              "|   Main Menu:                                             |\n" +
              "------------------------------------------------------------\n" +
              "|   1 - Create a New Employee                              |\n" +
              "|   2 - Create an Item                                     |\n" +
              "|   3 - Make a Purchase                                    |\n" +
              "|   4 - All Employee Summary                               |\n" +
              "|   5 - Exit                                               |\n" +
              "------------------------------------------------------------")
print(menuDesign)

# List to store employee info
employee_data = []


# Create a New Employee Function
def create_employee():
    print("------------------------------------------------------------\n"
          "|   You are creating a new employee.                       |\n"
          "------------------------------------------------------------")

    while True:
        try:
            employee_id = int(input("    Enter 4-Digit employee ID: "))
            if len(str(employee_id)) == 4:
                if not any(employee_id == employee[0] for employee in employee_data):
                    break
                else:
                    print("    Error! Employee ID already in use.")
            else:
                print("    Error! Employee ID must be 4-digit integer.")
        except ValueError:
            print("    Error! Employee ID must be 4-digit integer.")

    # employee_discount creation + validation
    while True:
        employee_name = (input("    Enter employee first and last name: "))
        if re.match(r'^[a-zA-Z]+([\' -][a-zA-Z]+)*$', employee_name):
            break
        print("    Error! Employee name must be alphanumeric.")

    # employee_type creation + validation
    employee_type = (input("    Enter employee type (Hourly/Manager): "))
    while employee_type.lower() not in ["hourly", "manager"]:
        print("    Error! Employee type must be Hourly or Manager.")
        employee_type = (input("    Enter employee type (Hourly/Manager): "))

    # years_worked creation + validation
    while True:
        try:
            years_worked = int(input("    Enter number of years employee has worked: "))
            break
        except ValueError:
            print("    Error! Employee years must be an integer.")

    # employee_purchases creation + set to 0 to start
    employee_purchases = 0

    # total_discount creation + set to 0 to start
    total_discount = 0

    # employee_discount creation + validation
    while True:
        try:
            employee_discount = int(input("    Enter employee discount number: "))
            if not any(employee_discount == employee[6] for employee in employee_data):
                break
            else:
                print("    Error! Employee discount number already assigned.")
        except ValueError:
            print("    Error! Employee discount must be an integer.")

    # Adding input for new employee to employee_data list
    employee_data.append([employee_id, employee_name, employee_type, years_worked,
                          employee_purchases, total_discount, employee_discount])

    # Option to add another employee
    # I CAN PROBABLY CONDENSE THIS INTO ITS OWN FUNCTION TO CALL IN EACH FUNCTION THAT USES IT !!!!!
    add_another_employee = (input("    Would you like to add another employee? (Y/N): ")).lower()
    if add_another_employee == "y":
        create_employee()
    elif add_another_employee == "n":
        ask_about_menu = (input("    Would you like to go to main menu? (Y/N): ")).lower()
        if ask_about_menu == "y":
            print(menuDesign)
            menu_options()
        elif ask_about_menu == "n":
            print("------------------------------------------------------------\n"
                  "|   You are exiting the program. Bye!                      |\n"
                  "------------------------------------------------------------")
            sys.exit()
    while add_another_employee not in ["y", "n"]:
        print("    Error! Please select either Y or N.")
        add_another_employee = (input("    Would you like to add another employee? (Y/N): ")).lower()


# Create  list to store item data
item_data = []


# Create an Item Function
def create_item():
    print("------------------------------------------------------------\n"
          "|   You are creating a new item.                           |\n"
          "------------------------------------------------------------")
    while True:
        try:
            item_number = int(input("    Enter 5-digit item integer: "))
            if len(str(item_number)) == 5:
                if not any(item_number == item[0] for item in item_data):
                    break
                else:
                    print("    Error! That item number is already in use.")
            else:
                print("    Error! Item number must be 5-digit integer.")
        except ValueError:
            print("    Error! Item number must be 5-digit integer.")

    while True:
        item_name = input("    Enter item name: ")
        if re.match(r'^[a-zA-Z]+([\' -][a-zA-Z]+)*$', item_name):
            break
        print("    Error! Item name must be alphanumeric.")

    while True:
        try:
            item_cost = float(input("    Enter item cost: $"))
            break
        except ValueError:
            print("    Error! Item cost must be numeric.")

    item_data.append([item_number, item_name, item_cost])

    # Option to add another item
    # I CAN PROBABLY CONDENSE THIS INTO ITS OWN FUNCTION TO CALL IN EACH FUNCTION THAT USES IT !!!!!
    add_another_item = (input("    Would you like to add another item? (Y/N): ")).lower()
    if add_another_item == "y":
        create_item()
    elif add_another_item == "n":
        ask_about_menu = (input("    Would you like to go to main menu? (Y/N): ")).lower()
        if ask_about_menu == "y":
            print(menuDesign)
            menu_options()
        elif ask_about_menu == "n":
            print("------------------------------------------------------------\n"
                  "|   You are exiting the program. Bye!                      |\n"
                  "------------------------------------------------------------")
            sys.exit()
    while add_another_item not in ["y", "n"]:
        print("    Error! Please select either Y or N.")
        add_another_item = (input("    Would you like to add another item? (Y/N): ")).lower()


def make_purchase():
    print("------------------------------------------------------------\n"
          "|   You are making a purchase.                             |\n"
          "------------------------------------------------------------")


# Menu Selection Function
def menu_options():
    while True:
        menu_selection = input("    Enter Menu Option Selection: ")
        if menu_selection == "1":
            create_employee()
        elif menu_selection == "2":
            create_item()
        elif menu_selection == "3":
            make_purchase()
        # NOT FUNCTIONING HOW I WANT
        elif menu_selection == "4":
            if not employee_data:
                print("    No employees in the system.")
            else:
                header = ("| Employee ID    | Employee Name   | Employee Type   | Years Worked    | Total Purchased "
                          "| Total Discount  | Discount Number |")
                print(header)
                print("-" * len(header))  # Print a separator line

                # Determine the maximum width for each column based on header length
                max_lengths = [max(len(item.strip()) for item in column.split('|'))
                               for column in header.split('|')[1:-1]]

                for employee_information in employee_data:
                    formatted_data = (f"| {employee_information[0]:<{max_lengths[0]}} "
                                      f"| {employee_information[1]:<{max_lengths[1]}} "
                                      f"| {employee_information[2]:<{max_lengths[2]}} "
                                      f"| {employee_information[3]:<{max_lengths[3]}} "
                                      f"| {employee_information[4]:<{max_lengths[4]}} "
                                      f"| {employee_information[5]:<{max_lengths[5]}} "
                                      f"| {employee_information[6]:<{max_lengths[6]}} |")
                    print(formatted_data)



        elif menu_selection == "5":
            print("------------------------------------------------------------\n"
                  "|   You are exiting the program. Bye!                      |\n"
                  "------------------------------------------------------------")
            sys.exit()
        print(menuDesign)


menu_options()
