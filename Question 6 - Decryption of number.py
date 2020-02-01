# based on the video: https://www.youtube.com/watch?v=Z8M2BTscoD4
# Write a program to convert an encrypted number c = m^e (mod n) into the original m = c^d (modn), where 0 < m < n is some integer
number=5
p=7
q=13
# Step 1 Calculate n and phi
n=p*q
phi=(p-1)*(q-1)
# Step 2 Select e so that phi and e don't share a factor and e must be >2
e=5
cipher=(number**e)%n
print("Cipher:",cipher)
# Step 3 Calculate d so that e*d mod phi = 1, or e*d=1mod phi. Construct a table with three rows and two columns and initialize it with below values
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
# Step 4 convert the cipher text back into the original text m = cypher^d (modn)
decryptednumber=(cipher**d)%n
print("Number to encrypt:{}, Decrypted number:{}".format(number,decryptednumber))
print("RSA Public key:({},{}) has been used for encryption. RSA Private key:({},{}) has been used for decryption".format(n,e,n,d))

