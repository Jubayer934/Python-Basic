# Class
class student:
    roll=""
    gpa=""

    def __init__(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa

    def display(self):
        print(f"Roll = {self.roll} , gpa = {self.gpa}")

# Object 1
sakib = student(101,3.70)
sakib.display()

# Object 2
rakib = student(102,4.70)
rakib.display()
