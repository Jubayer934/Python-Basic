try:
    num1=int(input("Enter a value = "))
    num2=int(input("Enter a value = "))
    result=num1/num2
    print(result)
except (ValueError,IndentationError):
    print('You have entered wrong index or zero')

finally:
    print('succesful')