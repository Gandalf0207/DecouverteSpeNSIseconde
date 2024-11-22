# Correction 1 
# Calculs de base : "Le convertisseur de température"

def Convertisseur(temperatureType, temperature):
    """ Fonction permettant de convertir la température donné par l'utilisateur en C° ou °F selon le choix de ce dernier.
    Cette fonction prend en entrée : le type de tempétature envoyé (Celsius ou Fahrenheit) sous forme de valeur entière : 1 et 2
    Cette fonction renvoie une F string contenant les information d'entrées et de sorties selon le choix.
    """

    if temperatureType == 1: # Si la température d'entrée est en Celsius
        newTemperature = temperature *9/5 + 32 # Conversion des C° en °F
        return f"{temperature} C° = {newTemperature} °F" # Retour des valeurs attendus
    
    elif temperatureType == 2: # Si la température d'entrée est en Fahrenheit
        newmTeperature = (temperature - 32) * 5/9 # Conversion des °F en C°
        return f"{temperature} °F = {newTemperature} C°" # Retour des valeurs attendus
    
    else: # Si la valeur du type de température est différente des entrées possibles
        print("L'entrée est invalide, veillez sélectionner un bon type de temperature") # On affiche un information d'erreur
        return None 
    
temperatureType = int(input("Valeur sasie en : \n   Celsius : 1 \n    Fahrenheit : 2 \n\n> :")) # Choix du type de la valeur saisie (Celcius ou Fahrenheit)
temperature = float(input("Votre temperature d'entrée : ")) # Valeur à convertir

print(Convertisseur(temperatureType, temperature)) # Affichage + Appel de la fonction de conversion avec les valeurs de l'utilisateur