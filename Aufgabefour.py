def berechne_dreieck(katheten):
    a = katheten[0] 
    b = katheten[1]  
    hypotenuse = (a ** 2 + b ** 2) ** 0.5 
    flaecheninhalt = (a * b) / 2 
    return (a, b, hypotenuse, flaecheninhalt)

katheten = (3.0, 4.0)
ergebnis = berechne_dreieck(katheten)
print("Katheten: " + str(ergebnis[0]) + " und " + str(ergebnis[1]) +
      ", Hypotenuse: " + str(ergebnis[2]) +
      ", Flächeninhalt: " + str(ergebnis[3]))

def pruefe_liste_gegen_dict(liste, dictionary):
    for wert in liste:
        if wert in dictionary:
            print("Gefunden: " + wert + " -> " + dictionary[wert])
        else:
            print("Key " + wert + " ist nicht im Dictionary vorhanden.")

liste = ['Apfel', 'Banane', 'Kirsche', 'Pfirsich']
dictionary = {'Apfel': 'Apple', 'Banane': 'Banana', 'Kirsche': 'Cherry'}
pruefe_liste_gegen_dict(liste, dictionary)


def kombiniere_dictionaries(dict1, dict2):
    gemeinsames_dict = {}
    for key in dict1:
        if key in dict2:  
            gemeinsames_dict[key] = (dict1[key], dict2[key]) 
    return gemeinsames_dict


dict1 = {'Haus': 'House', 'Baum': 'Tree', 'Auto': 'Car'}
dict2 = {'Haus': 'Maison', 'Auto': 'Voiture', 'Hund': 'Chien'}
ergebnis = kombiniere_dictionaries(dict1, dict2)
for key in ergebnis:
    print("Key: " + key + " -> Werte: " + str(ergebnis[key]))
