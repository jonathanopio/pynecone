import os.path
from typing import List, Tuple, Type
from pynecone.event import EVENT_ARG

import pytest

from pynecone.components.component import Component
from pynecone.components.forms.checkbox import Checkbox
from pynecone.style import Style
from pynecone.var import Var
from typing import Dict


def test_label_exists():
        checkbox = Checkbox()
    
        props = {"label": "Test Label"}
        assert checkbox.Check_Label_Prop(props) == True
        
def test_label_does_not_exist():
    checkbox = Checkbox()
    
    props = {"not_label": "Test Value"}
    assert checkbox.Check_Label_Prop(props) == False
    
def test_empty_props():
    checkbox = Checkbox()
    
    props = {}
    assert checkbox.Check_Label_Prop(props) == False