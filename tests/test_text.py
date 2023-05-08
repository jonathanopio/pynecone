

from pynecone import Text


def test_no_quotes():
    text = Text.create()
    props = {'a': 1, 'b': 2, 'c': True, 'd': None}
    assert text.Reformat_Dict_Quotes(props) == props

   
def test_should_format():
    text = Text.create()
    props = {'a': 'foo', 'b': 'bar,"baz",qux'}
    expected = {'a': 'foo', 'b': "bar,'baz',qux"}
    assert text.Reformat_Dict_Quotes(props) == expected


def test_should_not_format():
    text = Text.create()
    props = {'a': 'foo,"bar",baz', 'b': '"hello",world'}
    expected = {'a': "foo,'bar',baz", 'b': "'hello',world"}
    assert text.Reformat_Dict_Quotes(props) == expected

def test_empty_string():
    text = Text.create()
    props = {'a': ''}
    assert text.Reformat_Dict_Quotes(props) == props