import sys

from parsing import *
from turing import *
from parsing import *


def un_pas_calcul(config, turing):
    save2 = []
    liste_turing = [turing.etat_courant, turing.tete_lecture]

    for i in range(len(config.liste_lecture)):
        save = config.liste_lecture[i].split(',')
        if save == liste_turing:
            save2 = config.liste_ecriture[i].split(',')
            turing.etat_courant = save2[0]
            break

    liste_turing = save2

    print("PAS DE CALCUL ")
    print()
    print("L'état courant est :", turing.etat_courant)
    print("La tête de lecture est : ", turing.tete_lecture)
    # print("save2:", save2)
    print()
    # print("liste turing, ", liste_turing)
    # print(config.liste_lecture)
    # print(config.liste_ecriture)

    # print(turing.bande)
    return liste_turing


def calcul(config, turing):
    for i in range(len(turing.bande)):
        liste_turing = un_pas_calcul(config, turing)
        print("chemin ", liste_turing)

        if turing.etat_courant == turing.qaccept and turing.tete_lecture == '_':
            # print("final", liste_turing[0])
            print("La tête est deplacé sur  : ", turing.tete_lecture)
            print("FIN ACCEPTÉ")
            break

        if '>' == liste_turing[2]:
            print("La tête de lecture avant est : ", turing.tete_lecture)
            turing.bande[i] = liste_turing[1]
            turing.tete_lecture = turing.bande[i + 1]
            print("bande i+1", turing.bande[i + 1])
        if '<' == liste_turing[2]:
            print("La tête de lecture avant est : ", turing.tete_lecture)
            turing.bande[i] = liste_turing[1]
            turing.tete_lecture = turing.bande[i - 1]
            print("bande i-1", turing.bande[i - 1])

        if turing.etat_courant != turing.qaccept and turing.tete_lecture == '_' and i == range(len(turing.bande)):
            print("final", liste_turing[0])
            print("La tête est deplacé sur  : ", turing.tete_lecture)
            print("FIN NON ACCEPTÉ")
            sys.exit()

        print("Nous ecrivons un : ", liste_turing[1])
        print("Nous passons sur l'état :", turing.etat_courant)
        print("La tête est deplacé sur  : ", turing.tete_lecture)
        print("Bande calcul", turing.bande)
        print()
