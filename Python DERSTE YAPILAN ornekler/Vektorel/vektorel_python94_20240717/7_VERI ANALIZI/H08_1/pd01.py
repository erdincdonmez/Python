# DataFrame
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
# verileri DataFrame içine aktar
df = pd.DataFrame(data)
print(df)