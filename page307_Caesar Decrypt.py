cipher = input("enter cipher:")
original = ''
for shift in range(1, 26):
    for char in cipher: 
        if char == ' ':
            original = original + char
        elif  char.isupper():
            original = original + chr((ord(char) - shift - 65) % 26 + 65)
        else:
            original = original + chr((ord(char) - shift - 97) % 26 + 97)
    print("shift",shift,"Original message:",original)
    original = ''

#I have added and subtracted 65 (for Uppercase) and 97 (for lowercase) in the formula because the ascii value of 
#‘A’ is 65 and of ‘a’ is 97. The ord() method is used to get the ascii value of the letters.

