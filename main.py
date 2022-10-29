"""
ini adalah demo project dengan python
"""
print ('ibu "budi, pergi ke toko" ')
print('budi "beli apa?"')
print('ibu , "beli susu 1, jika ada telur, beli 6"')
print('budi pergi ke toko')
print('budi cek harga dan membeli susu, mungkin juga beli telur kalau ada')

# Percabangan
jumlahbotolsusu = 173
jumlahtelur = 158

print (f"jumlah botol susu {jumlahbotolsusu} btl")
print (f"jumlah telur {jumlahtelur} butir")\

if jumlahbotolsusu > 0 :
    print ("budi cek harga dan ternyata cukup")
    if jumlahtelur == 0 :
        print ("budi beli 1 btl susu")
    else:
        print("budi beli 6 btl susu")
else:
    print("budi tidak jadi beli 1 btl susu")

print("budi pulang")
print("budi menyerahkan hasil ke ibu")
