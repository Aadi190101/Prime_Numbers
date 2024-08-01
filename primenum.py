num = int(input("Enter a no:"))
# method-1
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "it is a prime number")
else:
    print(num, "is not a prime number")


# method-2
flag = False
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            flag = True
            print(i, "times", num // i, "is", num)
            break

    if flag:
        print(num, "it is not a prime number")
    else:
        print(num, "it is a prime number")
else:
    print(num, "is not a prime number")
