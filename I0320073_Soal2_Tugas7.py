print('SOAL 2')
print('Membuat program menggunakan fungsi numerik.')
print()

nama = input('Nama = ')
nim = input('NIM = ')

import math
a = float(input("Nilai Tugas 1 = "))
b = float(input("Nilai UTS = "))
c = float(input("Nilai Tugas 2 = "))
d = float(input("Nilai UAS = "))
nilaitotal = [a,b,c,d]

#menghitung rata-rata nilai
rata_rata = float(a + b + c + d)/4
print("Rata-rata nilai ananda", nama, "adalah", math.floor(rata_rata))
print()

print("Rincian nilai ananda", nama, "adalah sebagai berikut :")
print("Nilai tertinggi = ", max(a,b,c,d))
print("Nilai terendah = ", min(a,b,c,d))
print()

#memilih nilai secara random
import random
print("Pemilihan nilai secara random = ", random.choice(nilaitotal))


