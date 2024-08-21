ad = "global değişken"
def selamla():
    global ad
    ad ="ada"
    def sabah():
        global ad
        ad = "efe"
        print("Günaydın", ad)
    ad = "ali"
    print("Merhaba", ad)
    sabah()
    print("Nasılsın", ad)
    
selamla()
print("Son durum:",ad)
