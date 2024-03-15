# Sözlükten seri oluşturma
# keyler label a dönüşür
import pandas as pd
calories = {"Gün-1": 420, "Gün-2": 380, "Gün-3": 390}
myvar = pd.Series(calories)
print(myvar)


myvar = pd.Series(calories, index = ["Gün-1", "Gün-2"])
print("\nSadece Gün-1 ve Gün-2 ile seri:")
print(myvar)