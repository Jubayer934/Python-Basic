# Class
class student:
    roll=""
    gpa=""


# Object 1
sakib = student()
print(isinstance(sakib,student))
sakib.roll = 101
sakib.gpa = 3.70
print(f"Roll = {sakib.roll} , gpa = {sakib.gpa}")

# Object 2
rakib = student()
rakib.roll = 102
rakib.gpa = 4.70
print(f"Roll = {rakib.roll} , gpa = {rakib.gpa}")