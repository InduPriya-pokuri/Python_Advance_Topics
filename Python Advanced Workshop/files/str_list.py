'''st=list(map(int,input().split("+")))
print(st)
'=li=[]
for num in st:
    if num%2==0:
        li.append(chr(num))
print(li) 

char=[chr(num) for num in st if num%2==0]
print(char) 


def is_prime(n):
    count=0
    for num in range(1,n+1):
        if n%num==0:
            count+=1
    if count==2:
        return True
    else:
        return False
    


lw=int(input("Enter lower bound:"))
up=int(input("Enter upper bound:"))
for num in range(lw,up+1):
    if is_prime(num):
        print(num,end=" ")   

for num in range(lw,up+1):
    count=0
    for dig in range(1,num+1):
        if num%dig==0:
            count+=1
    if count==2:
        print(num,end=" ")
    num+=1

    '''

def is_prime(n):
    count=0
    for i in range(1,n//2+1):
        if n%i==0:
            count+=1
    if count==1:
        return True
    else:
        return False

lw=int(input("Enter lower bound:"))
up=int(input("Enter upper bound:"))
li=[num for num in range(lw,up+1) if is_prime(num)]
print(li)
