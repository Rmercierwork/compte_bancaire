Il s'agit d'un exercice dans le cadre de la formation POEC-cybersécurité
avec l'EPSI Rennes.
Vous trouverez l'intitulé plus bas.

Pour lancer le programme : run le main.py

Le programme permet la création d'un utilisateur, qui pourra interagir avec son compte courant et son compte épargne.
Il pourra retirer ou verser de l'argent, son solde sera affiché après chaques opérations.

Le compte courant, les agios sont appliqués si le solde passe dans le négatif, et celui-ci dispose d'un plafond à ne pas dépasser.

Le compte épargne, les intérêts sont appliqués après chaque opération sur le nouveau solde.

Une petite batterie de tests ont été écris afin de tester les différentes méthodes de compte.py

Temps consacré au projet : 3 soirées (à update après chaque mise à jour)

TODO :
- configurer et ajouter une dabatase avec sqlite
- créer une interface graphique avec tk ou Qt



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
