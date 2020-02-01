# Pick any plaintext you would like to encrypt it using the public key (937513, 638471) and then check correctness of the algorithm
message="COMP-530 has a very nice assignment to work on"
p=877       # Calculated with the factorization algorithm of question 3
q=1069      # Calculated with the factorization algorithm of question 3
e=638471    # The value of e has been verified on correctness using the EA of question 4
# Step 1 Calculate n and phi
n=p*q
phi=(p-1)*(q-1)
# Step 2 Calculate d so that e*d mod phi = 1, or e*d=1mod phi. Construct a table with three rows and two columns and initialize it with below values
r1c1=r1c2=phi
r2c1=e
r2c2=1
# Loop until d has been found, so when the value in row 3 column 1 (r3c1) equals 1
d=0
while (d==0):
    temp=r1c1//r2c1 # Calculate a temporary value rounded to an integer
    r3c1 = r1c1-(temp*r2c1)
    r3c2 = r1c2-(temp*r2c2)
    if(r3c1<0):
        r3c1 %= phi
    if(r3c2<0):
        r3c2 %= phi
    if(r3c1==1):
        d=r3c2
    r1c1=r2c1
    r2c1=r3c1
    r1c2=r2c2
    r2c2=r3c2
# All info is available so let's encrypt and decrypt
print("Message:",message)
cipher = [(ord(char) ** e) % n for char in message]
print("Encrypted Message:",cipher)
decryptednumbers = [chr((char ** d) % n) for char in cipher]
decryptedmessage = ''.join(decryptednumbers)
print("Decrypted Message:",decryptedmessage)
print("RSA Public key:({},{}) has been used for encryption. RSA Private key:({},{}) has been used for decryption".format(n,e,n,d))

