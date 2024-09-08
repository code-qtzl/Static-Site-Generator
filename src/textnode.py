from enum import Enum

class TextType(Enum):
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url 

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
    
# Define the LeafNode class to represent HTML nodes
class LeafNode:
    def __init__(self, tag, text='', **props):
        self.tag = tag
        self.text = text
        self.props = props

    def __repr__(self):
        if self.tag:
            props_str = ' '.join(f'{key}="{value}"' for key, value in self.props.items())
            return f'<{self.tag} {props_str}>{self.text}</{self.tag}>'
        else:
            return self.text

# Function to convert TextNode to corresponding HTML node
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.text_type_text:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.text_type_bold:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.text_type_italic:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.text_type_code:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text_type}")

def main():
    # Create instances of TextNode
    node1 = TextNode('Hello World', TextType.text_type_bold)
    node2 = TextNode('Visit OpenAI', TextType.text_type_link, 'https://www.boot.dev')
    node3 = TextNode('Image Example', TextType.text_type_image, 'https://books.toscrape.com/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg')

    # print(text_node_to_html_node(node1)) 
    # print(text_node_to_html_node(node2)) 
    # print(text_node_to_html_node(node3)) 
    
main()