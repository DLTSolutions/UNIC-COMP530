import math

# Ask the user to fill in the number to check
numbertocheck = int(input("Enter the number to check: "))

# A prime number is always greater than 1 so exclude the others
if numbertocheck < 1:
    print(numbertocheck, "is less then 1 so not a prime number")

# All other values are checked on prime numbers
else:
    sqrtnumber = math.ceil(math.sqrt(numbertocheck)) #number must be rounded up to the next integer else in error
    for i in range(2, sqrtnumber):
        if (numbertocheck % i) == 0: # If the Modulus operator returns 0 then it's not a prime
            print("Unfortunately", numbertocheck, "is a composite number (not a prime) since it can also be divided by", i)
            break
    else:
        print("YES", numbertocheck, "is indeed a prime number")