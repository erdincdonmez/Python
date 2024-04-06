a = (
    {'adi': 'Mahir ARISOY', 'num': '6325214523'}, 
    {'adi': 'Gökhan', 'num':'5233333333'}
    )
b = {
    "ali":{'adi': 'Mahir ARISOY', 'num': '6325214523'}, 
    "veli":{'adi': 'Gökhan', 'num': '5233333333'}
    }

c = [
    {'adi': 'Mahir ARISOY', 'num': '6325214523'}, 
    {'adi': 'Gökhan', 'num': '5233333333'}
    ]

print("\n\n",a)
print("\n\n",a[1])
print("\n\n",b)
print("\n\n",b["ali"])
print("\n\n",c[0])
print("\n\nCnin 0.nın numarası:",c[0]['num'])
print("\n\nCnin 1.nın numarası:",c[1]['num'])
aa = "555"
c[1]['num'] = aa
print("\n\nCnin 1.nın numarası:",c[1]['num'])