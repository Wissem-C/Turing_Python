#!/usr/bin/env python3
import sys

from parsing import *
from turing import *
from calcul import *

# Initilise l'objet machine turing avec le parsing de fichier pour recuperer les elements correspondant
# turing = initilisation_mt("mt.txt")
# turing2 = initilisation_mt("mt2.txt")
# turing3 = initilisation_mt("mt3.txt")

# affiche_config_mt(turing)
# affiche_config_mt(turing2)
# affiche_config_mt(turing3)

# config = parse_configuration("mt.txt")
# config2 = parse_configuration("mt2.txt")
# config3 = parse_configuration("mt3.txt")

# print("voici la liste lecture ", config2.liste_lecture)
# print("voici la liste ecriture ", config2.liste_ecriture)

# print("Début d'un premier pas de calcul : ")
# print("L'etat courant pour démarrer est ", turing.etat_courant)
# print("La tête de lecture est : ", turing.tete_lecture)
# print("Bande avant calcul", turing.bande)
# print()

# un_pas_calcul(config, turing)
# affiche_config_mt(turing)
# calcul(config, turing)
# a = int(sys.argv[1])
# b = int(sys.argv[2])

# affiche_config_mt(turing2)
j = 1
while j < 4:
    print("DÉBUT DE LA", j, "EME MACHINE DE TURING")
    turing = initilisation_mt(sys.argv[j])
    config = parse_configuration(sys.argv[j])
    affiche_config_mt(turing)
    calcul(config, turing)
    j += 1

# config1 = parse_configuration(sys.argv[1])
# config2 = parse_configuration(sys.argv[2])
# config3 = parse_configuration(sys.argv[3])
# calcul(config1, turing)
# calcul(config2, turing)
# calcul(config3, turing)


# turing = initilisation_mt("mt3.txt")
# config = parse_configuration("mt3.txt")
# calcul(config, turing)

# 01001
