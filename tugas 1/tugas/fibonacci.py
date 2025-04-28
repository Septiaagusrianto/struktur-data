# Menentukan jumlah deret Fibonacci (default 10)
jumlah = 10 #nilai dafault
user_input = input("Masukkan jumlah deret Fibonacci (enter untuk menggunakan default 10): ")

# Jika ada input dari pengguna, ubah jumlah deret sesuai input
if user_input != "":
    jumlah = int(user_input)

# Inisialisasi dua angka pertama Fibonacci
a, b = 1, 1

# Menampilkan deret Fibonacci
print(a, end=", ")  # Menampilkan angka pertama
for _ in range(jumlah - 1):
    print(b, end=", " if _ < jumlah - 2 else "\n")  # Menampilkan angka berikutnya, koma kecuali angka terakhir
    a, b = b, a + b  # Update nilai a dan b ke angka Fibonacci berikutnya
