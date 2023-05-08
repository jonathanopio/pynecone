"""A link component."""
import urllib.request as ulib

import pynecone as pc
from pynecone.components.component import Component
from pynecone.components.libs.chakra import ChakraComponent
from pynecone.components.navigation.nextlink import NextLink
from pynecone.var import Var
from pynecone.components.layout import Html


class Link(ChakraComponent):
    """Link to another page."""

    tag = "Link"

    # The rel.
    rel: Var[str]

    # The page to link to.
    href: Var[str]

    # The text to display.
    text: Var[str]

    # If true, the link will open in new tab.
    is_external: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create a NextJS link component, wrapping a Chakra link component.

        Args:
            *children: The children to pass to the component.
            **props: The attributes to pass to the component.

        Returns:
            The component.
        """
        address = props.get("href")
        if not cls.get_url_status(address):
            return Html.create("<h1> 404! Link is broken! </h1>")
        else:
            kwargs = {"href": props.pop("href") if "href" in props else "#"}
            return NextLink.create(super().create(*children, **props), **kwargs)

    @classmethod
    def get_url_status(cls, url):
        try:
            r = ulib.urlopen(url)
            print(url + "\tStatus: " + str(r.getcode()))
            return True
        except BaseException as e:
            return False
