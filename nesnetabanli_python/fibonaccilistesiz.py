#0,1,1,2,3,5,8,13,21,34,55,89
#a,b
#    c
#Fibonacci Serisi
#Listeli Hali

a=0
b=1
fibonacci=[a,b]
for i in range(1,10):
    c=a+b
    a=b
    b=c
    fibonacci.append(c)
print(fibonacci)
    
