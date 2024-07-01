from veritabanı import *
from odemeıslem import odemeYap
from menu import Menu
from musteri import Musteri
from siparis import Siparis

#yeni bir müşteri oluşturma.müşteriye ismini sorup müşteri  nesnesini oluşturma
def musteri_olustur() -> Musteri:
    ad = input("Adinizi giriniz: ")
    return Musteri(ad)

#sipariş alma.toplam fiyatı hesaplama
def siparis_al(menu: Menu, musteri: Musteri) -> float:
    toplam_fiyat = 0

    while True:
        #menuyü gösterip seçim yaptırıyoruz
        menu.menu_goster()
        try:
            secim = int(input(
                "\nCorba icin 1'e basiniz\nAna yemek icin 2'ye basiniz\nTatli icin 3'e basiniz\nIcecek icin 4'e basiniz\nSeciminizi yapiniz: "))
        except ValueError:
            print("Geçersiz seçim! Lütfen bir sayı girin.")
            continue

        if secim in range(1, 5):
            #kullanıcının seçtiği kategoriye göre menü gösteriyoruz
            kategori = ['corba', 'ana_yemek', 'tatli', 'icecek'][secim - 1]
            urunler = menu.urun_fiyatlari[kategori]
            # bir liste içindeki string öğeler birleştirilmiş
            print("\n".join(
                [f"{sec}: {urun['isim']}: {urun['fiyat']} TL" for sec, urun in urunler.items()]))

            urun_secimi = input(
                f"{kategori.capitalize()} seciminizi yapiniz ({', '.join(urunler.keys())}): ")#capitalize ile ilk harf büyük
            secilen_urun = menu.urun_sec(kategori, urun_secimi)

            if secilen_urun:
                #seçilen ürünü siparişe ekleyip toplam fiyatı güncelliyoruz
                siparis = Siparis(secilen_urun['isim'], kategori, secilen_urun['fiyat'])
                musteri.siparis_ekle(siparis)
                print(f"{secilen_urun['isim']} sepete eklendi.")
                toplam_fiyat += secilen_urun['fiyat']
            else:
                print(f"Hatali {kategori} secimi yaptiniz!")
        else:
            print("Hatali secim yaptiniz!")

        if toplam_fiyat >= 300:
            #toplam fiyatı 300tlye eşit veya büyükse siparişi bitiriyoruz.
            print("Toplam fiyat 300 TL'yi gecti. Siparisiniz yola cikabilir!")
            break

        devam_et = input(
            f"Toplam fiyat su an {toplam_fiyat} TL. Sepete baska bir sey eklemek ister misiniz? (Evet icin 'E' / Hayir icin 'H'): ")
        if devam_et.lower() != 'e':
            break

    return toplam_fiyat

def main() -> None:
    #veri tabanına bağlanıp müşteri tablosunu oluşturuyoruz
    db, cursor = veritabani_kur('siparisler')
    tablo_olustur("Musteri", cursor, "isim TEXT, fiyat REAL")

    #yeni bir müşteri oluşturup menüyü gösteriyor
    musteri = musteri_olustur()
    menu = Menu()

    #müşterien sipariş alıyorz 
    toplam_fiyat = siparis_al(menu, musteri)

    #müşteri bilgilerini veri tabanına ekliyoruz ve siparişleri çekiyoruz
    tabloya_info_ekle(db, cursor, 'Musteri', "isim,fiyat", f"'{musteri.ad}' , {toplam_fiyat}")
    urunleri_cek(cursor, "Musteri")
    veritabani_kapat(db)

    #müşteriye sipariş özetini gösterip öeme yapmasını sağlıyoruz
    print(musteri.siparis_ozeti())
    odemeYap(toplam_fiyat)

if __name__ == "__main__":
    main()

