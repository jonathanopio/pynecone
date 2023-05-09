"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from ast import List, Tuple
from pcconfig import config

import pynecone as pc
import pandas as pd
docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

class State(pc.State):
     opened: bool = False

def index():
    return pc.center(
        pc.vstack(
            pc.html("<h1>Hello World</h1>"),
            pc.html("<h2>Hello World</h2>"),
            pc.html("<h3>Hello World</h3>"),
            pc.html("<h4>Hello World</h4>"),
            pc.html("<h5>Hello World</h5>"),
            pc.html("<h6>Hello World</h6>"),
        )
    )

app = pc.App(state=State)
app.add_page(index)
app.compile()