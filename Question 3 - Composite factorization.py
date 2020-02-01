import math

# Ask the user to fill in the number to check
numbertocheck = int(input("Enter a number greater than 3 to check: "))

# Check on input. All positive values below 4 are primes. Exclude also all negative numbers
if numbertocheck < 4:
    print(numbertocheck, "is not greater than 3. Please restart and provide a valid number")
    composite = False

# All other values are checked on prime numbers
else:
    sqrtnumber = math.ceil(math.sqrt(numbertocheck)) #number must be rounded up to the next integer else in error
    for i in range(2, sqrtnumber+1):
        if (numbertocheck % i) == 0: # If the Modulus operator returns 0 then it's not a prime but a composite number
            print("Nice", int(numbertocheck), "is a composite number, factorized by the below primes:")
            composite = True
            break
    else:
        print ("You've just entered a prime number")
        composite = False

if composite:
    # Print the first prime 2, the amount of times that numbertocheck can be divided leaving 0
    while numbertocheck % 2 == 0:
        print ("2")
        numbertocheck = numbertocheck / 2
		# numbertocheck is now an odd number. Continu to test from 3 until and including the sqrt of the number entered.
        # An increment of 2 is used as this is the minimal difference between two primes 
    for j in range(3,sqrtnumber+1,2):
        while numbertocheck % j== 0:
            print (j,)
            numbertocheck = numbertocheck / j
    if numbertocheck > 2: #print also the final remainder if this is a prime bigger than 2
        print (int(numbertocheck))