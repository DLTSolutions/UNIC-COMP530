# Euler’s Totient Function: Choose e where gcd(e,(p-1)(q-1))=1
# PROVIDE START VALUES. MAKE P AND Q 0 IF PHI IS KNOWN
e = 342952340      # This must be the SMALL number
phi = 4230493243    # This must be the BIG number
p = 0
q = 0
if p!=0:
    phi=(p-1)*(q-1)

# Initialize
numerator = phi
denominator = e
maxloops = phi - e

for i in range(1,maxloops+1):
    remainder = numerator % denominator
    if (remainder == 1):
        print ("gcd({},{})={}. They are Coprime".format(e, phi, remainder))
        break
    if (remainder == 0):
        print ("gcd({},{})={}".format(e, phi, denominator))
        print ("NOT COPRIME!!")
        break
    numerator = denominator
    denominator = remainder

    