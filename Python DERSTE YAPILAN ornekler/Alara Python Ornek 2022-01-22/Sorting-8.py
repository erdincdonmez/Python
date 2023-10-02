ogrenciDemeti = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
    ]
print("Sıralama öncesi : ",ogrenciDemeti)
print("Sıralama sonrası: ",sorted(ogrenciDemeti, key=lambda student: student[2]))# yaşa göre sırala
