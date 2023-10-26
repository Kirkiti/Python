# list
mylist = ["Erick", "Joan", "Mercy", "Daniel", "Gloria", "Brian"]
mylist2 = [89, 12, 34, 8, 1, 17, 9, -3, -19]
mylist2.sort()
mylist.sort()

print(mylist)
print(f"My name is {mylist[0]}")
print("My name is" + mylist[0])
print(f"My sorted list {mylist2}")

# turple immutable ordered
my_turple = ("Kenya", "Uganda", "Tanzania", "Ethiopia", "Burundi", "Somalia")
# my_turple[2] =congo
print(my_turple)
print(f"My country is {my_turple[0]}")

# set unordered

fruits = {"Oranges", "Pineapples", "Mangoes", "Banana", "Apples"}
print(fruits)

# dictionaries
employees={"Name":"Erick", "Age":30, "Gender": "Male", "Salary":20000}

print("employees name: %s"% employees["Name"])
print("employees age: %d"% employees["Age"])
print("employees gender: %s"% employees["Gender"])
print("employees salary: %d"% employees["Salary"])

