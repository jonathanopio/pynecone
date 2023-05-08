"""A html component."""

from typing import Dict

from pynecone.components.layout.box import Box
from pynecone.components.typography.heading import Heading
from pynecone.var import Var

from pynecone.components.typography.heading import Heading
from pynecone.var import Var


class Html(Box):
    """Render the html.

    Returns:
        The code to render the  html component.
    """

    # The HTML to render.
    dangerouslySetInnerHTML: Var[Dict]

    @classmethod
    def create(cls, *children, **props):
        """Create a html component.

        Args:
            *children: The children of the component.
            **props: The props to pass to the component.

        Returns:
            The html component.

        Raises:
            ValueError: If children are not provided or more than one child is provided.
        """
        # check for heading

        # If children are not provided, throw an error.
        if len(children) != 1:
            raise ValueError("Must provide children to the html component.")
        else:
            props["dangerouslySetInnerHTML"] = {"__html": children[0]}

        

        
        string = children[0]
        text, format = cls.Format_Headings(string)
        if (format != ''):
            return Heading().create(text, size=format)
        else:
            # Create the component.
            return super().create(**props)

    @classmethod
    def Format_Headings(cls, string):
        heading = 0
        text = ""
        format = ''

        heading = 0
        string = children[0]
        text = ""

        for i in range(len(string)-2):
            if (string[i]=='<' and string[i+1]=='h'):
                if(string[i+2]).isdigit() and (int(string[i+2])<=6 and int(string[i+2])>0):
                    heading = int(string[i+2])
                    break
        if heading != 0:
            for i in range(len(string)):
                if string[i] == '>':
                    text = ""
                else: text += string[i]
                if string[i+1]=="<" and string[i+2]=='/':
                    break
            format = ""
            if heading == 1:
                format = '3xl'
            elif heading == 2:
                format = '2xl'
            elif heading == 3:
                format = 'xl'
            elif heading == 4:
                format = 'lg'
            elif heading == 5:
                format = 'md'
            elif heading == 6:
                format = 'sm'

        return text, format

            return Heading().create(text, size=format)
        else:
            # Create the component.
            return super().create(**props)
