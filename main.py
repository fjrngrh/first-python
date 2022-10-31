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

# Perulangan for
""" 
perulangan membaca bukumu
"""

jmlhbuku = 100
print('ibu, baca semua bukumu')
jmlhbukuygsudahdibaca = 0

for jmlhbukuygsudahdibaca in range(1, jmlhbuku + 1):
    print(f"buku ke-{jmlhbukuygsudahdibaca} sudah dibaca")

# Perulangan while

jmlhbuku1 = 10
print('ibu, baca semua bukumu')

jmlhbukuygsudahdibaca1 =  0
print(f' jumlah buku yg sudah dibaca {jmlhbukuygsudahdibaca1 + 1}')

while jmlhbukuygsudahdibaca1 < jmlhbuku1:
    jmlhbukuygsudahdibaca1 = jmlhbukuygsudahdibaca1 + 1
    print(f"buku ke- {jmlhbukuygsudahdibaca1} sudah dibaca")

print(f'jumlah buku yg sudah dibaca {jmlhbukuygsudahdibaca1}')

"""
Program perulangan membaca buku dengan while sampai paham
"""
buku = 10
print('Ibu berkata, "Baca semua bukumu sampai paham')
dibaca = 0
dipahami = 0
print (f'Jumlah buku yang sudah dibaca dan dipahami {dipahami}')

while dibaca < buku * 2:
    dibaca = dibaca + 1
    if dipahami == 9:
        print(f"Buku ke { dipahami + 1} belum paham")
    else:
        dipahami = dipahami + 1
        print(f"Buku ke {dipahami} sudah dibaca dan dipahami")

print (f'Jumlah buku yang sudah dibaca dan dipahami {dipahami}')
if dipahami == buku:
    print('bu semua buku sudah dibaca dan dipahami ')
else:
    print(f"bu tidak semua buku bisa dipahami."
          f"budi hanya bisa pahami {dipahami} buku")


