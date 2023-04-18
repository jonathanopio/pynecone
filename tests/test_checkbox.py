import os.path
from typing import List, Tuple, Type
from pynecone.event import EVENT_ARG

import pytest

from pynecone.components.component import Component
from pynecone.components.forms.checkbox import Checkbox
from pynecone.style import Style
from pynecone.var import Var
from typing import Dict


def test_checkbox_prop_handle():
    checkbox = Checkbox()
    
    assert checkbox.Check_Label_Prop({"label": "Checkbox label"}) == True
    assert checkbox.Check_Label_Prop({"not_a_label": "Checkbox label"}) == False
