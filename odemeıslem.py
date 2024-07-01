def odemeYap(toplamFiyat):
    kartNo = input("Odeme bilgilerinizi giriniz:\nKart no (14 haneli olmalı): ")
    sifre = int(input("Sifre (4 haneli olmalı): "))

    if not kartNo.isdigit() or len(kartNo) != 14: #girilen verinin sayısal olup olmadığını kontrol etmek
        print("Gecersiz kart numarasi girdiniz.")
        return

    if 1000 <= sifre <= 9999:
        print(f"Odeme islemi tamamlandi. Toplam Fiyat: {toplamFiyat} TL")
    else:
        print("Gecersiz sifre girdiniz.")
