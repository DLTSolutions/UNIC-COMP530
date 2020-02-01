import math
# Work with temp values x and y such that N=X*Y,  
# Fermat algorithm states: N=X^2-y^2=(x+y)*(x-y) --> So x^2=n+y^2
# Find x=sqrt(n+y^2) when looping y=1 to ..... x is found when it's an integer. Then p=x+y, q=x-y
# WORKS ONLY FINE IF p AND q ARE CLOSE TOGETHER
N=15

k=math.ceil(math.sqrt(N))
for y in range(1, k):
    x=math.sqrt(N+y*y)
    if int(x) == x:
        p=int(x+y)
        q=int(x-y)
        print("Number {} can be factorized into primes {} and {}. N=p*q {}={}x{}".format(N,p,q,N,p,q))
        break
    if y == math.ceil(math.sqrt(N)-1):
        print("No factorization for {}".format(N))