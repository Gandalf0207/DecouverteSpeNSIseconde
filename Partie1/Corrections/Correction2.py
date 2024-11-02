# Correction 2
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

# Exercice Coreection 

def Calculator(entree):
    """ Fonction permettant de compter le nombre de voyelle dans une phrase, donnée par l'utilitateur.
    Cette fonction prend en entrée une phrase : donc une chaine de caractère (str).
    Cette fonction renvoie une valeur entière (int) : le nombre de voyelle dans la phrase.
    """

    entree = entree.lower() # Toute la est passé un minuscule pour pouvoi compter les voyelles Majuscule ex : "Apprendre" 
    listeVoyelle = ["a", "e", "i", "o", "u", "y"] # liste des voyelles en minuscule
    compteurVoyelle = 0 # compteur de voyelle, valeur initiale : 0

    for caractere in entree: # Boucle qui parcourt chaque caractère de la liste
        if caractere in listeVoyelle: # Si la valeur du caractère se trouve dans la liste des voyelles
            compteurVoyelle += 1 # On ajoute 1 au compteur
    
    return compteurVoyelle # On renvoie le nombre de voyelle de cette phrase

entree = str(input("Votre phrase : "))
print("Il y a ", Calculator(entree), "voyelles")



# Exercice Avancé Correction
def Calculator(entree):
    """ Fonction permettant de compter le nombre de voyelle, consonne, entier, caractère spéciaux... dans une phrase, donnée par l'utilitateur.
    Cette fonction prend en entrée une phrase : donc une chaine de caractère (str).
    Cette fonction affiche directement les résultats et ne retourne rien.
    """

    entree = entree.lower() # Toute la est passé un minuscule pour pouvoi compter les voyelles Majuscule ex : "Apprendre" 
    listeVoyelle = ["a", "e", "i", "o", "u", "y"] # liste des voyelles en minuscule
    listeConsonne = ["z", "r", "t", "p", "q", "s", "d", "f", "g", "h", "h", "j", "k", "l", "m", "w", "x", "c", "v", "b", "n"]
    listeNombre = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    compteurVoyelle = 0 # compteur de voyelle, valeur initiale : 0
    compteurConsonne = 0 # compteur de consonne, valeur initiale : 0
    compteurNombre = 0 # compteur de nombre, valeur initiale : 0
    compteurCaractereSpecial = 0 # compteur de caractère spécial, valeur initiale : 0

    for caractere in entree: # Boucle qui parcourt chaque caractère de la liste
        if caractere in listeVoyelle: # Si la valeur du caractère se trouve dans la liste des voyelles
            compteurVoyelle += 1 # On ajoute 1 au compteur
        elif caractere in listeConsonne: # Si la valeur du caractère se trouve dans la liste des consonnes
            compteurConsonne += 1 # On ajoute 1 au compteur
        elif caractere in listeNombre: # Si la valeur du caractère se trouve dans la liste des nombre
            compteurNombre += 1 # On ajoute 1 au compteur
        else: # Si la valeur du caractère ne se trouve dans aucune liste, il s'agit d'un caractère spécial...
            compteurCaractereSpecial +=1 # On ajoute 1 au compteur

    print(f"Il y a : \n    Voyelles(s) :{compteurVoyelle} \n    Consonne(s) : {compteurConsonne} \n    Nombre(s) : {compteurNombre} \n    Carctère(s) Autre(s) / Spécial.aux : {compteurCaractereSpecial}")
    
    return None

entree = str(input("Votre phrase : "))
Calculator(entree)