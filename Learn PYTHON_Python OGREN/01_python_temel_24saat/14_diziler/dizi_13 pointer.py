a = [2,4,1,6]
b = [3,2,5,1]
c = a
d = c[:]

print ("a: ",a)
print ("b: ",b)
print ("c: ",c)
print ("d: ",d)

c[1] = "h"
print ('\nc[1] = "h" sonrası')
print ("a: ",a)
print ("b: ",b)
print ("c: ",c)
print ("d: ",d)

d[1] = "k" 
print ('\nd[1] = "k" sonrası')
print ("a: ",a)
print ("b: ",b)
print ("c: ",c)
print ("d: ",d)

b[1] = "r" 
print ('\nb[1] = "r" sonrası')
print ("a: ",a)
print ("b: ",b)
print ("c: ",c)
print ("d: ",d)

a[1] = "w"
print ('\na[1] = "w" sonrası')
print ("a: ",a)
print ("b: ",b)
print ("c: ",c)
print ("d: ",d)

