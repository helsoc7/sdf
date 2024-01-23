class Zug:
    def __init__(self, name):
        self.name = name
        self.waggons = []
        self.triebwagen = None
    def add_waggon(self, waggon):
        self.waggons.append(waggon)

    def set_triebwagen(self, triebswagen):
        self.triebwagen = triebswagen

class Triebwagen:
    def __init__(self, name):
        self.name = name

class DieselLok(Triebwagen):
    def __init__(self, name):
        super().__init__(name)


class ELok(Triebwagen):
    def __init__(self, name):
        super().__init__(name)
  
class Waggon:
    def __init__(self, name):
        self.name = name
  
class Gueterwaggon(Waggon):
    def __init__(self, name):
        super().__init__(name)


class Personenwaggon(Waggon):
    def __init__(self, name):
        super().__init__(name)
        self.abteile = []

    def add_abteil(self, abteil):
        self.abteile.append(abteil)
    



class Speisewagen(Waggon):
    def __init__(self, name):
        super().__init__(name)
  
class Abteil:
    def __init__(self, name, plaetze):
        self.name = name
        
# Beispiel-Nutzung:

zug1 = Zug("Schnellzug")
triebwagen1 = DieselLok("Diesel-Triebwagen")
zug1.set_triebwagen(triebwagen1)

waggon1 = Gueterwaggon("G1")
waggon2 = Personenwaggon("P1")
waggon3 = Personenwaggon("P2")
waggon4 = Speisewagen("S1")

abteil1 = Abteil("Abteil1")
abteil2 = Abteil("Abteil2")

waggon2.add_abteil(abteil1)
waggon2.add_abteil(abteil2)

zug1.add_waggon(waggon1)
zug1.add_waggon(waggon2)
zug1.add_waggon(waggon3)
zug1.add_waggon(waggon4)

print("Zugname:", zug1.name)
print("Triebwagen:", zug1.triebwagen.name)
print("Waggons:")
for waggon in zug1.waggons:
    print("-", waggon.name)
    if isinstance(waggon, Personenwaggon):
        print("  Abteile:")
        for abteil in waggon.abteile:
            print("  -", abteil.name)