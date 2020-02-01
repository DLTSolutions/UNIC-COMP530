def encrypt(string, shift):
 
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  return cipher
 
text = input("Enter text to encrypt: ")
s = int(input("Enter shift number: "))
print("Text after encryption: ", encrypt(text, s))

#I have added and subtracted 65 (for Uppercase) and 97 (for lowercase) in the formula because the ascii value of 
#‘A’ is 65 and of ‘a’ is 97. The ord() method is used to get the ascii value of the letters.