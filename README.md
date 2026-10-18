<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=800&size=36&duration=2500&pause=800&color=00D9FF&center=true&vCenter=true&width=850&height=100&lines=MULTI-UTILITY+TOOLKIT" alt="Multi-Utility Toolkit" />
  <h3><b><i>✨ A Modular Python Application ✨</i></b></h3>
</div>
<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Project](https://img.shields.io/badge/Project-Multi--Utility-purple?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

</div>

## 📑 Table of Contents

- 🚀 About the Project
- ✨ Features
- 🛠️ Technologies Used
- 📂 Project Structure
- 🔄 Application Workflow
- 🧩 Modular Architecture
- 👩‍💻 Author

------------------------------------------------------------------------

## 🚀 About the Project

**Multi-Utility Toolkit** is a menu-driven Python command-line
application that brings several small utilities together in one program.
Instead of writing a separate application for every task, the project
organizes related features into separate Python modules and provides a
central menu in `main.py`.

The user selects an option, the application opens the relevant utility
menu or function, accepts any required input, performs the operation,
and displays the result in the terminal. The user can then return to the
main menu or exit the application.

This project is designed for learning and demonstrating Python's
built-in modules, custom packages, functions, conditionals, loops, input
validation, exception handling, and file operations.

## 🎯 Project Objectives

-   Combine multiple utilities in one menu-driven application.
-   Understand how Python modules and packages organize code.
-   Practise importing functions from custom modules.
-   Use built-in modules for date/time operations, mathematics, random
    data, and UUID generation.
-   Handle user input and invalid values more safely.
-   Practise reading from and writing to text files where file
    operations are implemented.
-   Make code easier to read, test, maintain, and extend.

## ✨ Features

### 1. 🕒 Date and Time Operations

The date/time section can provide the following tools, depending on the
functions implemented in `utilities/datetime_utils.py`:

-   **Display Current Date and Time:** displays the current system date
    and time.
-   **Calculate Difference Between Dates:** accepts two dates in
    `YYYY-MM-DD` format and calculates the difference in days.
-   **Format Date:** displays a date in a selected format.
-   **Stopwatch:** measures elapsed time between a start and stop
    action.
-   **Countdown Timer:** counts down from a positive number of seconds.

**Python modules:** `datetime`, `time`

### 2. 🧮 Mathematical Operations

The mathematics section groups common calculations:

-   **Factorial:** calculates the factorial of a non-negative integer.
-   **Compound Interest:** calculates compound interest using the
    required principal, rate, time, and compounding inputs.
-   **Trigonometric Calculations:** calculates sine, cosine, and tangent
    for an angle entered in degrees.
-   **Area of Geometric Shapes:** calculates area for supported shapes
    such as a circle, rectangle, and triangle.

**Python module:** `math`

### 3. 🎲 Random Data Generation

The random-data section can include:

-   **Random Number:** generates a random number within a user-provided
    range.
-   **Random List:** generates a list of random values.
-   **Random Password:** creates a random password.
-   **Random OTP:** generates a one-time numeric code for demonstration.
-   **Random Sampling:** selects random items from a collection.
-   **Number Guessing Game:** lets the user guess a randomly selected
    number.

**Python module:** `random`

> **Security note:** a password or OTP generated with Python's `random`
> module is suitable for learning demonstrations, not for production
> authentication or security-sensitive systems. Use Python's `secrets`
> module for security-sensitive random values.

### 4. 🆔 UUID Generation

This section generates a UUID (Universally Unique Identifier), which is
a standard format for identifying an item with a highly low probability
of accidental duplication.

**Python module:** `uuid`

### 5. 📁 File Operations

The file-operations section demonstrates text-file handling, according
to the functions implemented in `utilities/file_utils.py`. Common
operations include creating a file, writing content, reading saved
content, and appending new content.

A text file such as `output.txt` is optional unless your project code
specifically requires it. The program's terminal output is not
automatically saved to a file unless the code implements that behaviour.

### 6. 🔍 Explore Built-in Modules

The module-explorer option demonstrates importing and inspecting
selected Python modules, for example:

-   `datetime` --- date and time tools
-   `math` --- mathematical functions
-   `random` --- random values and selections
-   `uuid` --- unique identifiers
-   `time` --- delays and elapsed time

The exact modules shown depend on the implementation in `main.py`.

------------------------------------------------------------------------

## 🧰 Technologies and Modules

  Technology / Module     Purpose
  ----------------------- -----------------------------------------------------
  **Python 3**            Main programming language
  `datetime`              Working with dates and times
  `time`                  Stopwatch, countdown, and delays
  `math`                  Mathematical and trigonometric calculations
  `random`                Random numbers, selections, and demonstration games
  `uuid`                  Generating UUID values
  `os` *(if used)*        Operating-system and file-path utilities
  Text-file handling      Reading and writing text data
  Custom Python package   Keeping utility code separated and reusable
  Visual Studio Code      Writing and running the project

------------------------------------------------------------------------

## 📂 Project Structure

The expected structure for this project is:

``` text
project7/
│
├── main.py
│
└── utilities/
    ├── __init__.py
    ├── datetime_utils.py
    ├── math_utils.py
    ├── random_utils.py
    ├── uuid_utils.py
    └── file_utils.py
```

### What each file does

  -----------------------------------------------------------------------
  File                                Responsibility
  ----------------------------------- -----------------------------------
  `main.py`                           Starts the application, displays
                                      the main menu, imports utility
                                      functions, and routes the user's
                                      choice to the correct section.

  `utilities/__init__.py`             Marks `utilities` as a Python
                                      package. It can be empty.

  `utilities/datetime_utils.py`       Contains date and time functions
                                      and the date/time submenu.

  `utilities/math_utils.py`           Contains mathematical calculations
                                      and the mathematics submenu.

  `utilities/random_utils.py`         Contains random-data tools and the
                                      random-data submenu.

  `utilities/uuid_utils.py`           Contains UUID-generation
                                      functionality.

  `utilities/file_utils.py`           Contains file-handling functions
                                      and the file-operations submenu.
  -----------------------------------------------------------------------

**Important:** filenames and function names used in `main.py` imports
must exactly match the actual files and functions. For example, if
`main.py` imports `datetime_menu`, then `datetime_utils.py` must define
a function with that exact name.

------------------------------------------------------------------------

## 🔄 Flowchart 1 --- Application Workflow

This flowchart explains the user's journey through the program.

``` mermaid
flowchart TD
    A([Start]) --> B[Run main.py]
    B --> C[Display Main Menu]
    C --> D{Choose an option}
    D -->|Date and Time| E[Open Date and Time Menu]
    D -->|Mathematics| F[Open Mathematics Menu]
    D -->|Random Data| G[Open Random Data Menu]
    D -->|UUID| H[Generate UUID]
    D -->|File Operations| I[Open File Operations Menu]
    D -->|Explore Modules| J[Explore Built-in Modules]
    D -->|Exit| K([End])
    E --> L[Accept Input and Perform Operation]
    F --> L
    G --> L
    H --> M[Display Result]
    I --> L
    J --> M
    L --> M
    M --> N{Return to Main Menu?}
    N -->|Yes| C
    N -->|No / Exit| K
```

### Flowchart explanation

1.  The program starts when `main.py` is executed.
2.  The main menu displays the available categories.
3.  The user enters a menu choice.
4.  The program calls the function associated with that choice.
5.  The selected utility asks for any required input and performs its
    task.
6.  The result or an error message is displayed in the terminal.
7.  The user can continue using the toolkit or choose Exit.

------------------------------------------------------------------------

## 🧩 Flowchart 2 --- Modular Architecture

This flowchart explains how the main program is connected to the
separate utility modules.

``` mermaid
flowchart TD
    A[main.py<br/>Main Menu and Navigation] --> B[datetime_utils.py]
    A --> C[math_utils.py]
    A --> D[random_utils.py]
    A --> E[uuid_utils.py]
    A --> F[file_utils.py]
    A --> G[Built-in Module Explorer]
    B --> H[Execute Selected Function]
    C --> H
    D --> H
    E --> H
    F --> H
    G --> H
    H --> I[Return / Display Result]
    I --> J[Back to Main Menu]
    J --> A
```

### Architecture explanation

-   **`main.py` is the entry point:** it coordinates the application and
    handles navigation.
-   **Each utility module has a focused responsibility:** date/time,
    mathematics, random data, UUIDs, or file handling.
-   **Imports connect the modules:** `main.py` imports the functions it
    needs from the `utilities` package.
-   **Functions keep code reusable:** the same function can be called
    whenever its operation is needed.
-   **The terminal displays the result:** the user sees the output and
    can choose the next action.

This modular design is easier to maintain than putting every feature
into one very large Python file.

------------------------------------------------------------------------

## 💻 Sample Main Menu

Your exact menu text may vary, but it can look like this:

``` text
===================================
       MULTI-UTILITY TOOLKIT
===================================
1. Date and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. UUID Generation
5. File Operations
6. Explore Built-in Modules
7. Exit

Enter your choice:
```

### Example of how to use it

-   Enter `1` to open the date and time section.
-   Choose an option displayed inside that section.
-   Enter the requested date, angle, number, or other value.
-   Read the result printed in the terminal.
-   Use the section's **Back to Main Menu** option to select another
    utility.
-   Enter `7` at the main menu to exit, if your program uses the menu
    shown above.

Always follow the option numbers printed by your actual running program.

------------------------------------------------------------------------

## 📸 Project Screenshots
<img width="960" height="5621" alt="ss7" src="https://github.com/user-attachments/assets/4d55360e-08f4-4569-8b1d-2cf5e0357d85" />
---

---

## 🎬 Project Demo


---
## 📚 Concepts Demonstrated

This project gives practice with the following Python concepts:

-   **Modules:** storing related code in separate `.py` files.
-   **Packages:** grouping modules in the `utilities` directory.
-   **Imports:** using functions defined in another module.
-   **Functions:** splitting tasks into reusable blocks.
-   **Conditional statements:** choosing actions based on user input.
-   **Loops:** keeping menus active until the user chooses to exit.
-   **Input and output:** collecting values with `input()` and
    displaying results with `print()`.
-   **Exception handling:** using `try` and `except` to handle invalid
    inputs.
-   **Built-in modules:** using `datetime`, `time`, `math`, `random`,
    and `uuid`.
-   **File handling:** opening, reading, writing, and appending text
    files where implemented.
-   **Modular design:** separating responsibilities to make code easier
    to understand and maintain.

------------------------------------------------------------------------

## 🛠️ Troubleshooting

### 1. `ModuleNotFoundError: No module named 'utilities...'`

**Possible cause:** the terminal is in the wrong folder, the module file
is missing, or the filename is misspelled.

**Fix:** - Open the terminal in the `project7` root folder. - Confirm
that `utilities/__init__.py` exists. - Confirm that the required module
exists, for example `utilities/random_utils.py`. - Check spelling in the
import statement and filename. - Run `python main.py` again from the
root folder.

### 2. `ImportError: cannot import name ...`

**Possible cause:** the module exists, but it does not define the
function name imported by `main.py`.

**Fix:** open the relevant utility file and confirm that the function
name exactly matches the import. Python names are case-sensitive.

### 3. The menu appears again after selecting an option

This is often expected behaviour: the selected task finishes, then the
program displays the menu again so another tool can be selected. Follow
the prompts inside the selected section.

### 4. `Invalid choice!`

Enter one of the option numbers displayed on the screen. For example, if
a submenu lists options `1` through `5`, entering `6` is invalid unless
the menu explicitly provides that option.

### 5. A text file cannot be found

Check the filename and the directory in which the program expects the
file. Relative paths are resolved from the program's current working
directory. If the program is intended to create a file, confirm that the
relevant code opens it in a writing mode such as `"w"` or `"a"`.

------------------------------------------------------------------------

## 👩‍💻 Author

**Dhara Padhariya**
Computer Engineering Student | Python Programming

**Project:** Multi-Utility Toolkit

**✨ Learn • Build • Improve ✨**

------------------------------------------------------------------------

