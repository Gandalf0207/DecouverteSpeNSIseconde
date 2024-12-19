# Exercice 2
# Boucles et collections : "Compteur de voyelles"

"""
Objectif : Travailler avec les boucles et les chaînes de caractères.
Concepts : for loop, chaînes de caractères, in pour tester la présence de caractères dans une liste.

------

Exercice : Écrire un programme qui demande une phrase à l’utilisateur et compte le nombre de voyelles dans celle-ci.
Après cela, il affichera les valeurs obtenues.

Veillez à bien commenter et votre code !

Completer les éléments #...

"""

entree = str(input("Votre phrase : "))

entree = entree.lower() # Toute la chaine est passé un minuscule pour pouvoir compter les voyelles Majuscule ex : "Apprendre"  = "apprendre"
listeVoyelle = ["", "", ""] # liste des voyelles en minuscule
compteurVoyelle = 0  # Compteur de voyelle, valeur initiale : 0

for caractere in #...: # Boucle qui parcourt chaque caractère de la phrase
    if #... in #... : # Si la valeur du caractère se trouve dans la liste des voyelles
        compteurVoyelle = compteurVoyelle + 1 # On ajoute 1 au compteur
print("Il y a ", #... , "voyelles")


