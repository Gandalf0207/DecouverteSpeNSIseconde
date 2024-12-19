# Exercice 1 
# Calculs de base : "Le convertisseur de température"

"""
Objectif : Utiliser des opérations mathématiques et manipuler les données.
Concepts : Opérations arithmétiques, conditions (if, else), formatage des résultats.

------

Exercice : Écrire un programme qui convertit une température en Celsius en Fahrenheit (et inversement) et qui renvoit cette nouvelle valeur pour qu'elle soit affichée. 
Les élèves peuvent choisir s’ils saisissent des °C ou des °F. Completer le script suivant.

Completer les éléments ...

Formule de conversion des degrés Celsius en degrés Farenheit : C° * 9/5 + 32 = °F

"""
temperatureType = int(input("Valeur saisie en : \n   Celsius : 1 \n    Fahrenheit : 2 \n\n> :")) # Choix du type de la valeur saisie (Celcius ou Fahrenheit)
temperature = #... # Valeur à convertir
if #... : # Comparaison temperature en Celsius
    newTemperature = # ...     # C° ->  °F
    print(temperature, "C° = ", newTemperature, "F°"
    
elif #... : # Comparaison temperature en Fahrenheit
    newTemperature = #...    # °F -> C°
    print(temperature, "F° = ", newTemperature, "C°"
    
else: # Si la valeur du type de température est différente des entrées possibles
    print("...") # On affiche un information d'erreur
