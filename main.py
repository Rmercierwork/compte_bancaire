from compte import*

def identification():
    numero_compte = 0
    nom_proprietaire = compte_bancaire(input("Saisissez votre nom : "))

    choix_compte(nom_proprietaire)

def choix_compte(nom_proprietaire):
    choix = True
    while choix:
        print("Sur quel compte voulez-vous effectuer une opération ?")
        print("1 pour : Compte courant")
        print("2 pour : Compte épargne")
        compte_choisi = int(input())
        if compte_choisi == 1:
            compte_choisi = compte_courant
            print("Le solde de votre compte courant est de :", compte_choisi.afficher_solde(nom_proprietaire) )
            agios = compte_courant(nom_proprietaire, pourcentage_agios=int(input("De quel pourcentage sont vos agios : ")))
            operation(nom_proprietaire, compte_choisi, agios)
            choix = False
        elif compte_choisi == 2:
            compte_choisi = compte_epargne
            print("Le solde de votre compte épargne est de :", compte_choisi.afficher_solde(nom_proprietaire) )
            interet = compte_epargne(nom_proprietaire, pourcentage_interet=int(input("De quel pourcentage sont vos interet : ")))
            operation(nom_proprietaire, compte_choisi, interet)
            choix = False

        else:
            print("Vous n'avez pas choisi entre votre compte courant, ou votre compte épargne.")
            print("Merci de bien vouloir choisir parmis l'un des deux")

def operation(nom_proprietaire, compte_choisi, agios):
    choix = True
    while choix:
        print("Quel opération voulez-vous effectuer ?")
        print("1 pour : versement")
        print("2 pour : retrait")
        operation_choisi = int(input())
        if operation_choisi == 1:
            operation_choisi = compte_choisi.versement(nom_proprietaire)
            print("Le solde de votre compte courant est de :", compte_choisi.afficher_solde(nom_proprietaire))
            choix = False
        elif operation_choisi == 2:
            operation_choisi = compte_choisi.retrait(compte_choisi(nom_proprietaire, agios), argent_retire=0)
            choix = False

        else:
            print("Vous devez soit faire un versement, soit un retrait")
            print("Désolé, mais aucune autre opération n'est possible")

    montant(nom_proprietaire, compte_choisi, operation_choisi, agios)

def montant(nom_proprietaire, compte_choisi, operation_choisi, agios):
    if operation_choisi == compte_choisi.retrait(compte_choisi(nom_proprietaire, agios), argent_retire=0):
        argent = int(input("De combien voulez-vous retirer : "))


identification()