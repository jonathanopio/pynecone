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
        
        # Correct quotes to prevent compile error
        for key, value in props.items():
            print(type(value))
            if type(value) == str:
                print("this happened")
                splits = value.split(',')
                for i, split in enumerate(splits):
                    if split.startswith('"') and split.endswith('"'):
                        splits[i] = split.replace('"', "'")
                        props[key] = ','.join(splits)
                        
        return super().create(*children, **props)