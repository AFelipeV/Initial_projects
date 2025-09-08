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
    try:
        credential = int(input("Enter your ID: "))
    except ValueError:
        logging.warning("Invalid ID format. Must be a number.")
        return

    for emp in employees_list:
        emp_data = emp.to_dict()
        if credential in emp_data.values():
            logging.info("Credentials verified successfully.")
            if option == 3:
                return add_book()
            elif option == 4:
                return delete_book()
    print("Invalid employee credentials. Access denied.")


def get_choice(prompt, options):
    while True:
        try:
            choice = int(input(prompt))
            if choice in options:
                return choice
            logging.warning("Invalid option. Please try again.")
        except ValueError:
            logging.warning("Invalid input. Please enter a number.")


def main_menu():
    print("\nWelcome to the 'World of Books'.")
    print("Please select an option:")
    print(
        "1. Search for a book\n"
        "2. Purchase a book\n"
        "3. Add book\n"
        "4. Delete book\n"
        "5. Exit"
    )
    return get_choice("Enter your choice: ", [1, 2, 3, 4, 5])


def search_menu():
    print("\nSelect a search option:")
    print(
        "1. By name\n"
        "2. By author\n"
        "3. By year\n"
        "4. By ISBN\n"
        "5. Go back"
    )
    return get_choice("Enter your choice: ", [1, 2, 3, 4, 5])


def handle_search():
    while True:
        option = search_menu()
        if option == 5:
            logging.info("Search ended by user.")
            break
        value_to_search = input("Enter search value: ")
        if option == 3:
            try:
                value_to_search = int(value_to_search)
            except ValueError:
                logging.warning("Invalid year. Please enter a number.")
                continue
        search_book(option, value_to_search)


def run():
    logging.info("Program started.")
    main()

    try:
        while True:
            oper = main_menu()

            if oper == 1:
                handle_search()
            elif oper == 2:
                logging.warning("Option not yet implemented.")
            elif oper in (3, 4):
                verify_employee(oper)
            elif oper == 5:
                logging.info("Program exited successfully.")
                break
    except KeyboardInterrupt:
        logging.info("Program interrupted by user.")
        sys.exit("\nExiting...")


if __name__ == "__main__":
    run()
