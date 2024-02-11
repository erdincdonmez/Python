# Matplotlib'den pyplot'u içe aktarın ve DataFrame görselleştirme
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
df.plot()
plt.show()

# Dağılım grafiği / Scatter Plot
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show() # Kolerasyon 0.922721

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
plt.show() # Kolerasyon 0.009403

df["Duration"].plot(kind = 'hist')
plt.show() # Histogram : aralık sıklığı


