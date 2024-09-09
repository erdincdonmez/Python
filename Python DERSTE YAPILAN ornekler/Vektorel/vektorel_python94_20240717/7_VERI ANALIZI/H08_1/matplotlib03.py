#06 Veri etiketleri
import matplotlib.pyplot as plt

# Kategoriler ve değerler
kategoriler = ["1.Sınav", "2.Sınav", "3.Sınav"]
degerler = [80, 70, 90]
# Sütun grafiği oluşturma

plt.title('Kategoriye Göre Değerler')
plt.xlabel('Kategoriler')
plt.ylabel('Değerler')

plt.bar(kategoriler, degerler)
plt.bar_label(plt.bar(kategoriler, degerler))

plt.show() # Grafiği gösterme