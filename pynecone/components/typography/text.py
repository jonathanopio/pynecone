"""A text component."""
from __future__ import annotations

from pynecone.components.libs.chakra import ChakraComponent
from pynecone.var import Var


class Text(ChakraComponent):
    """Render a paragraph of text."""

    tag = "Text"

    # Override the tag. The default tag is `<p>`.
    as_: Var[str]
    
    @classmethod
    def create(cls, *children, **props):
        
        
                        
        return super().create(*children, **props)