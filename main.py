from compte import*

def bienvenue():
    '''Ui de lancement du programme, donnant un message de bienvenue'''
    print("Bienvenue dans notre banque fictive, vous pourrez stocker votre argent virtuel ici en tout sécurité !")
    print("Vous allez devoir répondre à quelques questions afin d'assurer le bon fonctionnement de cette expérience")
    print("Merci de remplir les champs demander dans le respect de notre programme")
    utilisateur()

def utilisateur():
    '''Ui de création de l'utilisateur'''

    nom_proprietaire = input("Saisissez votre nom ? : ")
    while True:
        try:
            solde_compte_courant = float(input("De combien d'argent disposé vous sur votre compte courant ? : "))
        except ValueError:
            print("Merci de rentrer nombre")
            print("Vous trouvez ça drôle d'essayer de me casser?!?")
            continue
        else:
            break
    while True:
        try:
            solde_compte_epargne = float(input("De combine d'argent disposé vous sur votre compte épargne ? : "))
        except ValueError:
            print("Merci de rentrer nombre")
            print("Vous trouvez ça drôle d'essayer de me casser?!?")
            continue
        else:
            break
    while True:
        try:
            pourcentage_agios = float(input("De combien sont vos agios ? : "))
            if pourcentage_agios <= 0:
                print("Votre taux d'agios ne peut pas nul ou négatif, merci de saisir une valeure correcte")
                continue
        except ValueError:
            print("Merci de rentrer nombre")
            print("Vous trouvez ça drôle d'essayer de me casser?!?")
            continue
        else:
            break
    while True:
        try:
            autorisation_depassement = int(input("Quel est votre limite de dépassement ? : "))
        except ValueError:
            print("Merci de rentrer nombre")
            print("Vous trouvez ça drôle d'essayer de me casser?!?")
            continue
        else:
            break
    while True:
        try:
            pourcentage_interets = float(input("De combien sont vos intérêts ? : "))
            if pourcentage_interets >= 20:
                print("Votre taux d'intérêt est trop élevé, merci de saisir une valeure moins élevée")
                print("On a beau être une banque fictive, nous voulons quand même avoir des résultats dans la limite du réaliste")
                continue
        except ValueError:
            print("Merci de rentrer nombre")
            print("Vous trouvez ça drôle d'essayer de me casser?!?")
            continue
        else:
            break

    utilisateur_compte_courant = compte_courant(nom_proprietaire, solde_compte_courant, pourcentage_agios, autorisation_depassement)
    utilisateur_compte_epargne = compte_epargne(nom_proprietaire, solde_compte_epargne, pourcentage_interets)

    compte(utilisateur_compte_courant, utilisateur_compte_epargne)

def compte(utilisateur_compte_courant, utilisateur_compte_epargne):
    continuer_operation = True
    while continuer_operation:
        print("Sur quel compte voulez-vous effectuer une opération ?")
        print("1 pour : Compte courant")
        print("2 pour : Compte épargne")
        print("3 pour : Quitter")
        compte_choisi = int(input())
        match compte_choisi:
            case 1:
                operation_compte_courant(utilisateur_compte_courant, utilisateur_compte_epargne)

            case 2:
                operation_compte_epargne(utilisateur_compte_courant, utilisateur_compte_epargne)

            case 3:
                break

            case _:
                print("Vous n'avez pas choisi entre votre compte courant, ou votre compte épargne.")
                print("Merci de bien vouloir choisir parmis l'un des deux")

def operation_compte_courant(utilisateur_compte_courant, utilisateur_compte_epargne):
    choix = True
    while choix:
        print("Le solde de votre compte courant est de :", compte_courant.afficher_solde(utilisateur_compte_courant))
        print("Quel opération voulez-vous effectuer ?")
        print("1 pour : Versement")
        print("2 pour : Retrait")
        print("3 pour : Retour")
        print("4 pour : Quitter")
        operation_choisi = int(input())
        match operation_choisi:
            case 1:
                try:
                    montant_verse = float(input("Combien d'argent voulez-vous ajouter sur votre compte courant : "))
                    compte_courant.versement(utilisateur_compte_courant, montant_verse)
                except ValueError:
                    print("Merci de rentrer nombre")
                    print("Vous trouvez ça drôle d'essayer de me casser?!?")
                    continue
                continue

            case 2:
                try:
                    montant_retire = float(input("Combien d'argent voulez-vous retirer sur votre compte courant : "))
                    compte_courant.retrait(utilisateur_compte_courant, montant_retire)
                except ValueError:
                    print("Merci de rentrer nombre")
                    print("Vous trouvez ça drôle d'essayer de me casser?!?")
                    continue
                continue

            case 3:
                compte(utilisateur_compte_courant, utilisateur_compte_epargne)

            case 4:
                choix = False

            case _:
                print("Vous pouvez soit faire un versement, soit un retrait ou retourner au choix du compte")
                print("Désolé, mais aucune autre opération n'est possible")

def operation_compte_epargne(utilisateur_compte_courant, utilisateur_compte_epargne):
    choix = True
    while choix:
        print("Le solde de votre compte épargne est de :", compte_epargne.afficher_solde(utilisateur_compte_epargne))
        print("Quel opération voulez-vous effectuer ?")
        print("1 pour : Versement")
        print("2 pour : Retrait")
        print("3 pour : Retour")
        print("4 pour : Quitter")
        operation_choisi = int(input())
        match operation_choisi:
            case 1:
                try:
                    montant_verse = float(input("Combien d'argent voulez-vous ajouter sur votre compte épargne : "))
                    compte_epargne.versement(utilisateur_compte_epargne, montant_verse)
                except ValueError:
                    print("Merci de rentrer nombre")
                    print("Vous trouvez ça drôle d'essayer de me casser?!?")
                    continue
                continue

            case 2:
                try:
                    montant_retire = float(input("Combien d'argent voulez-vous retirer sur votre compte épargne : "))
                    compte_epargne.retrait(utilisateur_compte_epargne, montant_retire)
                except ValueError:
                    print("Merci de rentrer nombre")
                    print("Vous trouvez ça drôle d'essayer de me casser?!?")
                    continue
                continue

            case 3:
                compte(utilisateur_compte_courant, utilisateur_compte_epargne)

            case 4:
                choix = False

            case _:
                print("Vous pouvez soit faire un versement, soit un retrait ou retourner au choix du compte")
                print("Désolé, mais aucune autre opération n'est possible")


if __name__ == "__main__":
    bienvenue()