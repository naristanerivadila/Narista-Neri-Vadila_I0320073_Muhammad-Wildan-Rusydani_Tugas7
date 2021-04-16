print("SOAL 1")
print("Membuat program menggunakan fungsi string.")
print()

str = "Biodata Mahasiswa"
str2 = str.upper()
print(str2)
print("Isilah biodata mahasiswa dibawah ini:")

s = str.center(30, "-")
print(s)

nama = input("Nama : ")
kelas = input("Kelas : ")
nim = input("NIM : ")
print()

nilaimin = 3.20
print("Syarat minimal nilai adalah = ", nilaimin)
nilai = input("Nilai anda : ")
print()

if float(nilai) >= nilaimin:
    print("Anda bisa mendaftar beasiswa!")
else :
    print("Anda tidak bisa mendaftar beasiswa!")

str = "selesai"
s = str.capitalize()
print(s)



