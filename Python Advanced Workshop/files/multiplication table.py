''' n=int(input("Enter a number:"))
for i in range(1,11):
    print(n,'*',i,'=',n*i)
n2=int(input("Enter the number:"))
mul=[print(n2,'*',i,'=',n2*i) for i in range(1,11)]
print(mul) '''



dic={'int':123,'float':87.67,'str':'name'}
#print(dic)
dic2={'st':'name',id:238,'cgpa':8.7}
#print(dic2)

'''print(dic.keys())
print(dic.values())
print(dic.items())
for key,val in dic.items():
    print(key,val,sep=" ")

l=[]
l.append(dic)
l.append(dic2)
for key,val in dic.items():
    print(key,val,sep=",")

for s in l:
    for key,value in s.items():
        print(key,value,sep=':')

print()
for key,val in zip(dic.items(),dic2.items()):
    print(key,val,sep=",")

dic={}
st=input()
for ch in st:
    dic[ch]=ord(ch)
print(dic)

dic2={ch:ord(ch) for ch in st if ord(ch)%2==1}
print(dic2)  '''

def is_perfect(n):
    s=0
    for num in range(1,n):
        if n%num==0:
            s+=num
    if s==n:
        return True
    else:
        return False


dic={num:num**2 for num in range(1,200) if is_perfect(num)}
print(dic)

