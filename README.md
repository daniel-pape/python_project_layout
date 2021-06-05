# About

This is a simple skeleton for a Python project with one
package with placeholder name `packagename` I use for bootstrapping
Python projects.

# How to get

```bash
mkdir $PROJECT_DIR
git clone https://github.com/daniel-pape/python_project_layout.git $PROJECT_DIR
```

# Project layout

```
.                                   # Root of $PROJECT_DIR
├── README.md                       # This file
├── setup.py                        # To make package `packagename` installable via `pip`
├── src
│   └── packagename                 # The single root package of this project    
│       ├── __init__.py
│       ├── some_module.py
│       └── subpackage              # One of the possible subpackages
│           ├── __init__.py
│           └── another_module.py
└── test                            # Some tests
    ├── test_buzz.py
    ├── test_fizz.py
    └── test_fizzbuzz.py
```

To get this output do `cd $PROJECT_DIR` followed by `tree`.

# How to use

```bash
cd $PROJECT_DIR
# Install package `packagename` (cf. `setup.py`)
pip install -e .
# Run tests in `test/`
pytest
```
