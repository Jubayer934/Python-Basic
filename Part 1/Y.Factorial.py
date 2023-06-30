def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

a=int(input('Now give a number for factorial = '))

print(f"Factorial of {a} is = {fact(a)}")