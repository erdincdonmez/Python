import tensorflow as tf
from tensorflow.keras.layers import TextVectorization

tv = TextVectorization()
veri = [
    "Bugün hava çok güzel",
    "Ali, Efe ve Ece çay içecek",
    "Selam söyle"
]

print(veri)

tv.adapt(veri) # verileri eğitmek için. Verilerden sözlük oluşturarak her bir token(en küçük parçalar) indexlendi.
tv.get_vocabulary()

print("tv: ",tv.get_vocabulary())

vt = tv(veri) # vectorized text / sözlüğü vektörize edelim

print("vt:",vt) # verinin sözlükteki indexlerini içeren sayısal şekli. 0 lar olmayan kelimelerin yerine..


# text vectorization
# tv = [
#     "", # maskeleme için
#     [UNK], # Bilinmeyen kelimeler için
#     'çok', # çok kelimesinin sözlük indexi 1
#     'çay'  # çay kelimesinin sözlük indexi 2
#     ...    # ...
#     'ali'
# ]

# vectorized text
# vt: tf.Tensor([
#     [12  8  2  9  0  0]
#     [13 10  4 11  3  7]
#     [ 6  5  0  0  0  0]
# ], shape=(3, 6), dtype=int64)