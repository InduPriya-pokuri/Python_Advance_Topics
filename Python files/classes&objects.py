''' class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p=person('IIIT',130417)
print(p.name)
print(p.age)

p2=person(input(),int(input()))
print("name is",p2.name)
print("age is",p2.age)

objects can also have methods and properties '''

class person_details:
    def __init__(obj,name,age):
        obj.name=name
        obj.age=age

    def my_return(abc):
        print("my name is ",abc.name)
        print("my age is",abc.age)

pd=person_details('hi',123)
''' pd.age=40 # we can update the object properties
pd.my_return() '''

del pd.age # we can delete the object properties
pd.my_return()
