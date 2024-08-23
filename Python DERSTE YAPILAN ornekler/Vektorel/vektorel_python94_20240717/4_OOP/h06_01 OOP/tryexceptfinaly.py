b = 5000 # string olduğunda type error

try:
    a = int(input()) 
    # integer yerine string bir ifade girilirse value error verir
    print ((a+b)/0) # /0 "Bilinmeyen hata oluştu" der.
except ValueError:
    print ("Değer hatası oluştu.")
except TypeError:
    print ("Kardeşim doğru tip gir.")
except ZeroDivisionError:
    print ("Kardeşim 0 a bölünmez.")
# except NameError:
#     print("Olmayan değer var.")
except:
    print("Bilinmeyen hata oluştu")
# finally:
#     print ("İşlem tamam.")


