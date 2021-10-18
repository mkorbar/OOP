
class Zivila():
    ime = None
    kalorije = None
    priljubljenost = None

    def __init__(self, ime, kalorije, priljubljenost):
        self.ime = ime
        self.kalorije = kalorije
        self.priljubljenost = priljubljenost

    def dodaj_sladkor(self):
        self.kalorije += 500
        self.priljubljenost -= 1


class Hrana(Zivila):
    teza = None

    def __init__(self, ime, teza, kalorije, priljubljenost):
        super().__init__(ime, kalorije, priljubljenost)
        self.teza = teza

    def __repr__(self):
        return f"{self.ime} je tezek {self.teza}"



class Pijaca(Zivila):
    volumen = None

    def __init__(self, ime, volumen, kalorije, priljubljenost):
        self.volumen = volumen
        super().__init__(ime, kalorije, priljubljenost)


caj = Pijaca("Zeleni caj", 0.2, 200, 4)
pivo = Pijaca("Lasko", 0.5, 1600, 8)

krof = Hrana("Trojanski Krof", 0.25, 2000, 5)
obara = Hrana("Zasavski ajmoht", 0.5, 1100, 2)

print(krof.__dict__)


print(krof.kalorije)
krof.dodaj_sladkor()
print(krof.kalorije)

print(caj.priljubljenost)
caj.dodaj_sladkor()
print(caj.priljubljenost)