marks = int(input("Enter marks:"))

if marks > 80 and marks <= 100:
    print("You've got an A")
elif marks > 60 and marks <= 80:
    print("You've got a B")
elif marks > 40 and marks <= 60:
    print("You've got a C")
else:
    print("Sorry you failed")
