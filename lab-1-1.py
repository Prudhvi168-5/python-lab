#Y.Prudhvi Naidu
class Student:
    pass
def display():
    age = 20
    PI = 3.14
    user_name = "Prudhvi"
    print("Variable:", age)
    print("Constant:", PI)
    print("Underscore Name:", user_name)
display()
print("Class Name: Student")
print("Function Name: display")

# 1. 2value -> Invalid
#    Reason: Identifiers cannot start with a digit.
# 2. value_2 -> Valid
#    Reason: Starts with a letter and contains letters, digits, and underscore.
# 3. _hidden -> Valid
#    Reason: Identifiers can start with an underscore (_).
# 4. class -> Invalid
#    Reason: 'class' is a reserved keyword in Python.
# 5. my-var -> Invalid
#    Reason: Hyphen (-) is not allowed in identifiers.
# 6. MyClass -> Valid
#    Reason: Starts with a letter and follows Python identifier rules.
# 7. total$ -> Invalid
#    Reason: Dollar sign ($) is not allowed in Python identifiers.

# Python is case-sensitive
Marks = 95
marks = 80
print("Marks =", Marks)
print("marks =", marks)
