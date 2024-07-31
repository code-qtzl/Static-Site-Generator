class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        LeafNode().to_html()
        raise NotImplemented()

    def props_to_html(self):
        return f' {self.props}'

    def __repr__(self):
        print(f'{self.tag} {self.value} {self.children} {self.props}')

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == '':
            raise ValueError
        return f'{self.tag}, {self.value}, {self.props}'

