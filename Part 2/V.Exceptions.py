'''
Run time error
'''

try:
    list=[2,0,4]
    result= list[0]/list[1]
    result2= list[0]/list[3]
    print('Done')
except ZeroDivisionError:
    print("by Zero divide not possible")
except IndexError:
    print('IndexError')
except EOFError:
    print('when user not give any input')
finally :
    print("must print")




'''

int error

user input zero input error

'''
