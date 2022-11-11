# Pierre papier ciseaux 

# DEBUT 


# Importe la fonction random

# Definir 0 a la fonction points_joueur
# Definir 0 a la fonction points_ordinateur

# Definir la fonction regle 
    # Ecrire "La Pierre bat les Ciseaux" 
    # Ecrire "La Feuille bat la Pierre" 
    # Ecrire "Les Ciseaux battent la Feuille" 
    # Ecrire "Si vous et l'ordinateur avez le meme objet" 
    # Ecrire "Alors il y a egalite"
    # Ecrire "Et le premier a 10 il remporte la partie" 


# Definir la fonction choix_joueur avec pour parametre joueur 
    # Definir input de pierre, papier ou ciseaux a la fonction joueur 
    # Tant que joueur n'a pas entre pierre, papier ou ciseaux
        # Alors definir input de pierre papier et ciseaux a la fonction joueur 
    # Retourner la fonction joueur 
 

# Definir la fonction choix_ordinateur avec pour parametre nb et ordi
    # Definir un nombre aleatoire de 1 a 3 a la fonction nb
    # Si la fonction nb est egal a 1
        # Alors definir "pierre" à la fonction ordi
    # Sinon si la fonction nb est egal a 2
        # Alors definir "papier" à la fonction ordi
    # sinon
        # Alors definir "ciseaux" a la fonction ordi
    # Retourner la fonction ordi
 
# Ecrire la fonction choix_ordinateur

# si la fonction choix_joueur est egal à "pierre" et que la fonction choix_ordinateur est egal à "ciseaux" 
    # Alors ecrire "Vous gagnez 1 point." 
    # Definir points_joueur plus 1 a la fonction points_joueur 
# sinon si la fonction choix_joueur est egal à "pierre" et que la fonction choix_ordinateur est egal à "papier" 
    # Alors ecrire "L'ordinateur remporte 1 point." 
    # Definir points_ordinateur plus 1 a la fonction points_ordinateur 
# sinon si la fonction choix_joueur est egal à "pierre" et que la fonction choix_ordinateur est egal à "pierre" 
    # Alors ecrire "Dommage égalité."
 

# si la fonction choix_joueur est egal à "papier" et que la fonction choix_ordinateur est egal à "pierre" 
    # Alors ecrire "Vous gagnez 1 point."
    # Definir points_joueur plus 1 à la fonction points_joueur 
# sinon si la fonction choix_joueur est egal à "papier" et que la fonction choix_ordinateur est egal à "ciseaux " 
    # Alors ecrire "L'ordinateur remporte 1 point." 
    # Definir points_ordinateur plus 1 a la fonction points_ordinateur 
# sinon si la fonction choix_joueur est egal à "papier" et que la fonction choix_ordinateur est egal à "papier" 
    # Alors ecrire "Dommage égalité."

# si la fonction choix_joueur est egal à "ciseaux" et que la fonction choix_ordinateur est egal à "papier" 
    # Alors ecrire "Vous gagnez 1 point." 
    # Definir points_joueur plus 1 à la fonction points_joueur 
# sinon si la fonction choix_joueur est egal à "ciseaux" et que la fonction choix_ordinateur est egal à "pierre" 
    # Alors ecrire "L'ordinateur remporte 1 point." 
    # Definir points_ordinateur plus 1 a la fonction points_ordinateur 
# sinon si la fonction choix_joueur est egal à "ciseaux" et que la fonction choix_ordinateur est egal à "ciseaux" 
    # Alors ecrire "Dommage égalité."

# si la fonction points_ordinateur est egal a 10 
    # Alors ecrire "Dommage le résultat est de", points_ordinateur, "à", points_joueur
# Simon si la fonction points_joueur est egal a 10
    # Alors ecrire "Bravo tu a gagné avec un score de", points_joueur, "à", points_ordinateur

# FIN 
