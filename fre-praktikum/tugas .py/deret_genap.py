#Inisialisasi jumlah deret
jumlah = 10

#Inisialisasi bilangan genap awal
angka = 2
hitung = 1

#Perulangan while untuk mencetak bilangan genap
while hitung < jumlah:
    print(angka, end=", " if hitung < jumlah - 1 else "")
    angka += 2
    hitung += 1