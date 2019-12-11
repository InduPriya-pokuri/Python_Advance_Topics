li=list(map(int,input().split()))
li.sort()
min_part=li[:4]
max_part=li[-5:]
min_sum=sum(min_part)
max_sum=sum(max_part)
print(min_sum,max_sum)
