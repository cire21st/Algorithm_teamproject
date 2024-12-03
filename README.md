# Personalized Class Scheduler 📚🎓

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white" alt="Python 3.12">
  <img src="https://img.shields.io/badge/Algorithm-Greedy%20%26%20Backtracking-green" alt="Algorithm: Greedy & Backtracking">
  <img src="https://img.shields.io/badge/IDE-PyCharm-000000?logo=pycharm&logoColor=white" alt="PyCharm IDE">
  <img src="https://img.shields.io/badge/License-MIT-yellow?logo=license&logoColor=white" alt="MIT License">
</p>

## Project Overview
This repository is dedicated to the Algorithm team project for the Algorithm Course, 2024, at Gachon University.
The "Personalized Class Scheduler" is a program designed for students who value academic efficiency. By utilizing **Greedy Algorithm** and **Backtracking**, the system generates an optimal timetable that fulfills graduation requirements while maximizing credit hours.
This system automatically manages **core subjects**, such as major and general education requirements, and generates a conflict-free schedule tailored to the user's preferences. Users can define credit limits and quickly view their optimized timetable.

## **Motivation**
Students often face challenges in creating a timetable that balances:
1. Meeting graduation requirements for major and general education credits.
2. Avoiding scheduling conflicts between courses.
3. Maximizing the number of credits taken per semester.
This project aims to address these challenges by automating the process using advanced algorithms and providing a user-friendly interface for easy management.


## Team Members
| Name    | GitHub Profile                                         | Email                                                |
|---------|--------------------------------------------------------|------------------------------------------------------|
| 박준우   | [<img src="https://img.shields.io/badge/GitHub-cire21st-black?logo=github" alt="cire21st">](https://github.com/cire21st)               | <img src="https://img.shields.io/badge/junu321kr@gmail.com-blue" alt="junu321kr@gmail.com">  |
| 홍성준   | [<img src="https://img.shields.io/badge/GitHub-HongSeongJoon-black?logo=github" alt="HongSeongJoon">](https://github.com/HongSeongJoon)               | <img src="https://img.shields.io/badge/sjhong0220@gmail.com-blue" alt="sjhong0220@gmail.com">  |
| 최예빈   | [<img src="https://img.shields.io/badge/GitHub-cire21st-black?logo=github" alt="">](https://github.com/)               | <img src="https://img.shields.io/badge/-blue" alt="">  |
| 정수현   | [<img src="https://img.shields.io/badge/GitHub-cire21st-black?logo=github" alt="">](https://github.com/)               | <img src="https://img.shields.io/badge/-blue" alt="">  |

## Project Structure
The directory structure for this repository is as follows:

<pre>
Algorithm_teamproject/
├── src/
│   └── Exemplary_Scheduler.py                   # Main script for filter selection and application
├── README.md                # Project documentation
├── TODO.md                  # TO DO list
└── LICENSE                  # MIT License
</pre>

## Key Features
1. **Automated Timetable Generation**:
   - Greedy algorithm for quick initial timetable creation.
   - Backtracking algorithm for further optimization.
2. **Automatic Addition of Core Subjects**:
   - Core major and general education courses are automatically added when their names are entered.
3. **Conflict-Free Scheduling**:
   - Ensures no time overlaps between lectures.
4. **Credit Management**:
   - Tracks total credits, major credits, and general credits.
   - Ensures graduation requirements are met.
5. **Conflict Resolution**:
   - Automatically excludes lower-priority courses during time conflicts.
6. **User-Friendly Interface**:
   - Intuitive GUI for inputting course details and visualizing timetables.

## **Technologies Used**
- **Programming Language**: Python
- **Libraries**:
  - `tkinter` for GUI development.
  - Built-in Python algorithms for scheduling optimization.
- **Algorithms**:
  - Greedy Algorithm for initial scheduling.
  - Backtracking Algorithm for exploring and selecting optimal schedules.
---

## How to Run

### 1. **Run the Application**  
Developed with **Python 3.12**.

Navigate and run `Exemplary_Scheduler.py` to start :
   ```bash
   cd src
   python Exemplary_Scheduler.py
   ```

### **How It Works**
1. **Input**:
   - Users input course details (name, days, start/end times, credits, type, and required status) via a GUI.
   - Predefined required courses are automatically included.
2. **Processing**:
   - The system processes the input using the Greedy algorithm to create a quick, conflict-free timetable.
   - Backtracking optimizes the timetable by exploring all possible combinations.
3. **Output**:
   - Visualizes the timetable in a grid format.
   - Displays total credits, major credits, and general credits to track progress toward graduation.



## License
This project is distributed under the MIT License.
