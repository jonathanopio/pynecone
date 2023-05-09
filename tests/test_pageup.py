"""A html component."""

from pynecone import Button, Link


def test_button():
    button = Button().create("↑", href="#top", position="fixed", bottom="8px", right="10px")
    assert button.href == "#top"
    assert button.position == "fixed"
    assert button.bottom == "8px"
    assert button.right == "10px"
