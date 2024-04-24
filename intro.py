import math
import random

print("Geben Sie bitte die Zeit in Minuten in: ")
zeitraum = float(input())

stunden =  int(zeitraum // 60)
minuten =  int(zeitraum % 60)
sekunden = int((zeitraum % 1) *60)
print(f"{stunden}h {minuten}m {sekunden}sec")

geheime_zahl = random.randint(1, 100)

while True:
    eingabe = input("Errate die geheime Zahl (1-100): ")

    if eingabe.isdigit():
        versuch = int(eingabe)

        if 1 <= versuch <= 100:
            if versuch == geheime_zahl:
                print("Glückwunsch! Du hast die geheime Zahl erraten.")
                break
            elif versuch < geheime_zahl:
                print("Die geheime Zahl ist größer als deine Eingabe.")
            else:
                print("Die geheime Zahl ist kleiner als deine Eingabe.")
        else:
            print("Bitte gib eine Zahl zwischen 1 und 100 ein.")
    else:
        print("Bitte gib eine gültige Zahl ein.")

