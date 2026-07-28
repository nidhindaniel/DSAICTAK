#write a python program to find the sum of first n numbers using recursions
def sum_od_first(x):
    count=0
    if (x<=0) and (x>1000):
        print("Enter a valid Number")
    else:
        for i in range(x+1):
            count=count+i
        print(count)

n=int(input("Enter a number"))
sum_od_first(n)


