# Aufgabe 1
def remove_number_from_list(number_list, number):
    if number in number_list:
        number_list.remove(number)
    return number_list

my_list = [1, 2, 3, 4, 5]
input_number = int(input("Gib eine Zahl ein: "))

new_list = remove_number_from_list(my_list, input_number)
print("Neue Liste:", new_list)

# Aufgabe 2
def entferne_doppelte(zahlen_liste):
    einzigartige_zahlen = []
    for zahl in zahlen_liste:
        if zahlen_liste.count(zahl) == 1:
            einzigartige_zahlen.append(zahl)
    return einzigartige_zahlen

meine_liste = [1, 2, 3, 4, 4, 5, 6, 6, 7]
ergebnis = entferne_doppelte(meine_liste)
print("Liste nach Entfernen der doppelten Elemente:", ergebnis)

# Aufgabe3
def bubblesort(liste, aufsteigend=True):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if aufsteigend:
                if liste[j] > liste[j+1]:
                    liste[j], liste[j+1] = liste[j+1], liste[j]
            else:
                if liste[j] < liste[j+1]:
                    liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

unsortierte_liste = [64, 34, 25, 12, 22, 11, 90]
aufsteigend_sortiert = bubblesort(unsortierte_liste.copy())
absteigend_sortiert = bubblesort(unsortierte_liste.copy(), aufsteigend=False)

print("Aufsteigend sortierte Liste:", aufsteigend_sortiert)
print("Absteigend sortierte Liste:", absteigend_sortiert)

