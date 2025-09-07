import json
import os
from pathlib import Path
from users import User
from books import Book
from employees import Employee

DATA_PATH = Path(
    "...OOP_library_manager/data/library_data.json")


_cache = {
    "books": [],       # List[Book]
    "users": [],       # List[User]
    "employees": []    # List[Employee]
}


def load_data(path: Path) -> dict:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_data_atomic(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    # reemplazo atómico
    os.replace(tmp, path)


def load_objects(path: Path = DATA_PATH):
    data = load_data(path)
    books_dictionary = [Book.from_dict(b) for b in data.get("books", [])]
    users_dictionary = [User.from_dict(u) for u in data.get("users", [])]
    employees_dictionary = [Employee.from_dict(
        e) for e in data.get("employees", [])]
    return books_dictionary, users_dictionary, employees_dictionary


def initialize_db(path: Path = DATA_PATH):
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


def search_book(op, value):
    books_list = get_books()
    if op == 1:
        for i in books_list:
            if i.name == value:
                print("Book founded.")
                return print(i)
        return print(f"There is no book '{value}' stored.")
    elif op == 2:
        for i in books_list:
            if i.author == value:
                print("Book founded.")
                return print(i)
        return print(f"There is no book '{value}' stored.")
    elif op == 3:
        for i in books_list:
            if i.year == value:
                print("Book founded.")
                return print(i)
        return print(f"There is no book '{value}' stored.")
    elif op == 4:
        for i in books_list:
            if i.isbn == value:
                print("Book founded.")
                return print(i)
        return print(f"There is no book '{value}' stored.")


def add_book():
    pass


def delete_book():
    pass


def save(path: Path = DATA_PATH):
    data = {
        "users": [u.to_dict() for u in _cache["users"]],
        "books": [b.to_dict() for b in _cache["books"]],
        "employees": [e.to_dict() for e in _cache["employees"]],
    }
    save_data_atomic(path, data)
