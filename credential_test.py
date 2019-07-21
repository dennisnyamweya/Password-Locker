import unittest
from credential import Credential

class TestCredential(unittest.TestCase):

    def setUp(self):
        # Create credential object
        self.new_credential = Credential("Facebook","dela","dela13")

    def tearDown(self):
        Credential.credential_list = []
        
    # def test_init(self):
        
    #     self.assertEqual(self.new_credential.account, "Facebook")
    #     self.assertEqual(self.new_credential.password, "dela" )
    #     self.assertEqual(self.new_credential.account_password, "dela13")

if __name__ == '__main__':
    unittest.main()