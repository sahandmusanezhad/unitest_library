import unittest
import cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = "python"
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_two_words(self):
        text = "jacky jun"
        result = cap.cap_text(text)
        self.assertEqual(result, 'Jacky Jun')

if __name__ == '__main__':
    unittest.main()