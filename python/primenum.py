a=int(input("Enter a number:"))
b=a**0.5
c=int(b+1)
for i in range(2,c):
    if(a%i==0):
        print("it is a prime number")
    else:
        print("it is not a prime number")