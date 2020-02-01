smallnr = 499017086208
bignr = 676126714752

#Initialize
numerator = bignr
denominator = smallnr
maxloops = bignr - smallnr

for i in range(1,maxloops+1):
    remainder = numerator % denominator
    if (remainder == 1):
        print ("hcf({},{})={} so, they are relatively prime, or Coprime".format(smallnr, bignr, remainder))
        break
    if (remainder == 0):
        print ("hcf({},{})={}".format(smallnr, bignr, denominator))
        break
    numerator = denominator
    denominator = remainder

    