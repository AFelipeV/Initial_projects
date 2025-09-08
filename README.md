# Initial Projects

This repository contains different projects developed for learning and practice purposes, demonstrating concepts such as arguments, imports, tests and OOP, among others.

## Project Structure

```
initial_projects/
│   README.md
│   requirements.txt
│   .gitignore
│
├── main/
│   ├── __init__.py
│   └── demo_functions.py
|
├── OOP_library_manager/
│   ├── data/
│   └── src/
│
├── utils/
│   ├── __init__.py
│   └── math_utils.py
│
├── tests/
│   ├── __init__.py
│   └── test_math_utils.py
```

- **main/**: Contains the main script and demo functions.
- **utils/**: Includes reusable math utilities.
- **tests/**: Contains unit tests for the project.

## Requirements
- Python 3.8 or higher (required for pytest compatibility)
- `pytest` for running unit tests (see `requirements.txt`)


## Usage
From the project root, run:
```bash
python -m main.demo_functions
```

Run OOP library manager 
For detailed instructions, check the readme inside OOP_library_manager.

## Testing
Unit tests are located in the `tests/` directory and use `pytest`.
To run all tests:
```bash
pytest
```


## Features

### Demo Functions(main/)
- Sum any number of values.
- Arithmetic mean (with input validation).
- Median of a list of numbers (int and/or float).
- Basic logging for info, warnings, and errors.

### Library manager(OOP_library_manager/)
- Store books, users and employees.
- Search books by name, author, year or ISBN.
- Add and delete books.
- Persistent data storage in JSON format.


## Development Notes
- Input handling improved for robustness.
- Logging integrated using Python's standard `logging` module.
- `.gitignore` added to exclude cache and virtual environments.

