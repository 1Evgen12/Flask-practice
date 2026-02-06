import unittest
from decrypt import decrypt

class TestDecrypt(unittest.TestCase):
    def test_decrypt(self):

        self.assertTrue(decrypt("абра-кадабра.") == "абра-кадабра")
        self.assertTrue(decrypt("абраа..-кадабра") == "абра-кадабра")
        self.assertTrue(decrypt("абраа..-.кадабра") == "абра-кадабра")
        self.assertTrue(decrypt("абра--..кадабра") == "абра-кадабра")
        self.assertTrue(decrypt("абрау...-кадабра") == "абра-кадабра")
        self.assertTrue(decrypt("абра........") == "")
        self.assertTrue(decrypt("абр......а.") == "а")
        self.assertTrue(decrypt("1..2.3") == "23")
        self.assertTrue(decrypt(".") == "")
        self.assertTrue(decrypt("1.......................") == ""
)
