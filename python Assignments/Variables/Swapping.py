a = 10
b = 20
print("Before swapping:", a, b)
temp = a
a = b
b = temp
print("After swapping:", a, b)
a = 10
b = 20
print("Before swapping:", a, b)
a, b = b, a
print("After swapping:", a, b)

#output
#Before swapping: 10 20
#After swapping: 20 10
#Before swapping: 10 20
#After swapping: 20 10
