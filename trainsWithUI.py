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


import tkinter as tk
from tkinter import messagebox

# Hier fügen Sie Ihre Klassen und Methoden aus Ihrem vorherigen Code ein

# Funktion zur Buchung eines Tickets
def buche_ticket():
    success = waggon2.buche_ticket()
    if success:
        messagebox.showinfo("Buchung erfolgreich", "Ticket erfolgreich gebucht.")
    else:
        messagebox.showwarning("Buchung fehlgeschlagen", "Das Abteil ist ausgebucht.")

# Erstellung des Hauptfensters
root = tk.Tk()
root.title("Zugbuchung")

# Labels und Schaltflächen zur Benutzeroberfläche hinzufügen
label = tk.Label(root, text="Willkommen zur Zugbuchung")
label.pack(pady=10)

buchung_button = tk.Button(root, text="Ticket buchen", command=buche_ticket)
buchung_button.pack(pady=5)

info_label = tk.Label(root, text="Informationen zum Zug:")
info_label.pack(pady=5)

info_text = tk.Text(root, height=10, width=40)
info_text.pack()

# Funktion zur Anzeige von Informationen
def zeige_informationen():
    zug_info = str(zug1) + "\nWaggons im Zug:\n"
    for waggon in zug1.waggons:
        if isinstance(waggon, Personenwaggon):
            zug_info += f"- {waggon.name} mit {len(waggon.abteile)} Abteilen ({waggon.freie_plaetze} freie Plätze)\n"
        else:
            zug_info += f"- {waggon.name}\n"
    info_text.delete(1.0, tk.END)
    info_text.insert(tk.END, zug_info)

info_button = tk.Button(root, text="Zeige Informationen", command=zeige_informationen)
info_button.pack(pady=5)

# Funktion zum Beenden der Anwendung
def beenden():
    root.destroy()

beenden_button = tk.Button(root, text="Beenden", command=beenden)
beenden_button.pack(pady=5)

# Starten der GUI
root.mainloop()