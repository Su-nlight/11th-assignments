def freq(lis,element):
 sum=0
 for x in lis:
    if x==element:
      sum+=1
    else:
      continue
 return sum
def dupl(lis):
 repeated = []
 for i in range(len(lis)):
   for j in range(i+1, len(lis)): 
    if lis[i] == lis[j] and lis[i] not in repeated: 
      repeated.append(lis[i]) 
 return repeated
