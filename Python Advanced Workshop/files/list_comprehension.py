'''n=int(input("Enter range:"))
li=[]
for i in range(1,n+1):
    num=int(input("Enter number:"))
    li.append(num)
print(li)
print("minimum elemnent ", min(li))
print("max element :", max(li))
s=0
for ele in li:
    s+=ele
print("sum value is ",s)
print("sum of the list ",sum(li))

if li.sort()!=None:
    li=li.sort()
print("sorted list :",li)
if li.reverse()!=None:
    li=li.reverse()
print("Reversed list :",li)  '''



