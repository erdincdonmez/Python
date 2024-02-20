# DataFrame
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
# verileri DataFrame içine aktar
df = pd.DataFrame(data)
print(df)

print("\n1. satır: ")
print(df.loc[0])
# kullanıldığında []sonuç bir Pandas DataFrame olur
print("\n1. ve 2.satır: \n",df.loc[[0, 1]])

veri = {
  "kolori": [420, 380, 390],
  "süre": [50, 40, 45]
}
df = pd.DataFrame(veri, index = ["Gün-1", "Gün-2", "Gün-3"])
print("\nİsimlendirilmiş satırlar:\n",df) 
print("\ndf.loc['Gün-2']:")
print(df.loc["Gün-2"])