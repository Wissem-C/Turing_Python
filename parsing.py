from turing import *


class Configuration:
    def __init__(self, liste_lecture=None, liste_ecriture=None):
        if liste_ecriture is None:
            liste_ecriture = []
        if liste_lecture is None:
            liste_lecture = []
        self.liste_lecture = liste_lecture
        self.liste_ecriture = liste_ecriture

        # "A, 0"
        # "A, 0, >"


def parse_description(elm, fic):
    fichier = open(fic, "r")
    lecture = fichier.readlines()

    b = ' '

    for line in lecture:
        # print(line.strip())
        if elm in line:
            line = line.split()
            a = line[1:]
            b = b.join(a)

        if elm in line:
            line = line.split()
            a = line[1:]
            b = b.join(a)

        if elm in line:
            line = line.split()
            a = line[1:]
            b = b.join(a)

    fichier.close()
    return b


def parse_configuration(fic):
    fichier = open(fic, "r")
    lecture = fichier.readlines()[3:]
    liste_lecture = []
    liste_ecriture = []

    # print(lecture)

    for i in range(len(lecture)):

        if any('>' in string for string in lecture[i]) or any('<' in string for string in lecture[i]) or any(
                '-' in string for string in lecture[i]):

            liste_ecriture.append(lecture[i].strip())

        else:
            liste_lecture.append(lecture[i].strip())

    config = Configuration(liste_lecture, liste_ecriture)
    fichier.close()
    return config
