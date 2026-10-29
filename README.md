# 🎓 Student Management System (Python OOP)

A simple **Student Management System** built using Python and Object-Oriented Programming (OOP). This project allows users to manage student records, store marks, calculate results, and view class statistics.

## 📌 Features

* ➕ **Add Student** — Add a new student with ID, name, and class.
* 📋 **View Students** — Display all registered students.
* 🔍 **Search Student** — Search for a student using their ID.
* ✏️ **Update Student** — Update student information.
* 🗑️ **Delete Student** — Remove a student record.
* 📝 **Add Marks** — Add marks for multiple subjects.
* 📊 **Calculate Results** — Calculate total marks, average percentage, and grade.
* 📄 **Student Report** — Display a student's information and result.
* 📈 **Class Statistics** — Display class average, highest and lowest scorers, and pass/fail counts.
* 💾 **Save Data** — Save student records to a JSON file.
* 📂 **Load Data** — Load previously saved student records when the program starts.

## 🛠️ Technologies Used

* **Python 3**
* **Object-Oriented Programming (OOP)**
* **JSON** for data storage
* **Git and GitHub** for version control

## 🧠 OOP Concepts Used

This project demonstrates the following OOP concepts:

* **Classes and Objects:** The `Student` and `StudentManagementSystem` classes organize the program's functionality.
* **Constructor (`__init__`):** Initializes student information and management system attributes.
* **Instance Attributes:** Store student ID, name, class, and marks.
* **Instance Methods:** Perform operations such as adding marks, calculating results, and managing student records.
* **Encapsulation through Classes:** Keeps related data and functionality organized within classes.

## 📁 Project Structure

```text
Student-Management-System/
│
├── Menu(OOP).py
├── README.md
├── .gitignore
└── stu_data.json  # Generated when data is saved
```

*Note: The filenames may differ depending on how you organize your project.*

## ⚙️ Requirements

* Python 3 installed on your computer.
* No external Python packages are required; the project uses Python's built-in `json` module.

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Student-Management-System.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Open the Project Folder

```bash
cd Student-Management-System
```

### 3. Run the Program

If your Python file is named `main.py`, run:

```bash
python main.py
```

Depending on your system, you may need to use:

```bash
python3 main.py
```

## 📋 Menu Options

| Option | Function        |
| ------ | --------------- |
| 1      | Add Student     |
| 2      | View Students   |
| 3      | Search Student  |
| 4      | Update Student  |
| 5      | Delete Student  |
| 6      | Add Marks       |
| 7      | Student Result  |
| 8      | Student Report  |
| 9      | Show Statistics |
| 10     | Save Data       |
| 11     | Exit            |

## 💾 Data Storage

Student records are stored in a JSON file named `stu_data.json`.

The program can load previously saved data when it starts. Use the **Save Data** menu option to save the latest changes.

**Important:** The generated JSON file may contain student information. Avoid uploading real or sensitive student data to a public repository.

## 🎯 Learning Objectives

This project was created to practise:

* Understanding Python classes and objects.
* Converting procedural code into an OOP structure.
* Using instance attributes and methods.
* Working with lists and dictionaries.
* Reading and writing JSON files.
* Applying basic CRUD operations.
* Using Git and GitHub to manage a project.

## 🔮 Future Improvements

Possible improvements include:

* Input validation for student IDs and marks.
* Preventing duplicate subject entries.
* Automatically saving data when exiting.
* Adding a graphical user interface (GUI).
* Adding unit tests.
* Using a database for persistent storage.

## 👨‍💻 Author

Sidra Tariq

Created as a Python Object-Oriented Programming practice project.

## 📄 License

This project is available for educational and learning purposes.
