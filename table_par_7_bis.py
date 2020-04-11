# -*-coding:Latin-1 -*
import os  #On importe le module os, A mettre au tout d�but du programme


def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb
    de 1*nb � max*nb
    (max >= 0)"""

    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1
        
# On met le programme en pause pour �viter qu'il ne se referme (Windows)
os.system("pause")
