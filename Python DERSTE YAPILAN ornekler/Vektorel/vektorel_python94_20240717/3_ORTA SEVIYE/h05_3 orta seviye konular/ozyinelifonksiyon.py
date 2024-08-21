# temel kullanım
def sayac():
    i = 0;
    while True: 
        yield i; 
        i += 2


say = sayac()        
# say = sayac()        
# print(*say)
for a in range(5): 
    print(next(say))

# def myFunc():
#     yield "Hello"
#     yield 51
#     yield "Good Bye"

# x = myFunc()

# # print(x)
# for z in x:
#   print(z)