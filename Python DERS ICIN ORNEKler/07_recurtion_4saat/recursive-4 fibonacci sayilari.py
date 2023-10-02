# Fibonacci Dizisi (0 1 1 2 3 5 8 13 21 34 ...)
# Fibonacci dizisi elemanları önceki iki sayının toplamı şeklinde ilerler

def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

x = 10
print("Fibonacci dizisi:")
for i in range(x):
    print(fibonacci(i))
