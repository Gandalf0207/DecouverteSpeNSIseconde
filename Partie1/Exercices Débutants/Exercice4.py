# Exercice 4
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

Completer les éléments #...

"""
from random import random, randint, choice

def MotDePasse(longueur):

    ListeLettres = #... # Liste des lettres
    ListeNombre = #... # Liste des nombres
    ListeCaractereAutre = #... # Liste des autres caractères / spéciaux 
    motDePasse = "" # Set du mot de passe (str vide)

    for i in #... : # Boucle qui a chaque tour va ajotuer un caractère au mot de passe
        choix = randint(0,10) # Choix d'un nombre pour sélectionner le type de caractère que l'on va ajouter
        if #... : # Si choix inférieur stric à 5 on ajoute une lettre
            if choice([True, False]): # Choix pour savoir si on ajoute une majuscule / minuscule
                motDePasse += choice(ListeLettres).upper() # ajout majuscule 
            else:
                motDePasse += choice(ListeLettres) # ajout majuscule 
        elif #... : # Si choix suppérieur ou égale à 5 et inférieur stric à 9 on ajoute un chiffre
            motDePasse += choice(ListeNombre) # ajout chiffre
        else: # Sinon on ajoute un caractère autre
            motDePasse += choice(ListeCaractereAutre) # ajout caractère autre

    return motDePasse # On revoie le mot de passe


longueur = #... # Demande de la longueur du mot de passe (int)

print(MotDePasse(longueur)) # Affichage + Appel de la fonction 
