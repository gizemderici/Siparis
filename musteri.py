class Musteri:
    def __init__(self, ad: str):
        self.ad = ad
        self.siparisler = []

    def siparis_ekle(self, siparis):
        self.siparisler.append(siparis)

    def toplam_fiyat(self):
        return sum(siparis.fiyat for siparis in self.siparisler)

    def siparis_ozeti(self):
        ozet = f"{self.ad}'nin Siparisi:\n"
        for siparis in self.siparisler:
            ozet += f"- {siparis.isim}: {siparis.fiyat} TL\n"
        ozet += f"Toplam Fiyat: {self.toplam_fiyat()} TL"
        return ozet
