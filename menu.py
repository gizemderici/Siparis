class Menu:
    urun_fiyatlari = {
        'corba': {'a': {'isim': 'Mercimek Corbasi', 'fiyat': 30}, 'b': {'isim': 'Ezogelin Corbasi', 'fiyat': 40},
                  'c': {'isim': 'Yogurt Corbasi', 'fiyat': 30}},
        'ana_yemek': {'d': {'isim': 'Doner', 'fiyat': 100}, 'e': {'isim': 'Sebze Yemegi', 'fiyat': 60},
                      'f': {'isim': 'Hamsi', 'fiyat': 70}},
        'tatli': {'g': {'isim': 'Irmik Tatlisi', 'fiyat': 50}, 'h': {'isim': 'Kazandibi', 'fiyat': 60},
                  'i': {'isim': 'Baklava', 'fiyat': 70}},
        'icecek': {'j': {'isim': 'Kola', 'fiyat': 20}, 'k': {'isim': 'Ayran', 'fiyat': 20},
                   'l': {'isim': 'Su', 'fiyat': 5}}
    }

    def menu_goster(self):
        for kategori, urunler in self.urun_fiyatlari.items():
            print(f"\n{kategori.capitalize()}:")
            #her bir ürün ve fiyatı ayrı ayrı listelenir
            for secim, detay in urunler.items():
                print(f"{secim}: {detay['isim']} - {detay['fiyat']} TL")

    def urun_sec(self, kategori: str, secim: str):
         #eğer seçilen ürün mevcutsa, detayları döndürülür

        if secim in self.urun_fiyatlari[kategori]:
            return self.urun_fiyatlari[kategori][secim]
        else:
            return None