import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "paragraph value", [HTMLNode('span', 'child')], {"class": "text"})
        node2 = HTMLNode("p", "paragraph value", [HTMLNode('span', 'child')], {"class": "text"})
        self.assertEqual(node, node2)
    
    def test_link_eq(self):
        node = HTMLNode("a", "link", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("a", "link", None, {"href": "https://www.google.com"})
        self.assertEqual(node, node2)

    def test_heading_eq(self):
        node = HTMLNode("h1", "heading", [HTMLNode('span', 'child')], {"class": "text"})
        node2 = HTMLNode("h1", "heading", [HTMLNode('span', 'child')], {"class": "text"})
        self.assertEqual(node, node2)

    def test_leaf_p_eq(self):
        node = LeafNode("p", "This is a paragraph")
        node2 = LeafNode("p", "This is a paragraph")
        self.assertEqual(node, node2)

    def test_leaf_a_eq(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node, node2)


    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                "Normal text",
                LeafNode("i", "italic text"),
                "Normal text",
            ],
        )
        result = node.to_html()
        print(result)  # Print the actual output for inspection
        self.assertEqual(
            result,
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

if __name__ == "__main__":
    unittest.main()
