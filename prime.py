num = int(input("enter a number: \n"))
print("\n")
if num == 2:
    print("2 is not a prime number because it is divisible by 2")
    
for i in range(2,num):
    if num % i == 0:
        print(num, "is not a prime number because it is divisble by", num//i)
        break
    else:
        print(num, "is a prime number")
        break
