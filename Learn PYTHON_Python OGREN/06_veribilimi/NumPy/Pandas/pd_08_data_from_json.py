# Read from JSON Files
import pandas as pd
# data.json bu kodların kayıtlı olduğu dizinde olsun.
# vs-code kullanıyorsanız vscodu açtığını klasörde olsun.
print("\n\nPrint ile yazdırma\n")
df = pd.read_json('data.json')
print(df) # ilk 5 ve son 5 satır

print("\n\n.to_string() ile yazdırma\n")
print(df.to_string())# tamamı

# max_rows ayarının üzerindeki verilerde
# print ile ilk ve son 6 satırlar yazdırılır
print("max_rows :", pd.options.display.max_rows)
print("\n\nmax_row ayarı değiştirilebilir")
pd.options.display.max_rows = 100
print(df) # veri max_row dan fazlaysa ilk ve son5 satır

print("\n\nJSON = Python Sözlüğü olduğundan direk atanabilir.")
data = {
  "Duration":{"0":60,"1":60,"2":60,"3":45,"4":45,"5":60},
  "Pulse":{"0":110,"1":117,"2":103,"3":109,"4":117,"5":102},
  "Maxpulse":{"0":130,"1":145,"2":135,"3":175,"4":148,"5":127},
  "Calories":{"0":409,"1":479,"2":340,"3":282,"4":406,"5":300}
  }
df = pd.DataFrame(data)
print(df) 


