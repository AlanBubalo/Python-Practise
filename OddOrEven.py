num = int(input("Enter a number: "))
check = int(input("Enter another number: "))
if num % check == 0:
    print(str(num) + " is evenly divided by " + str(check))
elif num % 2 == 0:
    if (num % 4 == 0):
        print (str(num) + " is divideable by 4")
    else:
        print(str(num) + " is an even number")
else:
    print(str(num) + " is an odd number")