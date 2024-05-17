import tensorflow as tf, re, string
from tensorflow.keras.layers import TextVectorization

veri = [
    "Bugün hava çok güzel",
    "Ali, Efe ve Ece çay içecek",
    "Selam söyle"
]

def standartlarstir(xx):
    kucukHarfSekli = tf.strings.lower(xx)
    return tf.strings.regex_replace(
        kucukHarfSekli, f"[{re.escape(string.punctuation)}]","" # punctutation noktalama işaretlerini veriyor. Bu satır ile de noktalam işaretleri kaldırılıyor.
    )

def bol(gelen):
    return tf.strings.split(gelen)

# TextVectorization normalde CPU'da çalışır. Data pipline veya model içerisine yerleştirilirse GPU'da çalışırak daha hızlı işlem yapar.
tv = TextVectorization(
    standardize = standartlarstir, split = bol
)

tv.adapt(veri)

metin = "bugün ece çok güzel"

tv(metin)

print("tv: ",tv.get_vocabulary())
# print("tv: ",tv['bolunmusSekli'])

