cbd = []
for a in range(15):
    satir=[]
    for b in range(15):
        satir.append("▒") # 176 ░, 177 ▒, 178 ▓
        # satir = ...............
    cbd.append(satir)

# print(cbd)
satir1 = ""
for xx in cbd:
    for tt in xx:
        # print(tt)
        satir1 += tt
    print(satir1)
    satir1=""
    # print("-----------")
