# 1. import the files
import unittest
from AppiumFrameWork.tests.ContactUsFormTest import ContactFormTest
from AppiumFrameWork.tests.LoginPageTest import LoginTest

# 2. Create the object of the class using unitTest
cf = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)
gt = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

# 3. Create Test Suite.
regressiontest = unittest.TestSuite([cf,gt])

# 4. Call the Test Runner method.
unittest.TextTestRunner(verbosity=1).run(regressiontest)