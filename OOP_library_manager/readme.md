# OOP Library Manager

A Python object-oriented project for managing a small digital library.  
It handles **books, users, employees** with JSON persistence.

## Project Structure

```
OOP_library_manager/
├── src/
|   ├── __init__.py
│   ├── books.py
│   ├── data_base.py
│   ├── employes.py
|   ├── user_interface.py
│   └── users.py
├── data/
│   └── library_data.json
└── readme.md
```

## Usage

1. Clone the repository.
2. Run the `user_interface.py` file to start the application.

```bash
python src/user_interface.py
```

## Features

- Store books, users and employees.
- Search books by name, author, year or ISBN.
- Add and delete books.
- Persistent data storage in JSON format.