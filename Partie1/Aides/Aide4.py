# Aide 4
# Mini-application : "Le générateur de mots de passe"

"""
Objectif : Travailler avec des fonctions et des manipulations de chaînes de caractères.
Concepts : Listes, fonctions, bibliothèque random, boucles.

-----

Exercice : Créer un programme qui génère un mot de passe aléatoire à partir d’une combinaison de lettres,
chiffres et caractères spéciaux de la longueur souhaité par l'utilisateur.

Exercice Avancé (facultatif) : Créer une méthode de force brut, ayant pour objectif de trouver un mot de passe donné par l'utilisateur. 
En déduire une explication sur la robustesse des mots de passe.

Veillez à bien commenter et votre code !
"""

# Exercice Aide

# Vous devez créer vos différentes listes de valeurs : lettres, nombres, caractères spéciaux...
# Votre mot de passe doit etre le la longueur donné par l'utilisateur,
# il vous faut donc utiliser une boucle pour ajouter le bon nombre de caractère à votre mot de passe

# Afin d'ajouter une variété de position des caractères, vous pouvez sélectionner diférents
# nombres choisis aléatoirement pour prendre une valeur dans les liste correspondente.


from random import random, randint, choice

def MotDePasse(longueur):


    ListeLettres = ["a", "e", "i", "o", "u", "y", "z", "r", "t", "p", "q", "s", "d", "f", "g", "h", "h", "j", "k", "l", "m", "w", "x", "c", "v", "b", "n"] # Liste des lettres
    # ...

    motDePasse = None
    # Création du mot de passe
    # Boucle
    choix = randint(0,10) # Choix d'un nombre pour sélectionner le type de caractère que l'on va ajouter
    if choix < 5: #...
        pass
    # ...

    return motDePasse # On revoie le mot de passe


longueur = int(input("Longueur du mot de passe : ")) # Récupération de la longueur 
print(MotDePasse(longueur)) # Affichage + Appel de la fonction 



# Exercice Avancé Aide
# ///