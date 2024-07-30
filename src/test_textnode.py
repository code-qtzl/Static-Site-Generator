import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def __init__(self, text, text_type=None, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def test_eq(self):
        node = TextNode("This is a text node", "bold", url="https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", url="https://www.boot.dev")
        self.assertEqual(node, node2)
    
    def test_url_none(self):
        node = TextNode("This is a text node", "bold", url=None)
        node2 = TextNode("This is a text node", "bold", url=None)
        self.assertEqual(node, node2)

    def test_text_prop_italic(self):
        node = TextNode("This is a text node", "bold", url="https://www.boot.dev")
        node2 = TextNode("This is a text node", "italic", url="https://www.boot.dev")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()