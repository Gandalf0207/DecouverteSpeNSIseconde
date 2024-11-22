# Exercice 2
# Boucles et collections : "Compteur de voyelles"

"""
Objectif : Travailler avec les boucles et les chaînes de caractères.
Concepts : for loop, chaînes de caractères, in pour tester la présence de caractères dans une liste.

------

Exercice : Écrire un programme qui demande une phrase à l’utilisateur et compte le nombre de voyelles dans celle-ci.
Après cela, il affichera les valeurs obtenues.

Exercice Avancé (facultatif) : Ajouter de nouveaux compteurs à votre programme : 
    - Contient un nombre entier ou à virgule : 2024 / 19.35
    - Contient des caractère spéciaux : *!?+(
    - Contient des consonnes : zqsd

Veillez à bien commenter et votre code !

Completer les éléments #...

"""

def Calculator(entree):

    entree = entree.lower() # Toute la est passé un minuscule pour pouvoi compter les voyelles Majuscule ex : "Apprendre" 
    listeVoyelle = ["#..."] # liste des voyelles en minuscule
    #...  # compteur de voyelle, valeur initiale : 0

    for caractere in #...: # Boucle qui parcourt chaque caractère de la phrase
        if #... in #... : # Si la valeur du caractère se trouve dans la liste des voyelles
            compteurVoyelle += 1 # On ajoute 1 au compteur
    
    return #.... # On renvoie le nombre de voyelle de cette phrase

entree = str(input("Votre phrase : "))
print("Il y a ", Calculator(entree), "voyelles")
