# ElGamal public key (p, g, h)
    # p=large prime
    # x=private key 1<x<p-1
p=23
x=6
C1=20
C2=22

def main():
    # Step 1 Find encryption key from C1
    EncryptionKey=C1**x%p
    print("EncryptionKey=C1^x mod p={}^{}mod{}={}".format(C1,x,p,EncryptionKey))

    # The decryption key is the inverse of the EncryptionKey modulo p
    DecryptionKey=XmodY(EncryptionKey,p)
    print("The decryption key is the inverse of the EncryptionKey modulo p")
    print("DecryptionKey={}".format(DecryptionKey))
    DecryptedMessage=(C2*DecryptionKey)%p
    print("Decrypted Message={}*{}mod{}={}".format(C2,DecryptionKey,p,DecryptedMessage))

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
