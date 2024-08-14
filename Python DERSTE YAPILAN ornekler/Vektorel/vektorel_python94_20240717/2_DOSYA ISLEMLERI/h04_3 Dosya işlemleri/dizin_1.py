import os
# print(*os.listdir(),sep="\n")

ddlistesi = os.listdir()

for a in ddlistesi:
    # print(a)
    if a.endswith(".py"): print(a)