import unittest
from compte import *

class test_compte(unittest.TestCase):
    def setUp(self) -> None:
        '''Fonction servant à prédéfinir nos comptes tests afin de ne pas les réécrire pour chaque test'''
        self.compte_test = compte_bancaire("Toto", 1000)
        self.compte_epargne_test = compte_epargne("Toto", 1500, 10)
        self.compte_courant_test = compte_courant("Toto", 3000, 20, 200)

    def testStartingBalance(self):
        '''Test sur le compte bancaire affiche le nom'''
        self.assertEqual(self.compte_test._nom_proprietaire, "Toto")

    def test_bancaire_solde(self):
        '''Test sur le compte bancaire affiche le solde'''
        self.assertEqual(self.compte_test._solde, 1000)

    def test_bancaire_versement(self):
        '''Test sur le compte bancaire le versement d'argent'''
        self.compte_test.versement(100)
        self.assertEqual(self.compte_test._solde, 1100)

    def test_bancaire_retrait(self):
        '''Test sur le compte bancaire le retrait d'argent'''
        self.compte_test.retrait(500)
        self.assertEqual(self.compte_test._solde, 500)

    def test_epargne_solde(self):
        '''Test sur le compte épargne affiche le solde'''
        self.assertEqual(self.compte_epargne_test._solde, 1500)

    def test_epargne_versement(self):
        '''Test sur le compte épargne si les intérêts sont bien pris en compte'''
        self.compte_epargne_test.versement(500)
        self.assertEqual(self.compte_epargne_test._solde, 2200)

    def test_courant_solde(self):
        '''Test sur le compte courant affiche le solde'''
        self.assertEqual(self.compte_courant_test._solde, 3000)

    def test_courant_retrait_agios(self):
        '''Test sur le compte courant si les agios sont bien pris en compte'''
        self.compte_courant_test.retrait(3100)
        self.assertEqual(self.compte_courant_test._solde, -120)

    def test_courant_retrait_depassement(self):
        '''Test sur le compte courant si l'opération échoue en cas de dépassement du solde de retrait autorisé'''
        self.compte_courant_test.retrait(3500)
        self.assertEqual(self.compte_courant_test._solde, 3000)