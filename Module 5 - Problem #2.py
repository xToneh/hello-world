#Antonio Perez
#November 3, 2020

#This program prints out numbers in a list on different lines and also the squared of each number.

list = [1, 2, 3, 4, 5]
print("List of Numbers.")
print(*list, sep = "\n")

print("Numbers squared.")
list2 = [1, 2, 3, 4, 5]
list2s = [number ** 2 for number in list2]

print(*list2s, sep = "\n")
