n=int(input())
li=[]
for num in range(1,n+1):
    li.append(list(map(int,input().split())))
print(li)
sorted(li,reverse=False)
lx=[x[0] for x in li]
print(lx)
'''for num in range(len(li)):
    c=lx.count(li[num][0])
    if c>1:
        print(sorted(li[num:num+c]),reverse=True) '''
i=0
while i<len(li):
    c=lx.count(li[i][0])
    if c>1:
        for j in sorted(li[i:i+c],reverse=True):
            print(j[0],j[1])
        i+=c
    else:
        print(li[i][0],li[i][1])
        i+=1
