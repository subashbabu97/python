i,j=input().split()
a=int(i)
b=int(j)
for x in range(a+1,b): 
  c=0
  for y in range(1,b):
    if(x%y==0):
      c=c+1
  if(c==2):
    print(x,end=" ")
