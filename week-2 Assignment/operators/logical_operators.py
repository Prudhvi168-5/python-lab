#Y.Prudhvi Naidu
#logical oprators
percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance %: "))
eligible = percentage > 75 and attendance > 90
print("Eligible for scholarship:", eligible)
# output
# Enter percentage: 76
# Enter attendance %: 92
# Eligible for scholarship: True