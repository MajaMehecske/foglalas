from abc import ABC
from datetime import datetime

class Szoba(ABC):
    def __init__(self, ar, sz_szam):
        self.ar = ar
        self.sz_szam = sz_szam
        self.foglalt_idopontok = []

    def foglalhato_e(self,datum):
        if datum >= datetime.now().strftime('%Y-%m-%d'):
            if datum not in self.foglalt_idopontok:
                self.foglalt_idopontok.append(datum)
                print('Sikeres foglalás! Köszönjük, hogy a Száll-ide Szállodát választotta :)')
                return True
            else:
                print('Sajnáljuk, ezt a szobát már lefoglalták aznapra.')
                return False
        else:
            print('Sajnáljuk, jelenlegi technikánk nem biztosítja a szobák múltba való foglalását. Amennyiben időutazó, kérjük előbb utazzon vissza annyit az időben, hogy a megadott dátum még a jövőben legyen.')
            return False
        
    def lemondas(self, datum):
        if datum in self.foglalt_idopontok:
            self.foglalt_idopontok.remove(datum)
            print('Sikeresen lemondta ', datum, '-ei foglalását.')
            return True
        else:
            print('A megadott dátumra még nincsen lefoglalva a szoba.')
            return False
    def szoba_foglalasai(self):
        if self.foglalt_idopontok:
            print('A',self.sz_szam, 'szoba lefoglalt időpontjai:')
            for nap in self.foglalt_idopontok:
                print(nap)
        else:
            print('Nincs foglalás a', self.sz_szam, 'szobára')

class EgyAgyas(Szoba):
    def __init__(self, sz_szam):
        super().__init__(ar = 10000, sz_szam = sz_szam)


class KetAgyas(Szoba):
        def __init__(self, sz_szam):
            super().__init__(ar = 20000, sz_szam = sz_szam)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.egyagyas_szobak = []
        self.ketagyas_szobak = []

    def bovites_egyagyas(self, szoba):
        self.egyagyas_szobak.append(szoba)
    def bovites_ketagyas(self, szoba):
        self.ketagyas_szobak.append(szoba)

    def foglalas(self, datum):
        print('')
        print('Az aznap még rendelkezésre álló szobáink listája a következő:')
        print('Egyágyas lefoglalható szobáink:')
        for szoba in self.egyagyas_szobak:
            if datum not in szoba.foglalt_idopontok:
                print('Szobaszám:',szoba.sz_szam, '- Ár:', szoba.ar)
        print('Kétágyas lefoglalható szobáink:')
        for szoba in self.ketagyas_szobak:
            if datum not in szoba.foglalt_idopontok:
                print('Szobaszám:',szoba.sz_szam, '- Ár:', szoba.ar)
        sz_szam = input('Melyik szobát szeretné lefoglalni?')
        for szoba in self.egyagyas_szobak:
            if szoba.sz_szam == sz_szam:
                return szoba.foglalhato_e(datum)
        for szoba in self.ketagyas_szobak:
            if szoba.sz_szam == sz_szam:
                return szoba.foglalhato_e(datum)
        print('Nincs ilyen szobája szállodánknak.')
        return False

    def szoba_lemondas(self,datum):
        sz_szam = input("Melyik szoba foglalását szeretné lemondani?")
        for szoba in self.egyagyas_szobak:
            if szoba.sz_szam == sz_szam:
                return szoba.lemondas(datum)
        for szoba in self.ketagyas_szobak:
            if szoba.sz_szam == sz_szam:
                return szoba.lemondas(datum)
        print('Nincs ilyen szobája szállodánknak.')
        return False    

    def foglalasok_listazasa(self):
        for szoba in self.egyagyas_szobak:
            Szoba.szoba_foglalasai(szoba)
        for szoba in self.ketagyas_szobak:
            Szoba.szoba_foglalasai(szoba)

def szalloda_szobai():
    
    szalloda = Szalloda("Száll-ide Szálloda")

    szoba1 = EgyAgyas("101")
    szoba2 = EgyAgyas("102")
    szoba3 = KetAgyas("201")

    szalloda.bovites_egyagyas(szoba1)
    szalloda.bovites_egyagyas(szoba2)
    szalloda.bovites_ketagyas(szoba3)
    
    szoba1.foglalt_idopontok.append("2024-05-18")
    szoba1.foglalt_idopontok.append("2024-07-30")
    szoba2.foglalt_idopontok.append("2025-05-23")
    szoba2.foglalt_idopontok.append("2024-06-13")
    szoba3.foglalt_idopontok.append("2024-09-10")

    return szalloda

def main():
    szallide = szalloda_szobai()
    print('')
    print('Üdvözöljük! :)')
    print('Ön a Száll-ide Szálloda ügyintézési felületét látja. A szobák foglalásához, lemondásához, valamint a foglalások listázásához használja a következő kódokat:')

    while True:
        print("\nF - Szoba foglalása")
        print("L - Szoba lemondása")
        print("FL - Foglalások listázása")
        print("KI - Kilépés")
        print('')


        aktualis = input("Miben lehetünk a segítségére?")

        if aktualis == "F":
            datum = input("Adja meg, mikorra szeretne foglalni (év-hónap-nap formátumban):")
            szallide.foglalas(datum)
        elif aktualis == "L":
            datum = input("Adja meg, mikori foglalását szeretné lemondani (év-hónap-nap formátumban):")
            szallide.szoba_lemondas(datum)
        elif aktualis == "FL":
            szallide.foglalasok_listazasa()
        elif aktualis == "KI":
            print('Köszönjük, hogy a Száll-ide Szállodát választotta, reméljük elégedett volt ügyintézési szolgáltatásunkkal.')
            print('Viszont látásra! :)')
            break
        else:
            print("Kérem a fent megadott opciók közül válasszon")

if __name__ == "__main__":
    main()
