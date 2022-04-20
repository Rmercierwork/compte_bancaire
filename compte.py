from abc import ABC

class compte_bancaire(ABC):
    '''Classe abstraite, servant de base pour les classes compte enfant'''
    def __init__(self, nom_proprietaire, solde):
        '''Il s'agit du contructeur par défaut '''
        self._numero_compte = 123
        self._nom_proprietaire = nom_proprietaire
        self._solde = solde


    def retrait(self, argent_retire):
        '''Méthode servant à retirer de l'argent, vérifie si le solde est dans le négatif, auquel cas l'opération est impossible
        Retourne à l'utilsateur son solde et la valeur qu'il veut retirer'''
        if self._solde <= 0:
            print("Votre solde est de :", self._solde)
            print("Action impossible, vous êtes en négatif")
        else:
            print("Votre solde est de :", self._solde)
            print("Votre avez retiré :", argent_retire, "de votre solde")

            self._solde = self._solde - argent_retire

    def versement(self, argent_verse):
        '''Méthode servant à verser de l'argent, retourne à l'utilsateur son solde et la valeur qu'il veut verser'''
        print("Votre solde est de :", self._solde)
        print("Votre avez ajouté :", argent_verse, "à votre solde")

        self._solde = self._solde + argent_verse

    def afficher_solde(self):
        '''Simple methode pour afficher le solde arrondi à 2 chiffre après la virgule'''
        return round(self._solde, 2)


class compte_courant(compte_bancaire):
    '''Classe compte courant, compte servant au quotidient pour les payements et les retrait d'argent.
    Celui-ci peut être dans le négatif mais appliquera des agios le cas échéant'''
    def __init__(self, nom_proprietaire, solde, pourcentage_agios, autorisation_decouvert):
        super().__init__( nom_proprietaire, solde)
        self.__autorisation_decouvert = -autorisation_decouvert
        self.__pourcentage_agios = pourcentage_agios

    def agios(self):
        '''Methode servant à calculer les agios sur le solde si celui-ci est négatif après l'opération'''
        if self._solde < 0:
            self._solde = self._solde * (1 + self.__pourcentage_agios / 100)


    def retrait(self, argent_retire):
        '''Méthode de retrait appliquant les agios, quand ceux-ci sont actifs
        Et qui détermine si le retrait est possible en fonction du maximum de découvert possible'''
        if self._solde > 0 and self._solde - argent_retire > self.__autorisation_decouvert:
            compte_bancaire.retrait(self, argent_retire)
            self.agios()
        else:
            if self._solde <= 0:
                print("Votre solde est de :", self._solde)
                print("Action impossible, vous êtes en négatif")
            else:
                print("Votre solde est de :", self._solde)
                print("Vous voulez retirer :", argent_retire,)
                print("Pour un nouveau solde de :", self._solde - argent_retire,)
                print("Cette opération vous fera tomber sous votre seuil de découvert autorisé, qui est de :", self.__autorisation_decouvert)
                print("Vous ne pouvez pas effectuer ce retrait")

    def versement(self, argent_verse):
        '''Méthode de versement, applique les agios si le solde est toujours négatif après opération'''
        compte_bancaire.versement(self, argent_verse)
        self.agios()




class compte_epargne(compte_bancaire):
    '''Classe compte épargne, compte classic servant à stocker de l'argent sur le long terme afin de profiter des intérêts'''
    def __init__(self, nom_proprietaire, solde, pourcentage_interet):
        super().__init__( nom_proprietaire, solde)
        self.__pourcentage_interet = pourcentage_interet

    def interet(self):
        '''Méthode servant à calculer les intérêts en fonction du solde après opération'''
        if self._solde > 0:
            self._solde = self._solde * (1 + self.__pourcentage_interet / 100)

    def retrait(self, argent_retire):
        '''Méthode de retrait, applique les intérêts sur le solde après opération'''
        compte_bancaire.retrait(self, argent_retire)
        self.interet()

    def versement(self, argent_verse):
        '''Méthode de versement, applique les intérêts sur le solde après opération'''
        compte_bancaire.versement(self, argent_verse)
        self.interet()


__author__ = "MERCIER Raphaël"
__copyright__ = "Copyright (C) 2022 R.Mercier"
__licence__ = "Public Domain"
__version__ = "1.0"
