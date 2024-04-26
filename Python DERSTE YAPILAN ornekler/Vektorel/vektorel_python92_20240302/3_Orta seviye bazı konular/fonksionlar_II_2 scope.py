# degisken = 11

# def fonksiyon1():
#     print(degisken)

# fonksiyon1()

# degisken = 11

# def fonksiyon1():
#     degisken = 22
#     print(degisken)

# fonksiyon1()

degisken = 11

def fonksiyon1():
    global degisken 
    degisken = 22
    print(degisken)

fonksiyon1()
print(degisken)