
n=int(input('Give the list range'))
subject=list(map(int,input().split()))[:n]
print(subject)


print(' '.join(map(str, subject)))

'''


Graph Input



'''

n=int(input())
graph=[]
elemants=[]
for i in range(n):
    elemants=list(map(int,input().split()))
    graph.append(elemants)
print(graph)