import os.path
from typing import List, Tuple, Type
from pynecone.event import EVENT_ARG

import pytest

from pynecone.components.component import Component
from pynecone.components.forms.checkbox import Checkbox
from pynecone.style import Style
from pynecone.var import Var
from typing import Dict


@pytest.fixture
def checkbox1() -> Type[Checkbox]:
    """A test component.

    Returns:
        A test component.
    """
    class TestCheckbox(Checkbox):
        tag = "Checkbox"

        # Color scheme for checkbox.
        color_scheme: Var[str]

        # "sm" | "md" | "lg"
        size: Var[str]

        # If true, the checkbox will be checked.
        is_checked: Var[bool]

        # If true, the checkbox will be disabled
        is_disabled: Var[bool]

        # If true and is_disabled is passed, the checkbox will remain tabbable but not interactive
        is_focusable: Var[bool]

        # If true, the checkbox will be indeterminate. This only affects the icon shown inside checkbox and does not modify the is_checked var.
        is_indeterminate: Var[bool]

        # If true, the checkbox is marked as invalid. Changes style of unchecked state.
        is_invalid: Var[bool]

        # If true, the checkbox will be readonly
        is_read_only: Var[bool]

        # If true, the checkbox input is marked as required, and required attribute will be added
        is_required: Var[bool]

        # The name of the input field in a checkbox (Useful for form submission).
        name: Var[str]

        # The spacing between the checkbox and its label text (0.5rem)
        spacing: Var[str]

        label: Var[str]
        

        def test_create(*children,**props):
            print(children)
            print(props)
            label = props.get("label")

            if label is not None:
                children = (props["label"])
                
                return "correct handling"
            else:
                return "incorrect handling"
            
        @classmethod
        def get_controlled_triggers() -> Dict[str, Var]:
            """Get the event triggers that pass the component's value to the handler.

            Returns:
                A dict mapping the event trigger to the var that is passed to the handler.
            """
            return {
                "on_change": EVENT_ARG.target.checked,
            }

    return TestCheckbox


def test_create_checkbox(checkbox1):
    """Test that the component is created correctly.

    Args:
        component1: A test component.
    """

    c = checkbox1.test_create(label="checkbox label")
    assert c == "correct handling"

def test_checkbox_prop_handle():
    checkbox = Checkbox()
    
    assert checkbox.Check_Label_Prop({"label": "Checkbox label"}) == True

