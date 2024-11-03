# Aide 2
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
"""

# Exercice Aide

# Vous devez parcourir toute la chaine de caractère et comparer chaque caractère de cette chaine pour savoir si c'est une voyelle ou non.
# En python, la condition : "if value in ListeItem" avec value commme itérateur et ListeItem comme liste contenant différentes valeurs,
# permet de savoir si l'élément value se trouve ou non dans la liste.  
# Attention, une voyelle peut être au format majuscule et minuscule

def Calculator(entree):

    listeVoyelle = ["a", "e", "i", "o", "u", "y"] # liste des voyelles en minuscule
    
    # Boucle qui parcourt la chaine de caractère
    # Condition
    # Ajout de 1 au compteur
    
    return #...    On renvoie le nombre de voyelle de cette phrase

entree = str(input("Votre phrase : "))
print("Il y a ", Calculator(entree), "voyelles")




# Exercice Avancé Aide


# Il vous suffit d'ajouter de nouvelles vérifications avec de nouvelles listes de valeurs et de nouveaux compteurs...
# ex : 
listeConsonne = ["z", "r", "t", "p", "q", "s", "d", "f", "g", "h", "h", "j", "k", "l", "m", "w", "x", "c", "v", "b", "n"]
compteurConsonne = 0 # compteur de consonne, valeur initiale : 0
# ...