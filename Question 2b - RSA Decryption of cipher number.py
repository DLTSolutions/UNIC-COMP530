# Write a program to convert an encrypted number c = m^e (mod n) into the original m = c^d (modn), where 0 < m < n is some integer
cipher=5
p=7
q=13
n=p*q
phi=(p-1)*(q-1)
e=5
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
# Step 4 convert the cipher text back into the original text m = cipher^d mod n
decryptednumber=(cipher**d)%n
print("Number to decrypt:{}, Decrypted number:{}".format(cipher,decryptednumber))
print("RSA Private key:({},{}) has been used for decryption".format(n,d))
print("Double check with formula {}^{} MOD {} = original number. Original number ={}".format(cipher,d,n, decryptednumber))

