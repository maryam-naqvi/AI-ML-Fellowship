# Task 4: Libraries, Packaging & Modularization

This project demonstrates how to refactor simple scripts into production-ready, modular Python packages. It includes virtual environment management (`venv`), dependency tracking, and a custom package structure.

## 🔄 Modular Refactoring (Requirement Met)
I converted the standalone scripts from **Task 1** into reusable modules:

| Original Script (Task 1) | Refactored Module (Task 4) | Function Created |
| :--- | :--- | :--- |
| `area_of_circle.py` | `modules/math_utils.py` | `calculate_circle_area()` |
| `factorial.py` | `modules/math_utils.py` | `factorial()` |
| `String_reverse.py` | `mypackage/transformer.py` | `reverse_string()` |

*Note: The Logic was extracted and separated from user input `print` statements to ensure reusability.*

## 📂 Project Structure
```text
Task 4/
├── modules/                  # Standard Modules
│   └── math_utils.py         # Refactored math logic
├── mypackage/                # Custom Python Package
│   ├── __init__.py           # Package initialization
│   └── transformer.py        # String manipulation logic
├── venv/                     # Virtual Environment (Ignored by Git)
├── main.py                   # Entry point using all modules
├── requirements.txt          # Dependency list
└── README.md                 # Documentation

# Task 4: Libraries...
(bla bla bla)



## 🛠 How to Run
1. Activate Virtual Environment:
   venv\Scripts\activate

2. Install Dependencies:
   pip install -r requirements.txt

3. Run the Main Application:
   python main.py