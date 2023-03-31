Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def calculate_age():
...     print("Lütfen aşağıdaki soruları yanıtlayın.")
...     gender = input("Cinsiyetiniz (Erkek/Kadın): ")
...     height = float(input("Boyunuz (cm): "))
...     weight = float(input("Kilonuz (kg): "))
...     
...     # Hesaplama formülü
...     age = int((height * 0.5 + weight * 0.3 + (gender.lower() == 'kadın') * 3.6 - 676.2) / 4.4)
...     
...     print(f"Sizin tahmini yaşınız: {age}")
... 
... calculate_age()
