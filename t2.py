num=int(input("Enter a Year: "))
def leap_or_not(num):
    if (num % 4 == 0 ) or (num % 400 == 0):
        
        print(f"{num} is a Leap Year.")
    else:
        print(f"{num} is not a Leap Year.")

leap_or_not(num)
