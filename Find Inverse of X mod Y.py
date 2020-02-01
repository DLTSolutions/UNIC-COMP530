# based on the video: https://www.youtube.com/watch?v=FnQNbFl72LY
# Find the inverse of x mod Y
x=6
y=12
if (y%x==0):
    print("No modular inverse")
else:
    checksum = 1+y
    print("Start with 1+{}".format(y))
    print("{}(mod {}) \u2260 0, so add Y ({})".format(checksum,x,y))
    while (checksum %x != 0):
        checksum +=y
        if (checksum %x != 0):
            print("{}(mod {}) \u2260 0, so add Y ({})".format(checksum,x,y))
    inverse = checksum//x
    print("{}(mod {}) = 0".format(checksum,x,x))
    print("{}={}*{} so, the Modular inverse of {} \u2261 {}(mod {})".format(checksum,x,inverse,x,inverse,y))

