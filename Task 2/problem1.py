n = int(input())
students = []
for _ in range(n):
    name = input()
    score = float(input())
    students.append([name, score])
second_lowest_grade = sorted(set([score for name, score in students]))[1]
second_lowest_students = [name for name, score in students if score == second_lowest_grade]
for name in sorted(second_lowest_students):
    print(name)
