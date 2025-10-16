numeros=int(input("quantos numeros:"))
primeiro=int(input("numero1:"))
count=1
maior=primeiro
soma=primeiro
while count<numeros:
      count+=1
      temp=int(input("numero %d: "% count))
      soma+=temp
if   temp>maior:
      maoir=temp
media=("soma:",soma)
print("soma: ",soma)
print("maior:",maior)
print("media:%.2f"%(soma/numeros))
