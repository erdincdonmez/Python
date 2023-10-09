try:
    d = open("deneme.py","x")
    d.write("deneme dosyasına yazılan")
    d.close()
except:
    print("deneme.py dosyası var")
