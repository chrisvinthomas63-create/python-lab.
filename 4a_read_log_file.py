# Program 4(a): Read and Display Contents of a Log File
with open("log.txt", "w") as file:
    file.write("System Started\n")
    file.write("User Logged In\n")
    file.write("System Closed\n")

with open("log.txt", "r") as file:
    print("Log File Contents:")
    print(file.read())
