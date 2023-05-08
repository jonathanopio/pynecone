from pynecone import Html

def test_no_heading():
    html = Html.create("")
    string = '<p>This is a paragraph.</p>'
    expected_text, expected_format = "", ""
    assert html.Format_Headings(string) == (expected_text, expected_format)

def test_valid_heading():
    html = Html.create("")
    string = '<h2>This is a heading.</h2>'
    expected_text, expected_format = "This is a heading.", "2xl"
    assert html.Format_Headings(string) == (expected_text, expected_format)

def test_invalid_heading():
    html = Html.create("")
    string = '<h7>Invalid heading</h7>'
    expected_text, expected_format = "", ""
    assert html.Format_Headings(string) == (expected_text, expected_format)

def test_empty_string():
    html = Html.create("")
    string = ''
    expected_text, expected_format = "", ""
    assert html.Format_Headings(string) == (expected_text, expected_format)

def test_no_text():
    html = Html.create("")
    string = '<h1></h1>'
    expected_text, expected_format = "", "3xl"
    assert html.Format_Headings(string) == (expected_text, expected_format)
