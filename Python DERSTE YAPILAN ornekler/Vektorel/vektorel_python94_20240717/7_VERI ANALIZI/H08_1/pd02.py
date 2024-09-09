# Read from CSV Files
import pandas as pd
# data.csv bu kodların kayıtlı olduğu dizinde olsun.
# vs-code kullanıyorsanız vscodu açtığını klasörde olsun.
print("\n\nPrint ile yazdırma\n")
df = pd.read_csv('data1.csv')
print(df) # ilk 5 ve son 5 satır

print("\n\n.to_string() ile yazdırma\n")
print(df.to_string())# tamamı

# max_rows ayarının üzerindeki verilerde
# print ile ilk ve son 6 satırlar yazdırılır
print("max_rows :", pd.options.display.max_rows)
print("\n\nmax_row ayarı değiştirilebilir")
pd.options.display.max_rows = 100
print(df) # veri max_row dan fazlaysa ilk ve son 5 satır
