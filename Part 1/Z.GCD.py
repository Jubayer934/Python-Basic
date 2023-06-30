def FindGCD(x,y):
	while(y>0):
		r=x%y
		x=y
		y=r
	return x


a,b=map(int,input('Give two number for GCD = ').split())
print("The GCD of",a," and ",b,"is : ",end=" ")
print(FindGCD(a,b))