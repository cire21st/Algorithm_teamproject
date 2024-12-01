# 유효한 시간 입력을 받을 때까지 반복

def get_valid_time(prompt):

    while True:

        try:

            time = int(input(prompt))

            if 0 <= time < 24:  # 24시간제 범위 확인

                return time

            else:

                print("⚠️ 시간은 0에서 23 사이의 숫자여야 합니다. 다시 입력하세요.")

        except ValueError:

            print("⚠️ 숫자를 입력해야 합니다. 다시 입력하세요.")



# 메인 함수

def main():

    print("모범생 시간표 최적화 시스템 (요일별)")

    print("===================================")



    # 필수 과목 사전 정의

    predefined_required_courses = [

        {"name": "전공A", "days": ["월", "수"], "start_time": 9, "end_time": 11, "credits": 3, "type": "전공", "required": True},

        {"name": "전공B", "days": ["화", "목"], "start_time": 10, "end_time": 12, "credits": 3, "type": "전공", "required": True}

    ]



    print("필수 과목:")

    for course in predefined_required_courses:

        print(f"- {course['name']} ({', '.join(course['days'])} {course['start_time']}-{course['end_time']}), "

              f"{course['credits']}학점, {course['type']}")

    print("\n위 필수 과목은 이름만 입력해도 자동으로 추가됩니다.\n")



    # 사용자 입력으로 강의 데이터 추가

    courses = []

    while True:

        print("강의를 입력하세요 (종료하려면 'done' 입력):")

        name = input("강의 이름 (예: 교양A, 전공A): ")

        if name.lower() == 'done':

            required_courses = [course for course in courses if course["required"]]

            if not required_courses:

                print("❌ 필수 과목이 없습니다. 필수 과목을 최소 하나 이상 추가하세요.\n")

                continue  # 필수 과목 없으면 다시 입력

            break



        # 필수 과목 자동 추가

        predefined_course = next((course for course in predefined_required_courses if course["name"] == name), None)

        if predefined_course:

            courses.append(predefined_course)

            print(f"⚠️ 필수 과목 {name}이 자동으로 추가되었습니다.\n")

            continue



        # 일반 강의 입력

        days = input("강의 요일 (예: 월화수, 쉼표로 구분): ").split(',')

        start_time = get_valid_time("강의 시작 시간 (24시간제, 예: 9): ")

        end_time = get_valid_time("강의 종료 시간 (24시간제, 예: 11): ")



        if end_time <= start_time:  # 시작 시간과 종료 시간의 논리적 검증

            print("⚠️ 종료 시간은 시작 시간보다 늦어야 합니다. 다시 입력하세요.")

            continue



        credits = int(input("학점: "))

        course_type = input("강의 유형 (전공/교양): ").strip()

        required = input("필수 과목 여부 (y/n): ").strip().lower() == 'y'

        courses.append({

            "name": name,

            "days": days,

            "start_time": start_time,

            "end_time": end_time,

            "credits": credits,

            "type": course_type,

            "required": required

        })

        print("강의가 추가되었습니다.\n")



    # 필수 조건 설정

    min_total_credits = 12  # 최소 이수 학점

    max_credits = 18  # 최대 신청 가능 학점



    # Greedy 알고리즘으로 초기 시간표 생성

    def greedy_schedule(courses):

        # "전공 > 필수 과목 여부(Y) > 학점 > 교양" 우선순위로 정렬

        sorted_courses = sorted(

            courses,

            key=lambda x: (

                x["type"] == "교양",         # 전공 우선

                not x["required"],          # 필수 과목 우선

                -x["credits"],              # 학점 높은 과목 우선

                x["end_time"]               # 빨리 끝나는 과목 우선

            )

        )

        schedule = {day: [] for day in ['월', '화', '수', '목', '금']}

        total_credits = 0



        for course in sorted_courses:

            if add_course_to_schedule(schedule, course):

                total_credits += course["credits"]

                if total_credits >= max_credits:

                    break



        return schedule



    # 시간표에 강의를 추가할 수 있는지 확인하고 추가

    def add_course_to_schedule(schedule, course):

        for day in course["days"]:

            for scheduled_course in schedule[day]:

                # 시간 충돌 확인

                if not (course["end_time"] <= scheduled_course["start_time"] or course["start_time"] >= scheduled_course["end_time"]):

                    return False

            # 추가

            schedule[day].append(course)

        return True



    # Backtracking으로 최적화

    def optimize_schedule(initial_schedule, courses):

        # 필수 과목을 입력된 강의에 추가

        courses += [course for course in predefined_required_courses if course not in courses]



        best_schedule = initial_schedule

        best_credits = calculate_credits(initial_schedule)[0]



        def backtrack(current_schedule, current_credits, index):

            nonlocal best_schedule, best_credits



            # 필수 과목 포함 여부 확인

            if meets_requirements(current_schedule) and current_credits > best_credits:

                best_schedule = {day: current_schedule[day][:] for day in current_schedule}

                best_credits = current_credits



            # 최대 학점 도달 시 종료

            if current_credits >= max_credits:

                return



            # 모든 강의를 탐색

            for i in range(index, len(courses)):

                course = courses[i]

                if add_course_to_schedule(current_schedule, course):

                    current_credits += course["credits"]

                    backtrack(current_schedule, current_credits, i + 1)

                    current_credits -= course["credits"]

                    for day in course["days"]:

                        current_schedule[day].remove(course)



        # Backtracking 시작

        initial_credits = calculate_credits(initial_schedule)[0]

        backtrack(initial_schedule, initial_credits, 0)

        return best_schedule



    # 필수 조건 확인 함수

    def meets_requirements(schedule):

        total_credits, major_credits, general_credits = calculate_credits(schedule)

        included_required_courses = all(

            any(course in schedule[day] for day in schedule if course in predefined_required_courses)

            for course in predefined_required_courses

        )



        # 필수 과목 포함 여부

        if not included_required_courses:

            return False

        # 최소 학점 충족 여부

        if total_credits < min_total_credits:

            return False

        return True



    # 학점 계산 함수

    def calculate_credits(schedule):

        total_credits = 0

        major_credits = 0

        general_credits = 0



        for day_courses in schedule.values():

            for course in day_courses:

                total_credits += course["credits"]

                if course["type"] == "전공":

                    major_credits += course["credits"]

                elif course["type"] == "교양":

                    general_credits += course["credits"]



        return total_credits, major_credits, general_credits



    # 결과 출력 함수

    def print_schedule(schedule):

        total_credits, major_credits, general_credits = calculate_credits(schedule)

        print(f"총 학점: {total_credits}")

        print(f"전공 학점: {major_credits}/60")

        print(f"교양 학점: {general_credits}/30")

        for day in ['월', '화', '수', '목', '금']:

            print(f"{day}:")

            for course in schedule[day]:

                print(f"  {course['name']} ({course['start_time']}-{course['end_time']}, {course['credits']}학점, {course['type']})")

        print("\n")



    # Greedy로 초기 시간표 생성

    initial_schedule = greedy_schedule(courses)



    # Backtracking으로 최적화

    optimized_schedule = optimize_schedule(initial_schedule, courses)



    # 출력

    print("\n초기 시간표 (Greedy):")

    print_schedule(initial_schedule)



    print("최적화된 시간표 (Backtracking):")

    print_schedule(optimized_schedule)



if __name__ == "__main__":

    main()


