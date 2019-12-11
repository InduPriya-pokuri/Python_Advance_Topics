''' li=[1,2,3,4]
try:
    print("2nd element is ",li[1])
    print("5th element is ",li[4])
except IndexError:
    print("An error occured") 

def a_by_b(a,b):
    try:
        c=((a+b)/(a-b))
    except ZeroDivisionError:
        print("a/b results in 0")
    else:
        print(c)


a_by_b(int(input()),int(input())) '''



a=3
try:
    if a<4:
        b=a/(a-3)
        print("value of b is ",b)
except ZeroDivisionError:
    print("problem occured and solved")
