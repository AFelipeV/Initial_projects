# Initial Projects

This repository contains a small example Python project demonstrating concepts such as arguments, imports and tests, among others.

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

## Testing
Unit tests are located in the `tests/` directory and use `pytest`.
To run all tests:
```bash
pytest
```


## Features
- Sum any number of values
- Arithmetic mean (with input validation)
- Median of a list of numbers (int and/or float)
- Basic logging for info, warnings, and errors


## Development Notes
- Input handling improved for robustness
- Logging integrated using Python's standard `logging` module
- `.gitignore` added to exclude cache and virtual environments

