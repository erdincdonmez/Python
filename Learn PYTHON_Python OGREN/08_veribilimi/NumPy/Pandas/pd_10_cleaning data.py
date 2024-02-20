# Analyzing DataFrames
import pandas as pd
print("\n\nVeriler:\n")
df = pd.read_csv('data.csv')
print(df.to_string()) # veriler

# Boş hücreler, verileri analiz ettiğinizde size yanlış sonuç verme potansiyeline sahiptir.
# Boş hücrelerin oranı toplam veriye oranla önemli bir sayıyı geçmiyorsa kaldırılabilir.

new_df = df.dropna() # orjinal dizi aynı kalır.
print("\n\ndf.dropna() ile boş veri satırları silinerek  şekli:\n")
print(new_df.to_string())

print("\n\ndropna(inplace = True) ile boş veri satırları silinmiş şekli:\n")
df.dropna(inplace = True) # orjinal diziyi değiştirir.
print(df.to_string())

df = pd.read_csv('data.csv')
print("\n\nfillna(130, inplace = True) ile boş veri yerine 130 yaz:\n")
df.fillna(130, inplace = True)
print(df.to_string())

df = pd.read_csv('data.csv')
print("\n\nSadece Calories sütunundaki boşları 130 yap :\n")
df["Calories"].fillna(130, inplace = True) 
# df["Calories"].method(130, inplace=True) # yeni kullanım
print(df.to_string())

# pandas 3 sonrası aşağıdaki methodları kullanın
# df.method({"Calories": 130}, inplace=True) 
# df["Calories"] = df["Calories"]

df = pd.read_csv('data.csv')
print("Boş hücreleri mevcutların ortalaması ile değiştir:")
ort = df["Calories"].mean()
df["Calories"].fillna(ort, inplace = True) 
# df["Calories"].method(ort, inplace=True) # yeni kullanım
print(df.to_string())

print("Boş hücreleri mevcutların medyanı ile değiştir:")
# Medyan = tüm değerleri artan şekilde sıraladıktan sonra ortadaki değer.
df = pd.read_csv('data.csv')
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)
print(df.to_string())

print("Boş hücreleri mevcutların modu ile değiştir:")
df = pd.read_csv('data.csv')
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)
print(df.to_string())