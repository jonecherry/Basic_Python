import unittest
import myclass1
import test1
import tst






if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(test1.test1)
    suite1 = unittest.TestLoader().loadTestsFromTestCase(tst.TestStringMethods)
    allsuite = unittest.TestSuite([suite,suite1])
    unittest.TextTestRunner(verbosity=2).run(allsuite)