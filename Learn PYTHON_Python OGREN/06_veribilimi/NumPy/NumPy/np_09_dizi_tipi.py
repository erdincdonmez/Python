# Versiyonunu öğrenme
import numpy
print (numpy.__version__)

# Bir dizi oluşturalım.
import numpy
arr = numpy.array([1, 2, 3, 4, 5])
print(arr)

# İmport ta alias (takma ad) kullanalım
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# ndarray içerisine klasik python da olduğu gibi farklı türde veriler yazamıyoruz.
print (type(arr))
print (arr.dtype)

arr1 = np.arange(5,15,2)
print(arr1)