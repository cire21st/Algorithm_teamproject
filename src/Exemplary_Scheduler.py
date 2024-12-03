import tkinter as tk
from tkinter import messagebox


# 학점 계산 (중복 강의 제거)
def calculate_credits(schedule):
    seen_courses = set()
    total_credits = 0
    major_credits = 0
    general_credits = 0

    for day_courses in schedule.values():
        for course in day_courses:
            if course["name"] not in seen_courses:
                seen_courses.add(course["name"])
                total_credits += course["credits"]
                if course["type"] == "전공":
                    major_credits += course["credits"]
                elif course["type"] == "교양":
                    general_credits += course["credits"]

    return total_credits, major_credits, general_credits


# 시간표 출력 (GUI)
def display_schedule_gui(schedule, calculate_credits, title="시간표"):
    """시간표를 표 형식으로 GUI 창에 출력."""
    window = tk.Tk()
    window.title(title)
    window.geometry("800x600")

    total_credits, major_credits, general_credits = calculate_credits(schedule)
    credit_info = tk.Label(
        window,
        text=f"총 학점: {total_credits} | 전공 학점: {major_credits}/60 | 교양 학점: {general_credits}/30",
        font=("Arial", 14),
        pady=10
    )
    credit_info.pack()

    timetable_frame = tk.Frame(window)
    timetable_frame.pack(expand=True, fill="both", padx=10, pady=10)

    days = ['월', '화', '수', '목', '금']
    start_hour, end_hour = 8, 18
    time_slots = list(range(start_hour, end_hour + 1))

    for col, day in enumerate(["시간"] + days):
        tk.Label(
            timetable_frame,
            text=day,
            font=("Arial", 12, "bold"),
            relief="ridge",
            padx=10,
            pady=5,
            bg="#f0f0f0"
        ).grid(row=0, column=col, sticky="nsew")

    for row, hour in enumerate(time_slots, start=1):
        tk.Label(
            timetable_frame,
            text=f"{hour}:00",
            font=("Arial", 10),
            relief="ridge",
            padx=10,
            pady=5,
            bg="#f9f9f9"
        ).grid(row=row, column=0, sticky="nsew")

    for col, day in enumerate(days, start=1):
        for row, hour in enumerate(time_slots, start=1):
            frame = tk.Frame(timetable_frame, relief="ridge", borderwidth=1, bg="white")
            frame.grid(row=row, column=col, sticky="nsew")
            for course in schedule[day]:
                if course["start_time"] <= hour < course["end_time"]:
                    tk.Label(
                        frame,
                        text=course["name"],
                        font=("Arial", 10),
                        bg="#d0e8f2" if course["type"] == "전공" else "#f2d0d0",
                        padx=5,
                        pady=5,
                        wraplength=100
                    ).pack(fill="both", expand=True)

    for row in range(len(time_slots) + 1):
        timetable_frame.grid_rowconfigure(row, weight=1)
    for col in range(len(days) + 1):
        timetable_frame.grid_columnconfigure(col, weight=1)

    tk.Button(window, text="닫기", command=window.destroy).pack(pady=10)
    window.mainloop()


# Greedy 알고리즘으로 시간표 생성
def greedy_schedule(courses, max_credits):
    excluded_courses = set()  # 배제된 과목 기록
    sorted_courses = sorted(
        courses,
        key=lambda x: (
            x["type"] == "교양",  # 교양은 뒤로
            not x["required"],  # 필수 과목 우선
            -x["credits"],  # 높은 학점 우선
            x["end_time"]  # 빨리 끝나는 과목 우선
        )
    )
    schedule = {day: [] for day in ['월', '화', '수', '목', '금']}
    total_credits = 0

    for course in sorted_courses:
        if add_course_to_schedule(schedule, course, excluded_courses):
            total_credits += course["credits"]
            if total_credits >= max_credits:
                break

    return schedule


# Backtracking으로 최적화
def optimize_schedule(initial_schedule, courses, predefined_required_courses, max_credits):
    excluded_courses = set()  # 배제된 과목 기록
    courses += [course for course in predefined_required_courses if course not in courses]
    best_schedule = initial_schedule
    best_credits = calculate_credits(initial_schedule)[0]

    def backtrack(current_schedule, current_credits, index):
        nonlocal best_schedule, best_credits
        if current_credits > best_credits:
            best_schedule = {day: current_schedule[day][:] for day in current_schedule}
            best_credits = current_credits
        if current_credits >= max_credits:
            return
        for i in range(index, len(courses)):
            course = courses[i]
            if add_course_to_schedule(current_schedule, course, excluded_courses):  # excluded_courses 추가
                current_credits += course["credits"]
                backtrack(current_schedule, current_credits, i + 1)
                current_credits -= course["credits"]
                for day in course["days"]:
                    current_schedule[day].remove(course)

    initial_credits = calculate_credits(initial_schedule)[0]
    backtrack(initial_schedule, initial_credits, 0)
    return best_schedule


# 시간표 유효성 검사 및 추가
def is_valid(schedule, course):
    """현재 시간표에 강의를 추가할 수 있는지 확인."""
    for day in course["days"]:
        for scheduled_course in schedule[day]:
            if not (course["end_time"] <= scheduled_course["start_time"] or
                    course["start_time"] >= scheduled_course["end_time"]):
                return False
    return True


# 강의 추가
def add_course_to_schedule(schedule, course, excluded_courses):
    if course["name"] in excluded_courses:
        return False
    for day in course["days"]:
        for scheduled_course in schedule[day]:
            if not (course["end_time"] <= scheduled_course["start_time"] or
                    course["start_time"] >= scheduled_course["end_time"]):
                excluded_courses.add(course["name"])  # 배제된 과목으로 추가
                return False
        schedule[day].append(course)
    return True


# GUI로 시간표 추가 및 출력
class ScheduleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("모범생 시간표 최적화 시스템")

        self.predefined_required_courses = [
            {"name": "전공A", "days": ["월", "수"], "start_time": 9, "end_time": 11, "credits": 3, "type": "전공", "required": True},
            {"name": "전공B", "days": ["화", "목"], "start_time": 10, "end_time": 12, "credits": 3, "type": "전공", "required": True}
        ]
        self.courses = []  # 입력된 강의 저장
        self.schedule = {day: [] for day in ['월', '화', '수', '목', '금']}

        # GUI 구성
        self.setup_gui()

    def setup_gui(self):
        # 필수 과목 안내
        self.info_text = tk.Text(self.root, width=80, height=5, wrap="word", state="normal")
        self.info_text.insert(
            "1.0",
            "필수 과목:\n- 전공A (월, 수 9-11), 3학점, 전공\n"
            "- 전공B (화, 목 10-12), 3학점, 전공\n\n"
            "위 필수 과목은 강의 이름만 입력하면 자동으로 추가됩니다.\n"
        )
        self.info_text.config(state="disabled")
        self.info_text.pack(pady=10)

        # 입력 프레임
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        # 강의 이름
        self.name_label = tk.Label(self.input_frame, text="강의 이름:")
        self.name_label.grid(row=0, column=0, pady=10)
        self.name_entry = tk.Entry(self.input_frame)
        self.name_entry.grid(row=0, column=1)

        # 강의 요일
        self.days_label = tk.Label(self.input_frame, text="강의 요일:")
        self.days_label.grid(row=1, column=0, pady=10)

        self.day_vars = {day: tk.IntVar() for day in ['월', '화', '수', '목', '금']}
        for i, (day, var) in enumerate(self.day_vars.items()):
            tk.Checkbutton(self.input_frame, text=day, variable=var).grid(row=1, column=i + 1, padx=5)

        # 시작 시간
        self.start_label = tk.Label(self.input_frame, text="시작 시간:")
        self.start_label.grid(row=2, column=0)
        self.start_entry = tk.Entry(self.input_frame)
        self.start_entry.grid(row=2, column=1)

        # 종료 시간
        self.end_label = tk.Label(self.input_frame, text="종료 시간:")
        self.end_label.grid(row=3, column=0)
        self.end_entry = tk.Entry(self.input_frame)
        self.end_entry.grid(row=3, column=1)

        # 학점
        self.credits_label = tk.Label(self.input_frame, text="학점:")
        self.credits_label.grid(row=4, column=0)
        self.credits_entry = tk.Entry(self.input_frame)
        self.credits_entry.grid(row=4, column=1)

        # 강의 유형
        self.type_label = tk.Label(self.input_frame, text="강의 유형:")
        self.type_label.grid(row=5, column=0)
        self.type_var = tk.StringVar(value="전공")
        tk.Radiobutton(self.input_frame, text="전공", variable=self.type_var, value="전공").grid(row=5, column=1)
        tk.Radiobutton(self.input_frame, text="교양", variable=self.type_var, value="교양").grid(row=5, column=2)

        # 필수 과목 여부
        self.required_label = tk.Label(self.input_frame, text="필수 과목 여부:")
        self.required_label.grid(row=6, column=0)
        self.required_var = tk.StringVar(value="n")
        tk.Radiobutton(self.input_frame, text="Yes", variable=self.required_var, value="y").grid(row=6, column=1)
        tk.Radiobutton(self.input_frame, text="No", variable=self.required_var, value="n").grid(row=6, column=2)

        # 버튼
        self.add_button = tk.Button(self.input_frame, text="강의 추가", command=self.add_course)
        self.add_button.grid(row=7, column=0, columnspan=3, pady=10)

        self.show_greedy_button = tk.Button(self.root, text="Greedy 시간표 보기", command=self.show_greedy_schedule)
        self.show_greedy_button.pack(pady=10)

        self.show_optimized_button = tk.Button(self.root, text="Backtracking 시간표 보기", command=self.show_optimized_schedule)
        self.show_optimized_button.pack(pady=10)

    def add_course(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("오류", "강의 이름을 입력하세요.")
            return
        predefined_course = next((course for course in self.predefined_required_courses if course["name"] == name), None)
        if predefined_course:
            self.courses.append(predefined_course)
            messagebox.showinfo("알림", f"필수 과목 {name}이 추가되었습니다.")
        else:
            try:
                days = [day for day, var in self.day_vars.items() if var.get()]
                start_time = int(self.start_entry.get())
                end_time = int(self.end_entry.get())
                credits = int(self.credits_entry.get())
                course_type = self.type_var.get()
                required = self.required_var.get() == 'y'
                new_course = {
                    "name": name,
                    "days": days,
                    "start_time": start_time,
                    "end_time": end_time,
                    "credits": credits,
                    "type": course_type,
                    "required": required
                }
                self.courses.append(new_course)
                messagebox.showinfo("알림", f"강의 {name}이 추가되었습니다.")
            except ValueError:
                messagebox.showerror("오류", "입력값이 올바르지 않습니다.")
        self.clear_entries()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.start_entry.delete(0, tk.END)
        self.end_entry.delete(0, tk.END)
        self.credits_entry.delete(0, tk.END)
        for var in self.day_vars.values():
            var.set(0)
        self.type_var.set("전공")
        self.required_var.set("n")

    def show_greedy_schedule(self):
        greedy_result = greedy_schedule(self.courses, max_credits=18)
        display_schedule_gui(greedy_result, calculate_credits, "Greedy 시간표")

    def show_optimized_schedule(self):
        initial_schedule = greedy_schedule(self.courses, max_credits=18)
        optimized_result = optimize_schedule(initial_schedule, self.courses, self.predefined_required_courses, max_credits=18)
        display_schedule_gui(optimized_result, calculate_credits, "Backtracking 시간표")


# GUI 실행
root = tk.Tk()
app = ScheduleApp(root)
root.mainloop()
