import unittest
from searchAuthor import *
TOP = 3

class testTopThree(unittest.TestCase):
  def testAgathaChristieTopThree(self):
    result = informationRetrieval("books/Agatha_Christie_-_The_ABC_Murder.epub")
    results = []
    for i in range(TOP):
      results.append(result[i][1])
    self.assertIn("AgathaChristie", results)

  def testAndrzejSapkowskiTopThree(self):
    result = informationRetrieval("books/Andrzej_Sapkowski_-_Baptism_of_Fire.epub")
    results = []
    for i in range(TOP):
      results.append(result[i][1])
    self.assertIn("AndrzejSapkowski", results)
  
  def testBrandonSandersonTopThree(self):
    result = informationRetrieval("books/Bands_of_Mourning_The_-_Brandon_Sanderson.epub")
    results = []
    for i in range(TOP):
      results.append(result[i][1])
    self.assertIn("BrandonSarderson", results)

  def testELJamesTopThree(self):
    result = informationRetrieval("books/Grey.epub")
    results = []
    for i in range(TOP):
      results.append(result[i][1])
    self.assertIn("ELJames", results)

  def testGeorgeRRMartinTopThree(self):
    result = informationRetrieval("books/GeorgeRRMartin_-_A_Dance_With_Dragons.epub")
    results = []
    for i in range(TOP):
      results.append(result[i][1])
    self.assertIn("GeorgeRRMartin", results)

  def testJKRowlingTopThree(self):
    result = informationRetrieval("books/Harry_Potter_and_the_Deathly_Hallows_Harry_Potter_7.epub")
    results = []
    for i in range(TOP):
      results.append(result[i][1])
    self.assertIn("JKRowling", results)

  def testStephanieMeyerTopThree(self):
    result = informationRetrieval("books/Ebook_Series_-_Scifan_-_Stephenie_Meyer_-_Twilight_Saga_-_04_of_04_-_Breaking_Dawn.epub")
    results = []
    for i in range(TOP):
      results.append(result[i][1])
    self.assertIn("StephanieMeyer", results)

  def testSthephenKingTopThree(self):
    result = informationRetrieval("books/Stephen_King_-_Dark_Tower_08_-_The_Wind_Through_The_Keyhole_1.epub")
    results = []
    for i in range(TOP):
      results.append(result[i][1])
    self.assertIn("StephenKing", results)

  def testScottFitzGeraldTopThree(self):
    result = informationRetrieval("books/The_Great_Gatsby_-_Fitzgerald_F_Scott.epub")
    results = []
    for i in range(TOP):
      results.append(result[i][1])
    self.assertIn("ScottFitzgerald", results)
    
  def testArthurConanDoyle(self):
    result = informationRetrieval("books/ArthurConanDoyle-TheSignOfTheFour.epub")
    results = []
    for i in range(TOP):
      results.append(result[i][1])
    self.assertIn("ArthurConanDoyle", results)

  def testBramStoker(self):
    result = informationRetrieval("books/BramStoker-TheLairOfTheWhiteWorm.epub")
    results = []
    for i in range(TOP):
      results.append(result[i][1])
    self.assertIn("BramStoker", results)

  def testJaneAusten(self):
    result = informationRetrieval("books/JaneAusten-TheLettersOfJaneAusten.epub")
    results = []
    for i in range(TOP):
      results.append(result[i][1])
    self.assertIn("JaneAusten", results)

  def testJulesVerne(self):
    result = informationRetrieval("books/JulesVerne-TwentyThousandLeaguesUnderTheSea.epub")
    results = []
    for i in range(TOP):
      results.append(result[i][1])
    self.assertIn("JulesVerne", results)

  def testPatrickRothfuss(self):
    result = informationRetrieval("books/RothfussPatrick_-_The_King_Killer_Chronicle_1_-_The_Name_of_the_Wind.epub")
    results = []
    for i in range(TOP):
      results.append(result[i][1])
    self.assertIn("PatrickRothfuss", results)

if __name__ == '__main__':
  unittest.main()