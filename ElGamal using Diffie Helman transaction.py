#INPUT FOR ELGAMAL
N=97    #prime modulus
a=8	    #special number, primitive element modulo N or simply generator (public base)
p=71	#message
s=15	#private key Alice, 1 < s < N-1
r=2	    #private key Bob, 1 < r < N-1

def main():
    print("All steps for encryption and decryption using the ElGamal algorithm")
    print("********************************************************************************************")
    print("Message p={}, public base a={} and modulus N={}".format(p,a,N))
    print("Alice: Choose random number s={}. This is her private key".format(s))
    print("Bob: Choose random number r={}. This is his private key".format(r))
    AliceNr=(a**s)%N
    print("Alice: Computes {}^{} mod {}. {}^{} mod {} ≡ {}".format(a,s,N,a,s,N,AliceNr))
    BobNr=(a**r)%N
    print("Bob: Computes {}^{} mod {}. {}^{} mod {} ≡ {}".format(a,r,N,a,r,N,BobNr))
    print("Alice: Sends her number {} to Bob. ".format(AliceNr))
    print("Bob: Sends his number {} to Alice.".format(BobNr))
    EncryptionKeyBob=(AliceNr**r)%N
    print("Bob: Computes the encryption key using the number of Alice: {}^{} mod {} ≡ {}".format(AliceNr,r,N,EncryptionKeyBob))
    Cipher=(EncryptionKeyBob*p)%N
    print("Bob: Encrypt the message. Cipher ≡ {}*{} mod {} ≡ {} mod {} ≡ {}".format(EncryptionKeyBob,p,N,EncryptionKeyBob*p,N,Cipher))
    print("Bob: Sends the encrypted message {} to Alice".format(Cipher))
    EncryptionKeyAlice=(BobNr**s)%N
    print("Alice: Computes the encryption key using the number of Bob: {}^{} mod {} ≡ {}".format(BobNr,s,N,EncryptionKeyAlice))
    DecryptionKey= XmodY(EncryptionKeyAlice, N)
    print("Alice: Find the decryption key. This is the inverse of {}.".format(EncryptionKeyAlice))
    print("Alice: Find {} mod {} with the python program. X={}, Y={}. The decryption key is {}".format(EncryptionKeyAlice,N,EncryptionKeyAlice,N,DecryptionKey))
    DecryptedMessage=(Cipher*DecryptionKey)%N
    print("Alice: Decrypt the cipher. The decrypted message ≡ {}*{} mod {} ≡ {} mod {} ≡ {}".format(Cipher,DecryptionKey,N,Cipher*DecryptionKey,N,DecryptedMessage))
    if(p==DecryptedMessage):
        print("")
        print("The original message and the decrypted message are identical, so the protocol runs fine!")
        print("")
    elif(p!=DecryptedMessage):
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
