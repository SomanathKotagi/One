def myfunc(n):
    return len(n)
print(list(map(myfunc,('apple','mango'))))


def square(r):
    return 3.14*r*r
print(square(6))

def liststring(name):
    return name;

print(list(map(liststring,("Somanath","Anish","Prajwal","Prasad","Vijay","Pravin","Karthik","Mahesh"))))

def morethantwo(names):
    return names

print(tuple(map(morethantwo,[['Somanath','Kotagi','Suraj','Patil','Balkrishna','Arjunwadkar','Priiya Raut'],['Darshan Raut','Nilesh Somanache','Shivam ','Suryakant']])))

