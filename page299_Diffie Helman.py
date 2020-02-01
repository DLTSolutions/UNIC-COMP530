privatekey_A=7
privatekey_B=8
prime=71
g=7

Alice_key=(((g**privatekey_B)%prime)**privatekey_A)%prime
Bob_key=(((g**privatekey_A)%prime)**privatekey_B)%prime
print ("Alice_key:",Alice_key,"Bob_key:",Bob_key)
#OUTPUT: Alice_key: 32 Bob_key: 32

