from enum import Enum

import parsing
from parsing import *


class Direction(Enum):
    DROITE = '>'
    GAUCHE = '<'
    RESTE = '-'


class Machine_Turing:

    def __init__(self, nom, init, qaccept, mot, bande, tete_lecture, etat_courant):
        self.mot = mot
        self.nom = nom
        self.init = init
        self.qaccept = qaccept
        self.bande = bande
        self.tete_lecture = tete_lecture
        self.etat_courant = etat_courant


def affiche_bande(bande):
    print(bande)


def initilisation_mt(fic):
    res = input("Entrez un mot voulu pour la machine de turing : ")
    bande = initilisation_bande(res)
    nom = parsing.parse_description("name", fic)
    etat_initial = parsing.parse_description("init", fic)
    etat_final = parsing.parse_description("accept", fic)
    tete_de_lecture = bande[0]
    etat_courant = etat_initial

    turing = Machine_Turing(nom, etat_initial, etat_final, res, bande, tete_de_lecture, etat_courant)
    return turing


def initilisation_bande(mot):
    lst = ['_'] * len(mot)

    for i in range(len(mot)):
        lst.insert(i, mot[i])

    return lst


def affiche_config_mt(turing):
    print("Mot d'entré pour la machine de turing : ", turing.mot)
    print("Nom de la machine de turing : ", turing.nom)
    print("Etat inital : ", turing.init)
    print("Etat acceptant : ", turing.qaccept)
    print("Initialisation de la bande avec le mot d'entrée : ", turing.bande)
    print("Etat courant", turing.etat_courant)
    print("Tête de lecture", turing.tete_lecture)
