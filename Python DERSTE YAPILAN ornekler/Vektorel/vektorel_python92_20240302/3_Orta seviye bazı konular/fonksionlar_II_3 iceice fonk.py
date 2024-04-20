a = 1
def selam():
    a = 2
    print ("merhaba",a)
    def sabah():
        global a
        a = 3
        print("günaydın",a)
    sabah()

selam()
print(a)
