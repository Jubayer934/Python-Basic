'''
Stack= push and pop
'''
# Push
books=[]
books.append('bookOne')
books.append('BookTwo')
books.append('bookThree')
print(books)

# POP
books.pop()
print(books)
print(books[-1])

books.pop() # poping last two books
books.pop()
if not books: #not book is true
    print('No books there')


'''

Last in First out

'''