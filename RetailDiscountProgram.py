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


# NOT FUNCTIONING HOW I WANT
def employee_summary():
    print(employee_data)


def discount_percentage(years_worked, employee_type, total_discount):
    while total_discount < 200:
        if years_worked < 5:
            discount = years_worked * 2
            if employee_type == 'manager':
                discount += 10
            elif employee_type == 'hourly':
                discount += 2
            return discount
        else:
            discount = 10
            if employee_type == 'manager':
                discount += 10
            elif employee_type == 'hourly':
                discount += 2
            return discount

    discount = 0
    return discount


def make_purchase():
    print("------------------------------------------------------------\n"
          "|   You are making a purchase.                             |\n"
          "------------------------------------------------------------")
    header = "| Item Number | Item Name | Item Cost "
    print(header)
    print(item_data)

    employee = None;

    while True:
        try:
            employee_discount = int(input("    Enter the employee discount number: "))
            if any(employee_discount == employee[6] for employee in employee_data):
                employee = next(employee for employee in employee_data if employee[6] == employee_discount)
                break
            else:
                print("    Error! That discount number doesn't exist.")
        except ValueError:
            print("    Error! Employee discount number must be numeric.")

    while True:
        try:
            item_number = int(input("    Enter item number you wish to purchase: "))
            if any(item_number == item[0] for item in item_data):
                break
            else:
                print("    Error! That item number doesn't exist.")
        except ValueError:
            print("    Error! Item number must be numeric.")

    confirm_purchase = input("    Would you like to confirm this purchase? (Y/N): ").lower()
    if confirm_purchase == "y":
        _, _, employee_type, years_worked, _, total_discount, _ = employee
        discount = discount_percentage(years_worked, employee_type, total_discount)

        item_cost = 0
        for item in item_data:
            if item[0] == item_number:
                item_cost = item[2]
                break

        cost_calc = item_cost * (discount / 100)
        final_cost = item_cost - cost_calc
        employee[5] += cost_calc

        print(f"Item Cost: ${item_cost}")
        print(f"Final Cost: ${round(final_cost, 2)}")
        print(f"Total Discount for Employee: ${round(employee[5], 2)}")

    elif confirm_purchase == "n":
        new_purchase = input("    Would you like to make a new purchase? (Y/N): ").lower()
        if new_purchase == "y":
            make_purchase()
        elif new_purchase == "n":
            print(employee_summary)
            ask_about_menu = (input("    Would you like to go to the main menu? (Y/N): ")).lower()
            if ask_about_menu == "y":
                print(menuDesign)
                menu_options()
            elif ask_about_menu == "n":
                print("------------------------------------------------------------\n"
                      "|   You are exiting the program. Bye!                      |\n"
                      "------------------------------------------------------------")
                sys.exit()
            while ask_about_menu not in ["y", "n"]:
                print("    Error! Please select either Y or N.")
                ask_about_menu = (input("    Would you like to go to the main menu? (Y/N): ")).lower()

        else:
            while new_purchase not in ["y", "n"]:
                print("    Error! Please select either Y or N.")
                new_purchase = input("    Would you like to make a new purchase? (Y/N): ").lower()

    else:
        while confirm_purchase not in ["y", "n"]:
            print("    Error! Please select either Y or N.")
            confirm_purchase = input("    Would you like to confirm this purchase? (Y/N): ").lower()


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
        elif menu_selection == "4":
            print("------------------------------------------------------------\n"
                  "|   All employee summary.                                  |\n"
                  "------------------------------------------------------------")
            employee_summary()
        elif menu_selection == "5":
            print("------------------------------------------------------------\n"
                  "|   You are exiting the program. Bye!                      |\n"
                  "------------------------------------------------------------")
            sys.exit()
        print(menuDesign)


menu_options()
