import matplotlib.pyplot as plt

# Kategoriler ve değerler
kategoriler = ["1.Sınav", "2.Sınav", "3.Sınav"]
degerler = [80, 70, 90]

plt.bar(kategoriler, degerler, color='skyblue')
plt.title('Kategoriye Göre Değerler')
plt.xlabel('Kategoriler')
plt.ylabel('Değerler')

# Sütunların üzerine değerleri yazma
for i, v in enumerate(degerler):
    plt.text(i, v + 1, str(v), ha='center', va='bottom')

plt.show() # Grafiği gösterme
