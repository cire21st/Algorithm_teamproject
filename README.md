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
   - **Greedy Algorithm**:
     - Quickly generates an initial timetable based on priority.
     - Prioritization: Major > Required Courses > High Credits > Early Ending Times.
   - **Backtracking Algorithm**:
     - Optimizes the initial timetable by exploring all possible combinations.
     - Ensures the maximum number of credits and fulfillment of conditions.
2. **Required Course Management**:
   - **Automatic Inclusion of Required Courses**:
     - Predefined required courses (e.g., Major A, Major B) are automatically added to the timetable upon input.
   - **Conflict Resolution**:
     - Required courses are prioritized and always included in the timetable.
     - Courses with lower priority are excluded when there are time conflicts.
3. **Priority-Based Timetable Optimization**:
   - **Time Conflict Resolution**:
     - Resolves time conflicts by excluding courses based on priority.
     - Ensures no time overlaps between lectures.
     - Priority Order:
       1. Major
       2. Required
       3. High Credits
       4. General.
   - **Exclusion Management**:
     - Courses excluded due to conflicts are not re-added to the timetable.
4. **Credit Management**:
   - Tracks total credits, major credits, and general credits.
   - Ensures graduation requirements are met.
5. **Priority-Based Timetable Optimization**:
   - **Time Conflict Resolution**:
     - Resolves time conflicts by excluding courses based on priority.
     - Priority Order:
       1. Major
       2. Required
       3. High Credits
       4. General.
   - **Exclusion Management**:
     - Courses excluded due to conflicts are not re-added to the timetable.
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
---

### **Result Comparison**
- **Comparison of Greedy and Backtracking Results**:
  - Displays both the initial timetable (Greedy) and the optimized timetable (Backtracking).
  - Enables users to compare the two results and choose the most suitable one.



### **Expandability**
- **Integration of User Preferences**:
  - Can incorporate user preferences such as excluding specific days or time slots (potential additional feature).
- **Support for Additional Algorithms**:
  - Can be extended to include other optimization algorithms like Dynamic Programming.

### **Key Benefit**
This program goes beyond a simple timetable creation tool to become an **Personalized Class Scheduler** designed to manage credits and meet graduation requirements efficiently. It is particularly valuable for students who need to handle complex schedules while maximizing their academic achievements. 😊

## License
This project is distributed under the MIT License.
