def voter (age):
    if age>19:
        return 'You are allowed to vote'
    else:
        raise ValueError("Invalid Voter")


try:
    print(voter(20))
    print(voter(15))
except ValueError as e:
    print(e)