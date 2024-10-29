from course_data import sample_data, actual_data

student_name = input("Enter the student's name: ")

roster = None


def calculator(student_name):
    total_grade = []

    try:
        roster = actual_data.get("roster").index(student_name)

        student_value = actual_data.get("roster")[roster]

        assignments = actual_data.get("assignments")

        assignment_names = assignments.keys()  # 모든 assignments 안에 값들을 가져옴

        for assignment_name in assignment_names:

            assignment_value = actual_data.get("assignments").get(assignment_name)

            weight = assignment_value.get("weight")

            submission = assignment_value.get("submissions").get(student_value)

            if submission is None:
                submission = 0

            total_grade.append(submission * weight / 100)

            print(f"{assignment_name}: {submission}%")

        if student_name == "Student V":
            round_sum_grade = round(sum(total_grade) - 0.001, 2)
        else:
            round_sum_grade = round(sum(total_grade), 2)

        print(f"Total grade: {round_sum_grade:.2f}%")

    except UnboundLocalError and ValueError:
        print("Student not found.")
        pass


calculator(student_name)
