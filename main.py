# main.py

# 1. Basic Output: Using the print() function to display information.
print("Merhaba Akwannya Hub Skill Pod!") # Hello Akwannya Hub Skill Pod!
print("Python öğrenimine hoş geldiniz.") # Welcome to Python learning.

# 2. Variables and Data Types:
# Python's simple syntax for variable assignment and automatic type inference.
hafta_numarasi = 1             # Integer type
konu = "Python Temelleri"      # String type
katilimcilar = ["Ayşe", "Mehmet", "Zeynep", "Ali"] # List type

print(f"\n--- Hafta {hafta_numarasi} ---")
print(f"Konu: {konu}")
# Using len() function to get the number of elements in a list.
print(f"Toplam katılımcı sayısı: {len(katilimcilar)}")

# 3. Basic Operations:
# Arithmetic operation (multiplication).
ders_suresi_saat = 3
ders_suresi_dakika = ders_suresi_saat * 60
print(f"Ders süresi: {ders_suresi_saat} saat ({ders_suresi_dakika} dakika)")

# String concatenation using the '+' operator.
selamlama = "Merhaba, " + katilimcilar[0] + "!"
print(selamlama)

# 4. Control Flow: if/else statement
# Demonstrating conditional logic based on a condition.
if hafta_numarasi == 1:
    print("Bu ilk hafta, temel kavramlara odaklanıyoruz.")
else:
    print("İleri seviye konulara geçiyoruz.")

# 5. Loop: for loop
# Iterating through elements of a list, a common task in Python.
print("\nKatılımcılar:")
for isim in katilimcilar:
    print(f"- {isim}")

# 6. Function Definition
# Defining a simple function to encapsulate reusable logic.
def ders_ozeti_yaz(hafta, konu_adi):
    """
    Belirtilen hafta ve konu için bir ders özeti yazdırır.
    This function prints a summary for the given week and topic.
    """
    print(f"\n--- Ders Özeti ---")
    print(f"Hafta: {hafta}")
    print(f"Ana Konu: {konu_adi}")
    print("Bu hafta Python'ın temel söz dizimi, değişkenler, veri tipleri ve kontrol yapıları incelendi.")
    print("Pratik uygulamalarla pekiştirildi.")

# Calling the function with current week and topic.
ders_ozeti_yaz(hafta_numarasi, konu)

print("\nPython öğrenme yolculuğunuzda başarılar dileriz!")
