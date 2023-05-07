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
        props = cls.Reformat_Dict_Quotes(props)
                        
        return super().create(*children, **props)

    @classmethod
    def Reformat_Dict_Quotes(cls, props):
        # Correct quotes to prevent compile error
        for key, value in props.items():
            if type(value) == str:
                splits = value.split(',')
                for i, split in enumerate(splits):
                    if split.startswith('"') and split.endswith('"'):
                        splits[i] = split.replace('"', "'")
                        props[key] = ','.join(splits)
        return props
      
   