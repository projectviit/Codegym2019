maximum_val=10**32
div=10000019
l=[]
def cal(m):
    

for j in range(0,33):
    l.append((10**j)%div)
def pal(n):
    sum1=0
    n=str(n)
    for k in range(len(n)):
        sum1=sum1+int(n[k])*l[k]
    if sum1%div==0:
        return 1
    else:
        return 0
sum=0

for i in range(11,maximum_val+1):
    k=str(i)
    c=int(k[::-1])
    k=int(k)
    if k==c and i%11==0:
        sum=sum+pal(i)
print(sum)