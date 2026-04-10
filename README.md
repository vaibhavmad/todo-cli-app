# todo-cli-app
A simple command-line ToDo application built with Python, supporting add, edit, complete, and view operations with persistent file storage.

# Todo CLI App (Python)
A simple command-line Todo application built using Python.  
This project demonstrates core programming concepts like functions, modules, file handling, and error handling.

## Features
- Add new todos  
- Edit existing todos  
- Mark todos as complete  
- View all todos  
- Persistent storage using a text file  

## Tech Stack
- Python  
- File Handling (read/write)  
- Modular Code Structure  

## Project Structure
```
todo-cli-app/
│
├── modules/
│   ├── read_file.py
│   ├── write_file.py
│   └── __init__.py
│
├── app.py
├── todos.txt
└── README.md
```

## How to Run
1. Clone the repository: git clone
2. Navigate to the project folder: cd todo-cli-app
3. Run the application: python app.py or python3 app.py

## Example Usage
Select: Add, Edit, Complete, Show or Exit:
Commands:
- `add Buy milk`
- `edit 1`
- `complete 2`
- `show`
- `exit`

## What I Learned
- Writing modular Python code  
- Handling user input and errors  
- Working with files for data persistence  
- Structuring a simple CLI application

## Key Concepts Demonstrated
- File I/O operations
- Modular programming (custom modules)
- Error handling (try/except)
- CLI input processing
- Basic state persistence

## Future Improvements
- Improve input parsing using `split()`  
- Add timestamps to todos  
- Convert to GUI version  
- Add database support  

## Author
Built as part of my Python learning journey.
