import json
import os
from pathlib import Path
from users import User
from books import Book
from employees import Employee

DATA_PATH = Path("...OOP_library_manager/data/library_data.json")


_cache = {
    "books": [],
    "users": [],
    "employees": []
}


def load_data(path: Path) -> dict:
    """
    Load raw JSON data from a file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        dict: Parsed JSON content as a dictionary. 
              Returns an empty dictionary if the file does not exist.
    """
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_data_atomic(path: Path, data: dict):
    """
    Save JSON data to a file using an atomic write to prevent corruption.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    os.replace(tmp, path)


def load_objects(path: Path = DATA_PATH):
    """
    Load objects (Books, Users, Employees) from the JSON file.

    Args:
        path (Path, optional): Path to the JSON file. Defaults to DATA_PATH.

    Returns:
        tuple: A tuple containing three lists:
               - books (List[Book])
               - users (List[User])
               - employees (List[Employee])
    """
    data = load_data(path)
    books_dictionary = [Book.from_dict(b) for b in data.get("books", [])]
    users_dictionary = [User.from_dict(u) for u in data.get("users", [])]
    employees_dictionary = [Employee.from_dict(
        e) for e in data.get("employees", [])]
    return books_dictionary, users_dictionary, employees_dictionary


def initialize_db(path: Path = DATA_PATH):
    """
    Initialize the in-memory cache with data from the JSON file.

    Args:
        path (Path, optional): Path to the JSON file. Defaults to DATA_PATH.
    """
    books, users, employees = load_objects(path)
    _cache["books"] = books
    _cache["users"] = users
    _cache["employees"] = employees


def get_books():
    return _cache["books"]


def get_users():
    return _cache["users"]


def get_employees():
    return _cache["employees"]


def search_book(op: int, value: str):
    """
    Search for a book in the cache by a given attribute.

    Args:
        op (int): The attribute to search by.
        value (str): The value to match against the chosen attribute.

    Returns:
        None: Prints the result of the search.
    """
    books_list = get_books()
    if op == 1:
        for i in books_list:
            if i.name == value:
                print("Book founded.")
                return print(i)
        return print(f"No book named '{value}' was found.")
    elif op == 2:
        for i in books_list:
            if i.author == value:
                print("Book found.")
                return print(i)
        return print(f"No book by author '{value}' was found.")
    elif op == 3:
        for i in books_list:
            if i.year == value:
                print("Book found.")
                return print(i)
        return print(f"No book published in '{value}' was found.")
    elif op == 4:
        for i in books_list:
            if i.isbn == value:
                print("Book found.")
                return print(i)
        return print(f"No book with ISBN '{value}' was found.")


def add_book():
    """
    Prompt the user to add a new book to the cache.

    Requests input for book name, author, year, and ISBN.
    If the ISBN already exists in the database, the book is not added.

    Returns:
        None: Prints confirmation messages.
    """
    book_name = input("Enter the book name: ")
    book_author = input("Enter the author's name: ")
    book_year = int(input("Enter the year of publication: "))
    book_isbn = input("Enter the book's ISBN: ")
    if any(b.isbn == book_isbn for b in _cache["books"]):
        print("Error: This book already exists in the database")
        return

    new_book = Book(book_name, book_author, book_year, book_isbn)
    _cache["books"].append(new_book)
    save()
    print("Book added successfully: ", new_book.to_dict())


def delete_book():
    """
    Prompt the user to delete a book by its ISBN.

    Returns:
        None: Prints confirmation or error message.
    """
    book_isbn = input("Enter the ISBN of the book to delete: ")
    book_to_delete = next(
        (b for b in _cache["books"] if b.isbn == book_isbn), None)
    if book_to_delete:
        print(book_to_delete.to_dict())
        _cache["books"].remove(book_to_delete)
        save()
        print("Book deleted successfully.")
    else:
        print("No matching book was found.")


def save(path: Path = DATA_PATH):
    """
    Save all cached data (users, books, employees) to a JSON file.

    Args:
        path (Path, optional): The destination file path. Defaults to DATA_PATH.

    Returns:
        None
    """
    data = {
        "users": [u.to_dict() for u in _cache["users"]],
        "books": [b.to_dict() for b in _cache["books"]],
        "employees": [e.to_dict() for e in _cache["employees"]],
    }
    save_data_atomic(path, data)
