#05 Başlık ve etiket ve değer ekleme
import matplotlib.pyplot as plt
kategoriler = ["1.Sınav","2.Sınav","3.Sınav"]
degerler = [80,70,90]

plt.title('Kategoriye Göre Değerler')
# X ve Y eksenlerine etiketler ekleme
plt.xlabel('Kategoriler')
plt.ylabel('Değerler')

plt.plot(kategoriler, degerler)
plt.show()
