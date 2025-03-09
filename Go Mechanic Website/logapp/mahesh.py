a=[2,9,4,0,1,28,14]
for i in range(0,len(a)):
    for j in range(0,len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)