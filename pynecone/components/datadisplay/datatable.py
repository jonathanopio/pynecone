"""Table components."""

from typing import Any, List, Optional
import pynecone as pc
import pandas as pd
from pynecone.components.component import Component
from pynecone.components.tags import Tag
from pynecone.utils import format, imports, types
from pynecone.var import BaseVar, Var
from pynecone.components.navigation.nextlink import NextLink



class Gridjs(Component):
    """A component that wraps a nivo bar component."""

    library = "gridjs-react"


class DataTable(Gridjs):
    """A data table component."""

    tag = "Grid"

    # The data to display. Either a list of dictionaries or a pandas dataframe.
    data: Any

    # The columns to display.
    columns: Var[List]

    # Enable a search bar.
    search: Var[bool]

    # Enable sorting on columns.
    sort: Var[bool]

    # Enable resizable columns.
    resizable: Var[bool]

    # Enable pagination.
    pagination: Var[bool]

    @classmethod
    def get_alias(cls) -> Optional[str]:
        """Get the alias for the component.

        Returns:
            The alias.
        """
        return "DataTableGrid"

    @classmethod
    def create(cls, *children, **props):
        """Create a datatable component.

        Args:
            *children: The children of the component.
            **props: The props to pass to the component.

        Returns:
            The datatable component.

        Raises:
            ValueError: If a pandas dataframe is passed in and columns are also provided.
        """
        data = props.get("data")

        # If data is a pandas dataframe and columns are provided throw an error.
        if (
            types.is_dataframe(type(data))
            or (isinstance(data, Var) and types.is_dataframe(data.type_))
        ) and props.get("columns"):
            raise ValueError(
                "Cannot pass in both a pandas dataframe and columns to the data_table component."
            )

        # If data is a list and columns are not provided, throw an error
        if (
            (isinstance(data, Var) and issubclass(data.type_, List))
            or issubclass(type(data), List)
        ) and not props.get("columns"):
            raise ValueError(
                "column field should be specified when the data field is a list type"
            )
        
        print("********************************************************************************************props")
        print(props)
        props['data'] = cls.replace_links(props['data'])
        print(props)
        # Create the component.
        return super().create(
            *children,
            **props,
        )
    
    @classmethod
    def replace_links(cls, data):
        if isinstance(data, pd.DataFrame):
            for index, row in data.iterrows():
                for column in data.columns:
                    cell = row[column]
                    if isinstance(cell, str) and cls.is_website(cell):
                        data.at[index, column] = pc.link(cell, href=cell)
        elif isinstance(data, list):
            for index, row in enumerate(data):
                for column_index, cell in enumerate(row):
                    if isinstance(cell, str) and cls.is_website(cell):
                        row[column_index] = pc.link(cell, href=cell)
        return data

    def _get_imports(self) -> imports.ImportDict:
        return imports.merge_imports(
            super()._get_imports(), {"": {"gridjs/dist/theme/mermaid.css"}}
        )
        
    @classmethod
    def is_website(cls, string):
        if "." in string:
            if " " not in string:
                if not string.startswith(".") and not string.endswith("."):
                    if string.count(".") == 1:
                        return True
        return False


    def _render(self) -> Tag:

        if isinstance(self.data, Var):
            self.columns = BaseVar(
                name=f"{self.data.name}.columns"
                if types.is_dataframe(self.data.type_)
                else f"{self.columns.name}",
                type_=List[Any],
                state=self.data.state,
            )
            print(self.columns)
            self.data = BaseVar(
                name=f"{self.data.name}.data"
                if types.is_dataframe(self.data.type_)
                else f"{self.data.name}",
                type_=List[List[Any]],
                state=self.data.state,
            )

        # If given a pandas df break up the data and columns
        if types.is_dataframe(type(self.data)):
            self.columns = Var.create(list(self.data.columns.values.tolist()))  # type: ignore
            self.data = Var.create(format.format_dataframe_values(self.data))  # type: ignore

        # Render the table.
        return super()._render()
