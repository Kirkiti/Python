# lits mutable
mylist = ["Joshua", "Caleb", "Kevin", "Elias", "Jason", "Jackson"]
mylist.sort()
print(mylist)
print(f"My name is {mylist[0]}")
mylist2 = [89, 78, 56, 9, 5, -3, -19]
mylist2.sort()
print(f"My sorted list {mylist2}")

# turple immutable ordered
my_tuple = ("Kenya", "Uganda", "Tanzania", "Ethiopia", "Somalia")
print(my_tuple)
print(f"My country is {my_tuple[0]}")

# set unordered
fruits = {"Oranges", "Mangoes", "Apples", "Banana", "Pineappples"}
print(fruits)

# dictionaries
employees = {"Name": "Eric", "Age": 30, "Gender": "Male", "Salary": 20000}
print("employees name :%s" % employees["Name"])
print("employees age:%d" % employees["Age"])
