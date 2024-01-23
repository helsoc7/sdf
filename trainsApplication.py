class Zug:
    def __init__(self, name):
        self.name = name
        self.waggons = []
        self.triebwagen = None
    def add_waggon(self, waggon):
        self.waggons.append(waggon)

    def set_triebwagen(self, triebswagen):
        self.triebwagen = triebswagen

    def __str__(self):
        return f"Zug {self.name} mit {len(self.waggons)} Waggons und Triebwagen {self.triebwagen.name}"
  
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
        self.freie_plaetze = 0

    def add_abteil(self, abteil):
        self.abteile.append(abteil)
        self.freie_plaetze += abteil.plaetze
    
    def buche_ticket(self):
        if self.freie_plaetze > 0:
            self.freie_plaetze -= 1
            return True
        else:
            return False


class Speisewagen(Waggon):
    def __init__(self, name):
        super().__init__(name)
  
class Abteil:
    def __init__(self, name, plaetze):
        self.name = name
        self.plaetze = plaetze
        
# Beispiel-Nutzung:

# Erstellen von Zügen, Triebwagen, Waggons und Abteilen
zug1 = Zug("Schnellzug")
triebwagen1 = DieselLok("Diesel-Triebwagen")
zug1.set_triebwagen(triebwagen1)

waggon1 = Gueterwaggon("G1")
waggon2 = Personenwaggon("P1")
waggon3 = Personenwaggon("P2")
waggon4 = Speisewagen("S1")

abteil1 = Abteil("Abteil1", 4)
abteil2 = Abteil("Abteil2", 6)

waggon2.add_abteil(abteil1)
waggon2.add_abteil(abteil2)

zug1.add_waggon(waggon1)
zug1.add_waggon(waggon2)
zug1.add_waggon(waggon3)
zug1.add_waggon(waggon4)

# Buchung von Tickets für Abteile im Personenwaggon
if waggon2.buche_ticket():
    print("Ticket für Abteil1 gebucht.")
else:
    print("Abteil1 ausgebucht.")
if waggon2.buche_ticket():
    print("Ticket für Abteil2 gebucht.")
else:
    print("Abteil2 ausgebucht.")
if waggon2.buche_ticket():
    print("Ticket für Abteil2 gebucht.")
else:
    print("Abteil2 ausgebucht.")

# Anzeigen der Informationen über den Zug und Waggons
print(zug1)
print("Waggons im Zug:")
for waggon in zug1.waggons:
    if isinstance(waggon, Personenwaggon):
        print(f"- {waggon.name} mit {len(waggon.abteile)} Abteilen ({waggon.freie_plaetze} freie Plätze)")
    else:
        print(f"- {waggon.name}")