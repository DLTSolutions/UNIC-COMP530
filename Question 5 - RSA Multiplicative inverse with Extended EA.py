# based on the video: https://www.youtube.com/watch?v=Z8M2BTscoD4
phi=72
e=29
# Calculate d so that  e*d mod phi = 1, or e*d=1mod phi. Construct a table with three rows and two columns and initialize it with below values 
r1c1=r1c2=phi
r2c1=e
r2c2=1
# Loop until d has been found, so when the value in row 3 column 1 (r3c1) equals 1
d=0
while (d==0):
    # Calculate a temporary value
    temp=r1c1//r2c1 #rounded to an integer
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
print("{}*x=1 mod{}. x={}".format(e,phi,d))

