# Variabel global untuk menyimpan data siswa
siswa = []  # List kosong untuk menyimpan data siswa

# Fungsi untuk menambahkan nama siswa ke dalam daftar
def tambah_siswa():
    nama = input("Masukkan nama siswa: ")  # Minta input nama siswa
    siswa.append(nama)  # Tambahkan nama ke dalam list siswa
    print(f"Nama siswa '{nama}' telah ditambahkan.")  # Konfirmasi penambahan

# Fungsi untuk menampilkan semua data siswa
def tampilkan_siswa():
    if not siswa:  # Jika list siswa kosong
        print("Tidak ada data siswa.")  # Tampilkan pesan
    else:
        print("Data Siswa:")  # Tampilkan judul
        for i, nama in enumerate(siswa):  # Loop dengan index
            print(f"{i+1}. {nama}")  # Cetak nomor dan nama siswa

# Fungsi untuk mengubah nama siswa berdasarkan indeks
def update_siswa():
    if not siswa:  # Jika list siswa kosong
        print("Tidak ada data siswa.")  # Tampilkan pesan
    else:
        tampilkan_siswa()  # Tampilkan data siswa
        try:
            indeks = int(input("Masukkan indeks siswa yang ingin diubah: ")) - 1  # Input indeks
            if indeks < 0 or indeks >= len(siswa):  # Cek indeks valid/tidak
                print("Indeks tidak valid.")  # Tampilkan pesan error
            else:
                nama_baru = input("Masukkan nama baru: ")  # Input nama baru
                siswa[indeks] = nama_baru  # Update nama siswa
                print(f"Nama siswa pada indeks {indeks+1} telah diubah menjadi '{nama_baru}'.")  # Konfirmasi
        except ValueError:  # Jika input bukan angka
            print("Input harus berupa angka.")  # Tampilkan pesan error

# Fungsi untuk menghapus nama siswa berdasarkan indeks
def hapus_siswa():
    if not siswa:  # Jika list siswa kosong
        print("Tidak ada data siswa.")  # Tampilkan pesan
    else:
        tampilkan_siswa()  # Tampilkan data siswa
        try:
            indeks = int(input("Masukkan indeks siswa yang ingin dihapus: ")) - 1  # Input indeks
            if indeks < 0 or indeks >= len(siswa):  # Cek indeks valid/tidak
                print("Indeks tidak valid.")  # Tampilkan pesan error
            else:
                nama = siswa.pop(indeks)  # Hapus siswa dari list
                print(f"Nama siswa '{nama}' telah dihapus.")  # Konfirmasi penghapusan
        except ValueError:  # Jika input bukan angka
            print("Input harus berupa angka.")  # Tampilkan pesan error

# Loop utama program
while True:
    print("\nMenu:")  # Tampilkan menu
    print("1. Tambah Siswa")
    print("2. Tampilkan Siswa")
    print("3. Update Siswa")
    print("4. Hapus Siswa")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan: ")  # Input pilihan menu

    if pilihan == "1":
        tambah_siswa()  # Panggil fungsi tambah siswa
    elif pilihan == "2":
        tampilkan_siswa()  # Panggil fungsi tampilkan siswa
    elif pilihan == "3":
        update_siswa()  # Panggil fungsi update siswa
    elif pilihan == "4":
        hapus_siswa()  # Panggil fungsi hapus siswa
    elif pilihan == "5":
        print("Keluar dari program.")  # Tampilkan pesan keluar
        break  # Keluar dari loop
    else:
        print("Pilihan tidak valid.")  # Pesan jika pilihan salah