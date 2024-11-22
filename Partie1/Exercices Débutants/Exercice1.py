# Exercice 1 
# Calculs de base : "Le convertisseur de température"

"""
Objectif : Utiliser des opérations mathématiques et manipuler les données.
Concepts : Opérations arithmétiques, conditions (if, else), formatage des résultats.

------

Exercice : Écrire un programme qui convertit une température en Celsius en Fahrenheit (et inversement) et qui renvoit cette nouvelle valeur pour qu'elle soit affichée. 
Les élèves peuvent choisir s’ils saisissent des °C ou des °F. Completer le script suivant.

Exercice Avancé (facultatif) : Documenter à l'aide de docstrings et commentaires votre programme. 

Veillez à bien commenter et votre code !

Completer les éléments #...

Formule de conversion des degrés Celsius en degrés Farenheit : C° * 9/5 + 32 = °F

"""

def Convertisseur(temperatureType, temperature):
    if #... : #Temperature en Celsius
        newTemperature = # ...     # C° ->  °F
        return f"{#... } C° = {#...} °F"
    
    elif #... : # Temperature en Fahrenheit
        newTemperature = #...    # °F -> C°
        return f"{#...} °F = {#...} C°" 
    
    else: # Si la valeur du type de température est différente des entrées possibles
        print("#...") # On affiche un information d'erreur
        return None  

temperature = None

temperatureType = int(input("Valeur sasie en : \n   Celsius : 1 \n    Fahrenheit : 2 \n\n> :")) # Choix du type de la valeur saisie (Celcius ou Fahrenheit)
temperature = # ... # Valeur à convertir

print(Convertisseur(temperatureType, temperature)) # Affichage + Appel de la fonction de conversion avec les valeurs de l'utilisateur