import unittest
import myclass1

class test1(unittest.TestCase):
    def setUp(self):
        self.myclass1 = myclass1.myclass1()

        pass
    def tearDown(self):
        pass



    def test_sum(self):
        self.assertEqual(self.myclass1.sum(1,2),3,'test sum fail')
    def test_cha(self):
        self.assertEqual(self.myclass1.cha(2,1),1)



if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(test1)
    unittest.TextTestRunner(verbosity=2).run(suite)