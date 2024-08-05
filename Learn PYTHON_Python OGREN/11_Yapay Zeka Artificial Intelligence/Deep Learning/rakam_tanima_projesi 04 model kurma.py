# pip install tensorflow
import tensorflow as tf
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical, plot_model
import matplotlib.pyplot as plt
import numpy as np
import warnings 
from warnings import filterwarnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
warnings.filterwarnings("ignore",category=FutureWarning)
warnings.filterwarnings("ignore",category=UserWarning)
filterwarnings("ignore")

from tensorflow.keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data() # x_train : 28x28 eğitim görselleri, y_train görüntü etiketleri
print(f"Eğitim setinin boyutu:\t {x_train.shape}x{y_train.shape}")
print(f"Test setinin boyutu:\t {x_test.shape}x{y_test.shape}")

num_labels = len (np.unique(y_train))
print("Farklı etiket sayısı: ", num_labels)

# One-hot encode labels. y_train ve y_test in her bir değeri (0 to 9) arası rakamlar iken, one-hot encoded ile her bir değer [0, 0, 1, 0, 0, 0, 0, 0, 0, 0] şekline dönüştürüldü.
y_train = to_categorical(y_train, num_labels)
y_test = to_categorical(y_test, num_labels)

def tek_resim_goster(): # Tek resim göstermek için 
    plt.figure(figsize=(5,5))
    plt.imshow(x_train[2], cmap='gray') 
    plt.show()
# tek_resim_goster()

def resimleri_goster(veri): # Çoklu resim göstermek için
    for n in range(veri):
        ax = plt.subplot(5,5,n+1)
        plt.imshow(x_test[n], cmap='gray')
        # plt.imshow(x_train[n], cmap='gray')
        plt.axis('off')
    plt.show()
# resimleri_goster(5) 

print("\n\nx_train[2] verisi: ", x_train[2]) 
print("\n\nx_train[2][14,10] verisi: ", x_train[2][14,10]) 
print("\n\nx_train[2].sum() : ", x_train[2].sum()) 
print("\n\nx_train[2][14:20, 10:20] : \n", x_train[2][14:20, 10:20]) 
print("\n\nx_train[2][14:20, 10:20].mean() : ", x_train[2][14:20, 10:20].mean()) 

def resim_uzerinde_deger_göster(resim):
    fig = plt.figure(figsize=(12,12))
    ax = fig.add_subplot(111)
    ax.imshow(resim, cmap='gray')
    genislik, yukseklik = resim.shape # genislik=satır uzunluğu, yukseklik= sütun uzunluğu
    esik = resim.max()/2.5 # esik = threshold
    for x in range(genislik):
        for y in range(yukseklik):
            ax.annotate(str(round(resim[x][y],2)), xy=(y,x), color="blue" if y%2==0 else 'red')
            # ax.annotate(str(round(resim[x][y],2)), xy=(y,x), color="white" if resim[x][y]<esik else 'black')
            # ax.annotate(str(round(resim[x][y],2)), xy=(y,x), color="red")
    plt.show()

# resim_uzerinde_deger_göster(x_train[2])

# VERİYİ HAZIRLAMA İÇİN 3 AŞAMA TAKİP EDİLECEK.
# 1- Encoding / veriyi sayısallaştırma
# Bağımlı değişken, label, output, hedef değişken aynı şey
print("\n\ny_train[0:5] : ",y_train[0:5])
print("\n\nto_categorical(y_train[0:5] : \n",to_categorical(y_train[0:5]))
print("\n\nto_categorical(y_test[0:5] : \n",to_categorical(y_test[0:5]))

# 2- Reshaping / veriyi yeniden şekillendirme
print("\n\nx_train.shape[1] : ",x_train.shape[1])
print("\n\nx_train.shape1 : ",x_train.shape)
print("\n\nx_test.shape1 : ",x_test.shape)

x_train = x_train.reshape(x_train.shape[0],28,28,1)
x_test = x_test.reshape(x_test.shape[0],28,28,1)
print("\n\nx_train.shape2 : ",x_train.shape)
print("\n\nx_test.shape2 : ",x_test.shape)


# 3- Normalization / Aykırılıkları yoketme
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255
# resim_uzerinde_deger_göster(x_train[2])
print("\n\nx_train[2] : \n",x_train[2])

# MODEL KURMA
model = tf.keras.Sequential([
    Flatten(input_shape=(28,28,1)),
    Dense(units=128, activation='relu', name='layer1'), # unit = 128 unit: nöron sayısı ,28x28 resimleri tanımlayabilecek feature/özellik/nöron sayısı, activation='relu' insan beynindeki gibi gereksiz bazı nöronları sönümlendiren bazılarını güçlendiren bir fonksiyon. gizli katmanlarda relu kullanılır.
    Dense(units=num_labels, activation='softmax', name='output_layer') # activation='softmax' : çok sınıflı bir sınıflandırma problemi için softmax, iki sınıflı bir sınıflandırma problemi için sigmoid kullanılır.
])

model.compile(loss='categorical_crossentropy', # lose: hata/kayıp hesaplama yöntemi/hata değerlendirme metriği. Çok sınıflı olduğu için categorical_crossentropy
              optimizer='adam', # loss fonksiyonunu optimize edecek algoritma. adam, Stochastic Gradient Descent,
              metrics=[tf.keras.metrics.Precision(), tf.keras.metrics.Recall(), 'accuracy' ]
              )
model.summary()

model.fit(x_train, y_train,epochs=5, batch_size=128, validation_data=(x_test, y_test)) # epoch : tur sayısı, batch_size: gradian hesaplarında ağırlık güncelleme küme sayısı. 128 = her iterasyonda 128 gözlem birimi dikkate alınıp işlemler yapıldıktan sonra sonraki iterasyona geç.