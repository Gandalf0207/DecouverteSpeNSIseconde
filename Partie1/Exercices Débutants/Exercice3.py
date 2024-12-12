# Exercice 3
# Introduction aux listes et aux fonctions : "Moyenne finale"

"""
Objectif : Comprendre l’importance des fonctions et des listes.
Concepts : Listes, boucles (for), fonctions (def), calculs statistiques simples.

-----

Exercice : Demander à l’utilisateur le nombre de note et de matière, qu'il devra entrer par la suite, 
calculer la moyenne et afficher la note finale.

Exercice Avancé (facultatif) : Après avoir calculer la moyenne avec 2 notes ou plus,
votre programme devra afficher à la suite :
    - la note la plus haute
    - la plus basse
    - la médianne
    - l'étendu de ce groupe de note.
Il est conseillé d'utiliser les listes python pour les plus avancés

Veillez à bien commenter et votre code !

Completer les éléments #...

"""

"""
Aide Listes :
- Pour ajouter des valeurs à une liste on utilise la méthode .append(valeurs)
- Pour parcourir une liste, on utilise une boucle for, par exemple : 

    listeNote = [18,17,20]
    for note in listeNote:
        print(Note)

    >>> 18
    >>> 17
    >>> 20

Exemples : 

    liste = []
    print(liste)
    >>> []

    liste.append("Hello World")
    liste.append(15)
    print(liste)
    >>> ["Hello World", 15]

"""

def BulletinsDeNotes(notes):
    # Calcus de la moyenne : 
    nbNote = len(notes) # Nombre de note 
    #...  # Total des notes additionnés, par défaut  : 0
    for note in #... : # Boucle qui va additionner toutes les notes.
        total += #...

    moyenne = #... / #...  # Calcul de la moyenne


    print(f"Moyenne = {round(#..., 2)}")   # Afffichage de la moyenne avec un arrondis au centième près 
    return None



nombreNote = int(input("Nombre de note : ")) # Nombre de note attendu
listeNote = [] # Liste qui va contenir les notes


for note in #... : # Boucle de la longueur du nombre de note
    newNote = float(input(f"Note {note + 1} : ")) # Nouvelle note
    listeNote.append(#...) # Ajout de la nouvelle note


BulletinsDeNotes(listeNote)
