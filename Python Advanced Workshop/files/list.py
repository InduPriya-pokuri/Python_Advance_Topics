'''li=[]
for num in range(1,51):
    if num%2==0:
        li.append(num)
print(li)

li=[num for num in range(1,51) if num%2==0]
print(li)

odd=[num*num for num in range(1,51) if num%2==1]
print(odd)  


def is_even(n):
    if n%2==0:
        return True
    else:
        return False

even=[num for num in range(1,51) if is_even(num)]
print(even) '''


