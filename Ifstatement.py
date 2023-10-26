num = int(input("Enter number:"))
num2=int(input("Enter to check od or even:"))

if num>=0:
    print(f"{num} is positive number")
else:
    print(f"{num} is negative")
if num2 %2==0:
    print(f"{num2} is Even")
else:
    print(f"{num2} is odd")
