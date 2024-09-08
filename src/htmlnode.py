class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError('Method not implemented')

    def props_to_html(self):
        if not self.props:
            return ""
        return ' '.join(f'{key}="{value}"' for key, value in self.props.items())

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)

    def __repr__(self):
        return f'{self.tag} {self.value} {self.children} {self.props}'
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError('Invalid HTML: no value')
        props_str = self.props_to_html()
        opening_tag = f'<{self.tag} {props_str}>' if props_str else f'<{self.tag}>'
        return f'{opening_tag}{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError('No Tag')
        if not self.children:
            raise ValueError('No Children')

        props_str = self.props_to_html()
        opening_tag = f'<{self.tag} {props_str}>' if props_str else f'<{self.tag}>'
        
        # Convert all child nodes to HTML recursively
        children_html = ''.join(
            child.to_html() if isinstance(child, HTMLNode) else str(child)
            for child in self.children
        )
        
        closing_tag = f'</{self.tag}>'
        return f'{opening_tag}{children_html}{closing_tag}'
