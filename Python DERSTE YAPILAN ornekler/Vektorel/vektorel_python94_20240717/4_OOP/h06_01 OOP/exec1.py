# x = 'name = "Vekörel "\nprint(name*3)'
# exec(x)
# # eval(x)

# program = "a = 'Ozancan'\nfor a in range (5):print(a)"
# exec(program)

a = open("deneme","w")
a.write("denemedd")
a = open("deneme","r")
b=a.read()
print(b)
