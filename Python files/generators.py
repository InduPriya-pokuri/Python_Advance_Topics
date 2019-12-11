''' Generators are like normal functions but with keyword 'yield' as
return value
Defined with keyword 'def'
used to created iteratofs...

def generator_example():
    yield 1
    yield 2
    yield 3
    yield 4

for value in generator_example():
    print(value,end=" ") '''

def series(num):
    a,b=0,1
    while a<num:
        yield a
        a,b=b,a+b
    
s=series(4)
for num in s:
    print(num,end=" ")
for num in series(5):
    print(num,end=" ")
