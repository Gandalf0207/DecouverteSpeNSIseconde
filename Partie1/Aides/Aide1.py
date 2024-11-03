# Aide 1 
# Calculs de base : "Le convertisseur de température"

"""
Objectif : Utiliser des opérations mathématiques et manipuler les données.
Concepts : Opérations arithmétiques, conditions (if, else), formatage des résultats.

------

Exercice : Écrire un programme qui convertit une température en Celsius en Fahrenheit (et inversement) et qui renvoit cette nouvelle valeur pour qu'elle soit affichée. 
Les élèves peuvent choisir s’ils saisissent des °C ou des °F. Completer le script suivant.

Exercice Avancé (facultatif) : Documenter à l'aide de docstrings et commentaires votre programme. 

Veillez à bien commenter et votre code !s
"""



# Vous devez prendre en compte le type de mesure de temperature pour pouvoir déterminer quel calcul effectuer. 
# En fonction du typed de temperature donc, affectuer une comparaison pour appliquer la bonne méthode de calcul.

def Convertisseur(temperatureType, temperature):

    if temperatureType == 1: # Si la température d'entrée est en Celsius
        pass
    
    elif temperatureType == 2: # Si la température d'entrée est en Fahrenheit
        pass

    
temperatureType = None #Choix du type de mesure en entrée
temperature = float(input("Votre temperature d'entrée : ")) # Valeur à convertir

print(Convertisseur(temperatureType, temperature)) # Affichage + Appel de la fonction de conversion avec les valeurs de l'utilisateur