cubes=[i**4 for i in range (12)]
print(cubes)

term=int(input("enter the term"))
if term%2==0:
   term=term//2
   print((3**term-1))
else:
    term=term//2+1
    print((2**term-1))
       
term=int(input("enter the term"))
if term%2==0:
   term=term//2
   print((6**term-1))
else:
    term=term//2+1
    print((7**term-1))    
       