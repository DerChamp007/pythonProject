class Aufgaben:

    def fehlerbehandlung(self, wert):
        try:
            zahl = int(wert)
            print("Der Wert wurde erfolgreich in eine Ganzzahl umgewandelt:", zahl)
            ergebnis = 10 / zahl
            print("10 geteilt durch den Wert ergibt:", ergebnis)
            liste = [1, 2, 3]
            print("Zugriff auf das Element der Liste:", liste[zahl])
        except ValueError:
            print("ValueError: Der Wert konnte nicht in eine Zahl umgewandelt werden.")
        except ZeroDivisionError:
            print("ZeroDivisionError: Division durch Null ist nicht erlaubt.")
        except IndexError:
            print("IndexError: Ungültiger Index beim Zugriff auf die Liste.")
        except Exception as e:
            print("Ein anderer Fehler ist aufgetreten:", type(e).__name__)

    def string_zu_bits_verschieben(self, text):
        modifizierter_text = ''
        for char in text:
            modifiziertes_char = chr(ord(char) << 1)
            modifizierter_text += modifiziertes_char
        return modifizierter_text

    def bits_zu_string_verschieben(self, modifizierter_text):
        original_text = ''
        for char in modifizierter_text:
            originales_char = chr(ord(char) >> 1)
            original_text += originales_char
        return original_text

    def alle_bits_unterschiedlich(self, zahl1, zahl2):
        xor = zahl1 ^ zahl2
        return xor == (zahl1 | zahl2)


aufgaben = Aufgaben()

# Aufgabe 5.1:
aufgaben.fehlerbehandlung("abc")
aufgaben.fehlerbehandlung(0)
aufgaben.fehlerbehandlung(5)

# Aufgabe 5.2:
text = "Hallo"
modifiziert = aufgaben.string_zu_bits_verschieben(text)
print("Modifizierter Text:", modifiziert)
original = aufgaben.bits_zu_string_verschieben(modifiziert)
print("Ursprünglicher Text:", original)

# Aufgabe 5.3:
print(aufgaben.alle_bits_unterschiedlich(5, 10))
print(aufgaben.alle_bits_unterschiedlich(5, 5))

