# rock_paper_scissors
from random import *
 
def choix_utilisateur():
    """Cette fonction permet au joueur de choisir son mouvement"""
    joueur = input("Pierre\nPapier\nCiseaux\n")
    while joueur not in ["pierre","papier","ciseaux"]:
        joueur = input("pierre\npapier\nciseaux\n")
    return(joueur)
 
def choix_ordinateur():
    """Cette fonction permet à l'ordinateur de générer aléatoirement un mouvement"""
    n = randint(1,3)
    if n == 1:
        ordi = "pierre"
    elif n==2:
        ordi = "papier"
    else:
        ordi = "ciseaux"
    return(ordi)
 
a = choix_utilisateur()
b = choix_ordinateur()
print(b)
if a == "pierre" and b == "ciseaux":
    print("Vous avez gagne.")
elif a == "pierre" and b == "papier":
    print("Vous avez perdu.")
elif a == "pierre" and b == "pierre":
    print("Egalite.")
 
if a == "papier" and b == "pierre":
    print("Vous avez gagne.")
elif a == "papier" and b == "ciseaux":
    print("Vous avez perdu.")
elif a == "papier" and b == "papier":
    print("Egalite.")
 
if a == "ciseaux" and b == "papier":
    print("Vous avez gagne.")
elif a == "ciseaux" and b == "pierre":
    print("Vous avez perdu.")
elif a == "ciseaux" and b == "ciseaux":
    print("Egalite.")
