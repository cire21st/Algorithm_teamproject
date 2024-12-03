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

## Team Members
| Name    | GitHub Profile                                         | Email                                                |
|---------|--------------------------------------------------------|------------------------------------------------------|
| 박준우   | [<img src="https://img.shields.io/badge/GitHub-cire21st-black?logo=github" alt="cire21st">](https://github.com/cire21st)               | <img src="https://img.shields.io/badge/junu321kr@gmail.com-blue" alt="junu321kr@gmail.com">  |
| 홍성준   | [<img src="https://img.shields.io/badge/GitHub-cire21st-black?logo=github" alt="HongSeongJoon">](https://github.com/HongSeongJoon)               | <img src="https://img.shields.io/badge/sjhong0220@gmail.com-blue" alt="sjhong0220@gmail.com">  |
| 최예빈   | [<img src="https://img.shields.io/badge/GitHub-cire21st-black?logo=github" alt="">](https://github.com/)               | <img src="https://img.shields.io/badge/-blue" alt="">  |
| 정수현   | [<img src="https://img.shields.io/badge/GitHub-cire21st-black?logo=github" alt="">](https://github.com/)               | <img src="https://img.shields.io/badge/-blue" alt="">  |

## Project Structure
The directory structure for this repository is as follows:

<pre>
Algorithm_teamproject/
├── src/
│   └── main.py                   # Main script for filter selection and application
├── README.md                # Project documentation
├── TODO.md                  # TO DO list
└── LICENSE                  # MIT License
</pre>

## Key Features
1. **Automatic Addition of Core Subjects**:
   - Core major and general education courses are automatically added when their names are entered.
2. **Conflict-Free Scheduling**:
   - Ensures no time overlaps between lectures.
3. **Customizable Credit Limits**:
   - Minimum of 12 credits and a maximum of 18 credits can be set.
4. **Timetable Optimization**:
   - Uses Backtracking to ensure both credit and requirement fulfillment.

## How to Run

### 1. **Run the Application**  
Developed with **Python 3.12**.

Navigate and run `main.py` to start :
   ```bash
   cd src
   python main.py
   ```

## License
This project is distributed under the MIT License.
