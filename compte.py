class compte_bancaire:
    def __init__(self, nom_proprietaire, solde):
        self._numero_compte = 123
        self._nom_proprietaire = nom_proprietaire
        self._solde = solde


    def retrait(self, argent_retire):
        if self._solde <= 0:
            print("Votre solde est de :", self._solde)
            print("Action impossible, vous êtes en négatif")
        else:
            print("Votre solde est de :", self._solde)
            print("Votre allez retirer :", argent_retire, "de votre solde")

            self._solde = self._solde - argent_retire

    def versement(self, argent_verse):
        print("Votre solde est de :", self._solde)
        print("Votre allez ajouter :", argent_verse, "à votre solde")

        self._solde = self._solde + argent_verse

    def afficher_solde(self):
        return self._solde


class compte_courant(compte_bancaire):
    def __init__(self, nom_proprietaire, solde, pourcentage_agios):
        super().__init__( nom_proprietaire, solde)
        self.__autorisation_decouvert = -200
        self.__pourcentage_agios = pourcentage_agios

    def agios(self):
        if self._solde < 0:
            self._solde = self._solde * (1 + self.__pourcentage_agios / 100)


    def retrait(self, argent_retire):
        if self._solde > 0 and self._solde - argent_retire > self.__autorisation_decouvert:
            compte_bancaire.retrait(self, argent_retire)
            self.agios()
            print("Votre nouveau solde est de :", self._solde)
        else:
            if self._solde <= 0:
                print("Votre solde est de :", self._solde)
                print("Vous ne pouvez pas effectuer ce retrait")
            else:
                print("Votre solde est de :", self._solde)
                print("Vous voulez retirer :", argent_retire,)
                print("Pour un nouveau solde de :", self._solde - argent_retire,)
                print("Cette opération vous fera tomber sous votre seuil de découvert autorisé, qui est de :", self.__autorisation_decouvert)
                print("Vous ne pouvez pas effectuer ce retrait")

    def versement(self, argent_verse):
        compte_bancaire.versement(self, argent_verse)
        self.agios()
        print("Votre nouveau solde est de :", self._solde)




class compte_epargne(compte_bancaire):
    def __init__(self, nom_proprietaire, solde, pourcentage_interet):
        super().__init__( nom_proprietaire, solde)
        self.__pourcentage_interet = pourcentage_interet

    def interet(self):
        if self._solde > 0:
            self._solde = self._solde * (1 + self.__pourcentage_interet / 100)

    def retrait(self, argent_retire):
        compte_bancaire.retrait(self, argent_retire)
        self.interet()
        print("Votre nouveau solde est de : ", self._solde)

    def versement(self, argent_verse):
        compte_bancaire.versement(self, argent_verse)
        self.interet()
        print("Votre nouveau solde est de : ", self._solde)

