n = int(input())
student = list(map(int, input().split()))
student_line = []

for i in range(len(student)):
    student_line.insert(i - student[i], i+1)
print(*student_line)