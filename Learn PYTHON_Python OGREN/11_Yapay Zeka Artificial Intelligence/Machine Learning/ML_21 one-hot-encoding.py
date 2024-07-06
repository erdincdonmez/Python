# Pandas ile One-Hot Encoding
import pandas as pd

# Örnek veri
df = pd.DataFrame({'Renk': ['Kırmızı', 'Yeşil', 'Mavi', 'Yeşil']})

# One-hot encoding
one_hot_encoded_df = pd.get_dummies(df['Renk'])
print(one_hot_encoded_df)

# # Scikit-learn ile One-Hot Encoding
# from sklearn.preprocessing import OneHotEncoder

# # Örnek veri
# data = [['Kırmızı'], ['Yeşil'], ['Mavi'], ['Yeşil']]

# # One-hot encoder oluşturma
# encoder = OneHotEncoder(sparse_output=False)  # 'sparse' yerine 'sparse_output' kullanıldı
# encoded_data = encoder.fit_transform(data)
# print(encoded_data)

# # Pandas ile One-Hot Encoding
# import pandas as pd

# # Örnek veri
# df = pd.DataFrame({
#     'Renk': ['Kırmızı', 'Yeşil', 'Mavi', 'Yeşil'],
#     'Sayı': [1, 2, 3, 4]
# })

# print("Orijinal DataFrame:\n", df)

# # One-hot encoding
# one_hot_encoded_df = pd.get_dummies(df, columns=['Renk'])
# print("\nOne-hot encoded DataFrame:\n", one_hot_encoded_df)