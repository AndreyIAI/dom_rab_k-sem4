#5 Febonachi
#
#[-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

list_1 = []
a0=0
a1=1
x=1
n=int(input())
for i in range(n+1):
    list_1.append(a0)
    x=a0+a1
    a0=a1
    a1=x
list2=[list_1[i]*(-1) ** (1+i) for i in range(len(list_1))][len(list_1):0:-1]
print(list2+list_1)