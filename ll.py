listem=([2,4,"kötü"],[3,6,"iyi"],[3,4,"iyi"],[4,10,"kötü"],[5,8,"kötü"],[6,3,"iyi"],[7,9,"iyi"],[9,7,"kötü"],[11,7,"kötü"],[10,2,"kötü"])


from array import*
import math

x1=float(input('sayı girin:'))
x2=float(input('sayı girin:'))


def öklid(a,b):
    uzaklık=float(math.sqrt((math.pow(x1-a,2)+math.pow(x2-b,2))))
    return uzaklık


i=0
j=0
uzaklıklar=[]
while i<len(listem):  
    x=öklid(listem[i][0],listem[i][1])
    y=[x,listem[i][2]]
    uzaklıklar.append([x,listem[i][2]])
    i+=1

k=4
i=0
minUzaklık=[]

while j<k:
    mini=min(uzaklıklar)
    indeks=uzaklıklar.index(mini)
    minUzaklık.append(mini)
    uzaklıklar.pop(indeks)
    j+=1

m=0
iyi=0
kötü=0
while m<len(minUzaklık):
    if minUzaklık[m][1]=="iyi":
        iyi+=1
    else:
        kötü+=1    
    m+=1
    
print(minUzaklık)
    
if iyi>kötü:
    print("veri setine göre girdiğiniz değerlere uygun etiket = iyi")
else:
    print("veri setine göre girdiğiniz değerlere uygun etiket = kötü")
    


         