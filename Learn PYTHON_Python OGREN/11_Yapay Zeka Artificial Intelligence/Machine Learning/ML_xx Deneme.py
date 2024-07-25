# Bu kod, basit bir kayıp fonksiyonu olan 𝑓(𝑥)=𝑥2f(x)=x 2'nin minimumunu bulmak için gradyan inişi algoritmasını kullanır. Öğrenme oranı (learning_rate) ve başlangıç noktası (initial_x) gibi parametreler, algoritmanın performansını etkileyebilir.
import numpy as np

# Örnek bir kayıp fonksiyonu: f(x) = x^2
def loss_function(x):
    return x ** 2

# Gradyanı hesapla: f'(x) = 2x
def gradient(x):
    return 2 * x

# Gradyan inişi parametreleri
learning_rate = 0.1
initial_x = 10  # Başlangıç noktası
max_iterations = 100

# Gradyan inişi algoritması
x = initial_x
for i in range(max_iterations):
    grad = gradient(x)
    x = x - learning_rate * grad  # Parametre güncellemesi
    print(f"İterasyon {i+1}: x = {x}, Loss = {loss_function(x)}")

print(f"Minimuma ulaşılan x: {x}")
