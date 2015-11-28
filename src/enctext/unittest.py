import unittest
import enctext


class Test(unittest.TestCase):
    raw_password = 'secret_password'
    raw_text = b'This text will be encrypted.'

    def test_encrypto_and_decrypt(self):
        encrypted_text = enctext.encrypt(self.raw_password, self.raw_text)
        decrypted_text = enctext.decrypt(self.raw_password, encrypted_text)
        self.assertEqual(self.raw_text, decrypted_text)

    @unittest.expectedFailure
    def test_bad_password(self):
        encrypted_text = enctext.encrypt(self.raw_password, self.raw_text)
        decrypted_text = enctext.decrypt('wrong_password', encrypted_text)
        self.assertEqual(self.raw_text, decrypted_text)


if __name__ == '__main__':
    unittest.main()
