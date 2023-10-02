print("String işlemleri")
print("================")
a = input ("Metin giriniz:")
for b in range (1,len(a)+1):
    print(a[0:b]," "*(len(a)-b),"|"," "*(len(a)-b),a[0:b])
