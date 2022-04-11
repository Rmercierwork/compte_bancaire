# Exercice autour de la Programation Orientée Objet

Aujourd'hui, le thème est la Comptabilité !

## Sujet

Ecrire un programme qui implémente en POO un fonctionnement bancaire basique :  

- une classe Compte 
    - **attributs :** numeroCompte, nomProprietaire, solde  
    - **méthodes :** retrait, versement, afficherSolde  

- une classe fille CompteCourant, qui ajoute une gestion du découvert (montant maximum négatif 
possible) et des agios (pénalité de X % si le solde est inférieur à zéro) :  
    - **attributs :** autorisationDecouvert, pourcentageAgios  
    - **méthodes :** appliquerAgios  

- une classe fille CompteEpargne, qui ajoute :  
    - **attributs :** pourcentageInterets  
    - **méthodes :** appliquer Interets  

 

Le programme doit demander à l’utilisateur le compte concerné (« courant » ou « epargne ») et le montant 
de la transaction (positif pour un versement, négatif pour un retrait)  

Chaque appel de méthode doit afficher le solde avant opération, le détail de l’opération et le solde après 
opération. On suppose pour la simplicité de l’exercice que chaque modification du solde applique les agios 
ou intérêts du compte modifié. 

## Livraison
 
Réalisez un fork de ce dépôt.
Implémentez votre code
Puis réalisez une merge request afin de livrer votre code au formateur. 
Ne vous tracassez pas avec des branches git.



"""
class compte_bancaire:
    def __init__(self, numero_compte, nom_proprietaire):
        self._numero_compte = numero_compte
        self._nom_proprietaire = nom_proprietaire
        self._solde = 1


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
    def __init__(self, numero_compte, nom_proprietaire, pourcentage_agios):
        super().__init__(numero_compte, nom_proprietaire)
        self.__autorisation_decouvert = -200
        self.__pourcentage_agios = pourcentage_agios

    def agios(self):
        if self._solde < 0:
            self._solde = self._solde * (1 + self.__pourcentage_agios / 100)


    def retrait(self, argent_retire):
        if argent_retire < self._solde and self._solde - argent_retire > self.__autorisation_decouvert:
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
    def __init__(self, numero_compte, nom_proprietaire, pourcentage_interet):
        super().__init__(numero_compte, nom_proprietaire)
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

"""