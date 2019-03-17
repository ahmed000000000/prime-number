num = int(input("number: "))
if num>1:
  for i in range(2,num):
    if num % i == 0:
        print(num, "is not a prime number")
        break
    else:
        print(num, "is a prime number")
        break
else:
  print(num, "is not a prime numer")
  #if input is <1, not prime
  #else checks to see if num divisible by any number greater than 2
  # print prime
  # else if num>1 and not divisible by any num, print that num is a prime number
