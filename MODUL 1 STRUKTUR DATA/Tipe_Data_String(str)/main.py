a = 'Halo'
b = "Python"
c = """Ini adalah
string multi-baris"""
print(type(a))  # <class 'str'>
print(type(b))  # <class 'str'>
print(type(c))  # <class 'str'>

# indexing dan slicing 
text = "RIAN"
print(text[0])     # Output: R
print(text[-1])    # Output: I
print(text[0:3])   # Output: A
print(text[:4])    # Output: N
print(text[::2])   # Output: AN (loncat 2 karakter)

# Operasi penggabungan string
print('Hello ' + 'RIAN')

# Operasi pengulangan string
print('HOHO' * 3)

# Operasi Pengecekan string
print('B' in 'data') # menghasilkan boolean (True/False)

# Operasi panjang string
print(len('RIAN'))

s = "RIAN programming"
print(s.upper())       # 'RIAN PROGRAMMING'
print(s.capitalize())  # 'RIAN programming'
print(s.title())       # 'RIAN Programming'
print(s.replace("python", "java"))  # 'java programming'
print(s.split())       # ['RIAN', 'programming']
print(s.find("gram"))  # 10 

# F-String
# String format menggunakan F-String
name = "Rian"
age = 21
print(f"Halo, nama saya {name}, umur saya {age}")

# Format Method
# String format dengan format method
print("Halo, nama saya {}, umur saya {}".format(name, age))

