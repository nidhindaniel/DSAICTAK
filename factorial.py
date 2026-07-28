#factorial using while loop

count=1
n=int(input("Enter the Number"))
while n>0:
    for i in range(1,n+1):
        count=count*i
    print(count)
    break

       
print(count)

