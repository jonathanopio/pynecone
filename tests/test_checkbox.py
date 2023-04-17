import os.path
from typing import List, Tuple, Type

import pytest

from pynecone.components.component import Component
from pynecone.components import Checkbox
from pynecone.style import Style


@pytest.fixture
def checkbox1() -> Type[Component]:
    """A test component.

    Returns:
        A test component.
    """
    return Checkbox


def test_create_checkbox(checkbox1):
    """Test that the component is created correctly.

    Args:
        component1: A test component.
    """
    style = {
        checkbox1: Style({"label":"checkbox label"})
    }
    c = checkbox1().add_style(style)
    assert c.style['label'] == "checkbox label"
