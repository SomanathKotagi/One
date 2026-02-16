

 
y=lambda b:b*10
print(y(5))

z=lambda c:c/10
print(z(56))

t=lambda e:e/10
print(t(6))

lmb=lambda a,b,c:a+b+c
print(lmb(3,4,5))



##Power of lambda Function
def powerlam(n):
    return lambda a,b:(a+b)*n

mypower=powerlam(5)
print(mypower,"This is passing parameter to the function")

print(mypower(5,2),"This is passing the values to the lambda function to get the result back from the value")

##Reusing the function
print("Reusing the function ",mypower(3,2))

def getnumbers(numbers):
    return numbers
## Combining the map with lambda function
numbers=["Apple","Mango","Orange","Grapes"]
print(list(map(getnumbers,(numbers))))


#lambda
result=list(map(lambda x:x.lower(),numbers))
print(result)

val=[1,2,3,4,5,6]
print(list(map(lambda y:y *2,val)))


print(list(map(lambda x:x*3,val)))
print(val[4])



val_filter=[1,2,3,4,88,6,45,1,25]
print("Using filter",val_filter)
print(list(filter(lambda val_fil:val_fil%2==0,val_filter)))


students=[("Somanath",23),("Pratik",45),("Snehal",24),("Prajwal",46)]
sorted_students=sorted(students,key=lambda x:x[1])

print(sorted_students)

str_numbers=['1','2','3','4','5']
int_numbers=list(map(int,str_numbers))

print(type(int_numbers))
print(type(int_numbers[2]))