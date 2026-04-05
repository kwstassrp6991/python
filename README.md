# Student & Lesson Management System (C.R.U.D) 🎓

This is my first **C.R.U.D project** developed in Python. It is a comprehensive management system for an educational organization, allowing for the administration of students, teachers, and lessons with full data persistence.

## 🚀 Features

The system supports the following core functionalities:
* **Create:** Register new Students, Teachers, and Lessons.
* **Read:** View lists of registered users and detailed lesson information.
* **Update:** Modify existing records (e.g., enrolling a student in a specific lesson).
* **Delete:** Remove records from the system.
* **Data Persistence:** All changes are automatically saved to and loaded from **JSON** files.

## 📂 File Structure

* `main.py`: The main entry point featuring the application menu and logic flow.
* `lessons.py` / `pupils.py` / `teachers.py`: Controller classes handling the business logic.
* `lesson.py` / `pupil.py` / `teacher.py`: Data models (Classes) representing the entities.
* `*.json`: Acts as the database storage for all system information.

## 🛠️ Technologies Used

* **Python 3.x**
* **JSON Serialization:** Used to convert complex class objects into a readable text format for storage.
* **Object-Oriented Programming (OOP):** Implementation of classes, methods, and encapsulation to manage data effectively.

## ⚙️ Installation and Usage

1. Clone the repository:
   ```bash
   git clone [https://github.com/kwstassrp6991/python.git](https://github.com/kwstassrp6991/python.git)
