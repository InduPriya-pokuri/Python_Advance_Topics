''' def prime(n):
    i=2
    while(i*i<=n):
        if n%i==0:
            return False
        i+=1
    return True

li=[n for n in input("enter chars:").split() if prime(ord(n))]
print(li)   '''
def prime(n):
    i=2
    while(i*i<=n):
        if n%i==0:
            return False
        i+=1
    return True
s=input().split()
a=[i for i in s if(prime(ord(i)))]
print(a)
