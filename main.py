# Kullanıcıdan notları ve istenen ortalamayı al
not1 = float(input("Birinci sınavın notunu girin: "))
not2 = float(input("İkinci sınavın notunu girin: "))
istenen_ortalama = float(input("İstenen ortalamayı girin: "))

# Üçüncü sınavın notunu hesapla
not3 = (3 * istenen_ortalama) - (not1 + not2)

# Sonucu yazdır
print("Üçüncü sınavda {not3:.2f} alman gerekiyor.")