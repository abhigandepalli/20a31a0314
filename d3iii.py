
#conversion into binary
b=(6>>+2)
print(bin(b))
#swaping by addtion and substraction      
a=10
b=20
a=a+b
b=a-b
a=a-b
print(a,b)

a=11
b=22
print("before swap")
print("a=",a)
print("b=",b)
a=a+b
b=b-a
a=a-b
print("after swap")
print("a=",a)
print("b=",b)

a=11
b=22
print("before swap")
print("a=",a)
print("b=",b)
a=a^b
b=b^a
a=a^b
print("after swap")
print("a=",a)
print("b=",b)
