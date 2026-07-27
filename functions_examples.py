def add(n):
    count = 0
    for i in range(n+1):
        count + i
    return count

n = int(input("Enter the range: "))
s = add(n)
print("The sum of the numbers is:", s)
