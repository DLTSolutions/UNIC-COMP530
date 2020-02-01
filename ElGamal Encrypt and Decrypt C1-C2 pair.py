# INPUT FOR ELGAMAL see sheets page 170
# ElGamal public key (p, g, h)
    # p=large prime
    # g=generator, primitive element modulo p
    # x=private key 1<x<p-1
    # h=g^x
# C1=g^k mod p
# C2=M*y^k mod p
    # M=message
    # h=Public Key
    # k=random number k<p
p=23
g=11
M=10
x=6
k=3

def main():
    # Compute public key h
    h=(g**x)%p
    print("Public Key h={}^{}mod{}={}".format(g,x,p,h))

    # Encrypt message using public key
    C1=(g**k)%p
    print("C1={}^{}mod{}={}".format(g,k,p,C1))
    C2=M*(h**k)%p
    print("C2={}*{}^{}mod{}={}".format(M,h,k,p,C2))
    print("Cipher=({},{})".format(C1, C2))

    # Decrypt cipher back to Message
    EncryptionKey=C1**x%p
    print("EncryptionKey={}^{}mod{}={}".format(C1,x,p,EncryptionKey))

    # The decryption key is the inverse of the EncryptionKey modulo p
    DecryptionKey=XmodY(EncryptionKey,p)
    print("The decryption key is the inverse of the EncryptionKey modulo p")
    print("DecryptionKey={}".format(DecryptionKey))
    DecryptedMessage=(C2*DecryptionKey)%p
    print("Decrypted Message={}*{}mod{}={}".format(C2,DecryptionKey,p,DecryptedMessage))

# Check on correctness
    if(M==DecryptedMessage):
        print("")
        print("The original message and the decrypted message are identical, so the protocol runs fine!")
        print("")
    elif(M!=DecryptedMessage):
        print("")
        print("The original message and the decrypted message are NOT THE SAME so the protocol is wrong!")
        print("")

def XmodY(x, y):
    if (y%x==0):
        print("not found")
    else:
        checksum = 1+y
        while (checksum %x != 0):
            checksum +=y
        inverse = checksum//x
        return inverse

if __name__ == "__main__":
    main()
