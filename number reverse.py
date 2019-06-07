a=int(input())
k=0
while(a>0):
  m=int(a%10)
  k = int((k*10) +(m))
  a = int(a/10)
print (k)
