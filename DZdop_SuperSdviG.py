n=int(input('сколько  '))
list1= range(1,n)
k=int(input('Введите на сколько'))
res=[0]*n
k=k%n
if k<0:
    k=-k
for i in range(k):
    res[i]=list[n-k+i]
for i in range(n-k):
    res[k+i]= list1[i]

print(res)