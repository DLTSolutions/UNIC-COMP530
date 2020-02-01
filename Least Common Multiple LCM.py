#The least common multiple of the positive integers a and b is the smallest positive integer that is divisible by both a and b
#INPUT FOR LCM
a=57
b=6

def main():
    print("The least common multiple LCM of the positive integers a and b is the smallest positive integer that is divisible by both a and b")
    print("*********************************************************************************************************************************")
    print("LCM({},{})={}".format(a,b,LCM(a,b)))
    
def LCM(x, y):
    if x > y: # choose the greater number
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

if __name__ == "__main__":
    main()
