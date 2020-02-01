# ElGamal public key (p, g, h)
    # p=large prime
    # g=generator, primitive element modulo p
    # x=private key 1<x<p-1
    # h=g^x
p=97
g=8
h=33

def main():
    x=0
    while ((g**x)%p!=h):
        x+=1
        if (x==1000):
            print("Public key ({},{},{}) is NOT correct".format(p,g,h))
    print("Public key ({},{},{}) is correct for private key {}, since {}^{} mod {}={}".format(p,g,h,x, g, x, p, h))

if __name__ == "__main__":
    main()
