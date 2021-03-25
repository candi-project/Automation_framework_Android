# 1. import the files
import unittest
from AppiumFrameWork.tests.test_scenario1 import Scenario1
from AppiumFrameWork.tests.test_scenario2 import Scenario2

# 2. Create the object of the class using unitTest
cf = unittest.TestLoader().loadTestsFromTestCase(Scenario1)
gt = unittest.TestLoader().loadTestsFromTestCase(Scenario2)

# 3. Create Test Suite.
regressiontest = unittest.TestSuite([cf, gt])

# 4. Call the Test Runner method.
unittest.TextTestRunner(verbosity=1).run(regressiontest)
