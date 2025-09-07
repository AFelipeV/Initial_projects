from employees import Employee
from users import User
from data_base import initialize_db, get_employees, search_book, add_book, delete_book
import logging
import sys

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    initialize_db()


def verify_employee(option):
    logging.warning(
        "Employee credentials are requiered to perform this operation.")
    employees_list = get_employees()
    credential = int(input("Enter your id: "))
    if option == 3:
        for emp in employees_list:
            emp_data = emp.to_dict()
            if credential in emp_data.values():
                logging.info("Credentials verified succesfully.")
                return add_book()
        return print("Invalid employee credentials. Access denied.")
    elif option == 4:
        for emp in employees_list:
            emp_data = emp.to_dict()
            if credential in emp_data.values():
                logging.info("Credentials verified succesfully.")
                return delete_book()
        return print("Invalid employee credentials. Access denied.")


logging.info("Program started.")
main()

print("Welcome to the 'World of Books'. \nPlease select an option:")
try:
    while True:
        print(
            "1. Search for a book \n"
            "2. Purchase a book \n"
            "3. Add book \n"
            "4. Delete book \n"
            "5. Exit"
        )
        try:
            oper = int(input("Enter your choice: "))
        except ValueError:
            logging.warning("Invalid input. Please enter a valid input.")
            continue
        if oper == 1:
            print("Select a search option:")
            try:
                while True:
                    print(
                        "1. By name \n"
                        "2. By author \n"
                        "3. By year \n"
                        "4. By ISBN \n"
                        "5. Go back."
                    )
                    try:
                        option = int(
                            input("Enter your choice: "))
                    except ValueError:
                        logging.warning(
                            "Invalid input. Please enter a valid input.")
                        continue
                    if option == 1:
                        value_to_search = input("Enter the book name: ")
                        search_book(option, value_to_search)
                    elif option == 2:
                        value_to_search = input("Enter the book author: ")
                        search_book(option, value_to_search)
                    elif option == 3:
                        value_to_search = int(
                            input("Enter the year of the publication: "))
                        search_book(option, value_to_search)
                    elif option == 4:
                        value_to_search = input("Enter the ISBN of the book: ")
                        search_book(option, value_to_search)
                    elif option == 5:
                        logging.info("Search ended by user.")
                        break
                    else:
                        logging.warning("Invalid option. Please try again.")
            except KeyboardInterrupt:
                logging.info("Program interrupted by user.")
                sys.exit("\nExiting...")
        elif oper == 2:
            logging.warning("Option not yet implemented.")
            continue
        elif oper == 3:
            verify_employee(oper)
        elif oper == 4:
            verify_employee(oper)
        elif oper == 5:
            logging.info("Program exited succesfully.")
            break
        else:
            logging.warning("Invalid option. Please try again.")
except KeyboardInterrupt:
    logging.info("Program interrupted by user.")
    sys.exit("\nExiting...")
