# Program 4(b): Store and Display Student Details Using Files
n = int(input("Enter number of students: "))

with open("students.txt", "w") as file:
    for i in range(n):
        name = input("Enter student name: ")
        usn = input("Enter USN: ")
        file.write(name + " " + usn + "\n")

with open("students.txt", "r") as file:
    print("\nStudent Details:")
    print(file.read())
