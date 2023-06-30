# Class
class student:
    roll=""
    gpa=""

    def set_value(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa

    def display(self):
        print(f"Roll = {self.roll} , gpa = {self.gpa}")

# Object 1
sakib = student()
sakib.set_value(101,3.70)
sakib.display()

# Object 2
rakib = student()
rakib.set_value(102,4.50)
rakib.display()
