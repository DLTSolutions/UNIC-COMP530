smallnr = 49901708 #6208
bignr = 67612671 #4752
for i in range(1, smallnr+1):
    if((smallnr % i == 0) and (bignr % i == 0)):
        hcf=i
        if(i==1):
            print("Start finding HCF")
if(hcf==1):
    print ("hcf(", smallnr, ",", bignr,") =",hcf,"they are relatively prime") 
else:
    print ("hcf(", smallnr, ",", bignr,") =",hcf) 