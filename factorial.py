#implement a python program to count even and odd numbers using fuynctions'

def check_count(list):
    count=0
    if len(list)== 0:
        print("emptylist")
    else:
        list.sort()
        length=len(list)

    #check_evennumbers
    for i in range(length):
        if i%2==0:
            count=count+i
    print(f"The count of even numbers in the list is {count}")

        else:
        print(f"The count of odd numbers is {length-count}")



    



l=[2,4,5,3,2]
check_count(l)