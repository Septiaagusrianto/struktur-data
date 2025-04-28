#Inisialisasi jumlah deret
jumlah = 20 #Mengatur jumlah bilangan genap yang akan dicetak

#Inisialisasi bilangan genap awal
angka = 2# Mengatur bilangan genap awal, yaitu 2.
hitung = 0#Mengatur variabel penghitung untuk mengontrol perulangan.

#Perulangan while untuk mencetak bilangan genap
while hitung < jumlah: # Perulangan while yang akan berjalan selama hitung kurang dari jumlah.
    print(angka, end=", " if hitung < jumlah - 1 else "") #Mencetak bilangan genap saat ini. Jika bukan bilangan terakhir, maka akan mencetak koma setelahnya.
    angka += 2 #Meningkatkan bilangan genap saat ini menjadi bilangan genap berikutnya.
    hitung += 1 #Meningkatkan variabel penghitung