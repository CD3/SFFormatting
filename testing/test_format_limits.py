import pytest


def test_delimiters():

  assert "{NAME}".format(NAME="Rusty") == "Rusty"
  assert "{{NAME}}".format(NAME="Rusty") == "{NAME}"
  assert "<<NAME>>".format(NAME="Rusty") == "<<NAME>>"
  with pytest.raises(ValueError):
    assert "{{NAME}".format(NAME="Rusty") == "{{Name}"

def test_latex():


  assert r"\includegraphics{{filename}}".format(filename="image.png") != r"\includegraphics{image.png}"
  assert r"\includegraphics{{{filename}}}".format(filename="image.png") == r"\includegraphics{image.png}"
  assert r"\includegraphics{{{{filename}}}}".format(filename="redirect").format(redirect="image.png") != r"\includegraphics{image.png}"
  with pytest.raises(IndexError):
    assert r"\frac{1}{2}".format(filename="image.png") == r"\frac{1}{2}"
  assert r"\frac{{1}}{{2}}".format(filename="image.png") == r"\frac{1}{2}"
