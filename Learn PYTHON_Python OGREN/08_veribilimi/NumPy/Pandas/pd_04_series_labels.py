
# LABEL
# Verilere etiket ekleyebilirsiniz.
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print("myvar['x'] etiketli eleman:",myvar['x'])
print("myvar['y'] etiketli eleman:",myvar['y'])