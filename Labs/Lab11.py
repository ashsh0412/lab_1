import matplotlib.pyplot as plt
import os
import math

path = "/Users/sungho/Documents/coding_class/data/submissions"

def get_assignment(assignment_id, score_rate):
    file_name = 'data/assignments.txt'
    with open(file_name, 'r') as f:
        lines = []
        for line in f:
            lines.append(line.strip())  # 각 줄에서 공백 제거 후 리스트에 추가

    assignment_score = []
    for i in range(0, len(lines), 3):  # 3줄씩 묶기
        group = lines[i:i + 3]  # 슬라이싱으로 그룹 생성
        if assignment_id == group[1]:
            result = int(group[2]) * score_rate * 0.01
            assignment_score.append(result)

    return assignment_score

def get_submissions(student_id):
    file_list=os.listdir(path)
    file_list_txt = [file for file in file_list if file.endswith(".txt")]

    filtered_value = []

    for i in file_list_txt:
        file_name = f"data/submissions/{i}"
        f = open(file_name, 'r')
        lines = f.readlines()

        for line in lines:
            line = line.strip()
            lined = line.split("|")
            if lined[0] == student_id:
                filtered_value.append(lined)
    return (filtered_value)

def get_student(name):
    file_name = 'data/students.txt'
    f = open(file_name, 'r')
    lines = f.readlines()

    filtered_name = []

    for line in lines:
        line = line.strip()
        line1 = line[:3]
        line2 = line[3:]

        if name == line2:
            filtered_name.append(line1)
            filtered_name.append(line2)

    return filtered_name

def get_assignment_statistics(assignment_name):
    file_name = 'data/assignments.txt'
    with open(file_name, 'r') as f:
        lines = []
        for line in f:
            lines.append(line.strip())

    for i in range(0, len(lines), 3):  # 3줄씩 묶기
        group = lines[i:i + 3]  # 슬라이싱으로 그룹 생성

        if group[0] == assignment_name:

            file_list=os.listdir(path)
            file_list_txt = [file for file in file_list if file.endswith(".txt")]

            filtered_values = []

            for i in file_list_txt:
                file_name = f"data/submissions/{i}"
                f = open(file_name, 'r')
                lines = f.readlines()

                for line in lines:
                    line = line.strip()
                    lined = line.split("|")
                    if lined[1] == group[1]:
                        filtered_values.append(lined)
        
    
            scores = []
            for filtered_value in filtered_values:
                scores.append(int(filtered_value[2]))
            min_value = (min(scores))
            max_value = max(scores)
            avg_value = int(math.floor(sum(scores)/ len(scores)))
            return min_value, max_value, avg_value, scores

def main():
    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")
    inputValue = int(input("Enter your selection: "))

    if inputValue == 1:
        nameValue = input("What is the student's name: ")
        a = get_student(nameValue)
        if a:
            b = get_submissions(a[0])
            total_grades = []
            for i in b:
                a = get_assignment(i[1], int(i[2]))
                total_grades.append(a)
            total_grades = sum(total_grades, [])
            sum_score = sum(total_grades)
            avg_grade = sum_score * 0.1
            print(f"{int(math(avg_grade, 0))}%")
        else:
            print("Student not found")
    
    if inputValue == 2:
        assignmentValue = input("What is the assignment name: ")
        a = get_assignment_statistics(assignmentValue)
        if a:
            print(f"Min: {a[0]}%")
            print(f"Avg: {a[2]}%")
            print(f"Max: {a[1]}%")
        else:
            print("Assignment not found")

    if inputValue == 3:
        assignmentValue = input("What is the assignment name: ")
        a = get_assignment_statistics(assignmentValue)
        print(a[3])
        plt.hist(a[3], cumulative=False)
        plt.show()


main()