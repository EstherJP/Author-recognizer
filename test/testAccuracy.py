import unittest
from searchAuthor import *
import sys
# sys.path.insert(0, '../scripts/searchAuthor.py')
import searchAuthor

class testAccuracy(unittest.TestCase):
  def testAgathaChristie(self):
    result = informationRetrieval("books/Agatha_Christie_-_The_ABC_Murder.epub")[0][1]
    self.assertEqual(result, "AgathaChristie")

  def testAndrzejSapkowski(self):
    result = informationRetrieval("books/Andrzej_Sapkowski_-_Baptism_of_Fire.epub")[0][1]
    self.assertEqual(result, "AndrzejSapkowski")

  def testBrandonSanderson(self):
    result = informationRetrieval("books/Bands_of_Mourning_The_-_Brandon_Sanderson.epub")[0][1]
    self.assertEqual(result, "BrandonSarderson")

  def testELJames(self):
    result = informationRetrieval("books/Grey.epub")[0][1]
    self.assertEqual(result, "ELJames")
  
  def testGeorgeRRMartin(self):
    result = informationRetrieval("books/GeorgeRRMartin_-_A_Dance_With_Dragons.epub")[0][1]
    self.assertEqual(result, "GeorgeRRMartin")

  def testJKRowling(self):
    result = informationRetrieval("books/Harry_Potter_and_the_Deathly_Hallows_Harry_Potter_7.epub")[0][1]
    self.assertEqual(result, "JKRowling")

  def testStephanieMeyer(self):
    result = informationRetrieval("books/Ebook_Series_-_Scifan_-_Stephenie_Meyer_-_Twilight_Saga_-_04_of_04_-_Breaking_Dawn.epub")[0][1]
    self.assertEqual(result, "StephanieMeyer")

  def testSthephenKing(self):
    result = informationRetrieval("books/Stephen_King_-_Dark_Tower_08_-_The_Wind_Through_The_Keyhole_1.epub")[0][1]
    self.assertEqual(result, "StephenKing")

  def testScottFitzGerald(self):
    result = informationRetrieval("books/The_Great_Gatsby_-_Fitzgerald_F_Scott.epub")[0][1]
    self.assertEqual(result, "ScottFitzgerald")

  def testArthurConanDoyle(self):
    result = informationRetrieval("books/ArthurConanDoyle-TheSignOfTheFour.epub")[0][1]
    self.assertEqual(result, "ArthurConanDoyle")

  def testBramStoker(self):
    result = informationRetrieval("books/BramStoker-TheLairOfTheWhiteWorm.epub")[0][1]
    self.assertEqual(result, "BramStoker")

  def testJaneAusten(self):
    result = informationRetrieval("books/JaneAusten-TheLettersOfJaneAusten.epub")[0][1]
    self.assertEqual(result, "JaneAusten")

  def testJulesVerne(self):
    result = informationRetrieval("books/JulesVerne-TwentyThousandLeaguesUnderTheSea.epub")[0][1]
    self.assertEqual(result, "JulesVerne")

  def testPatrickRothfuss(self):
    result = informationRetrieval("books/RothfussPatrick_-_The_King_Killer_Chronicle_1_-_The_Name_of_the_Wind.epub")[0][1]
    self.assertEqual(result, "PatrickRothfuss")

if __name__ == '__main__':
  unittest.main() 