'''
#no 1
Nilai = int(input("Masukan nilai:"))
if Nilai >=0:
    if Nilai >= 90:
        print("Excellent")
    elif Nilai >= 80:
        print("Very Good")
    elif Nilai >= 70:
        print("Good")
    elif Nilai >= 60:
        print("Average")
    else:
        print ("Coba lagi!")
'''

'''#no 2
a = int(input("Masukan nilai bilangan pertama: "))
b = int(input("Mas)ukan nilai bilangan kedua: "))
c = int(input("Masukan nilai bilangan ketiga: "))

terbesar = max(a,b,c)
print("Bilangan terbesar = ", terbesar)

#no 3
#Mencetak Deret Fibonacci hingga
def fibonacci(n):
    a, b = 0, 1
    hasil = []
    while a <= n:
        hasil.append(a)
        a, b = b, a + b
    return hasil
n = int(input("Masukan nilai bilangan: "))
print("Hasilnya adalah", fibonacci(n))
'''

'''#no 4
bilangan = int(input("Masukan nilai bilangan: "))
for i in range(1, bilangan+1, 2):
    print(i)'''

'''#no 5
n = int(input("Masukan bilangan bulat positif: "))
for i in range(1, n +1):
    print(str(i) * i)'''