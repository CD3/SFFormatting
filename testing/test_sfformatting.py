import pytest
from sfformatting import *


def test_sfformatting():

  formatter = SFFormatter()

  assert formatter.fmt("A {str}.", str="string") == "A string."
  assert formatter.fmt("kwarg = {k}. arg = {0}.", "B", k="A") == "kwarg = A. arg = B."
  assert formatter.fmt("x = {0:.2f}, y = {1:.2e}", 1, 20) == "x = 1.00, y = 2.00e+01"

def test_fmt():

  assert fmt("A {str}.", str="string") == "A string."
  assert fmt("kwarg = {k}. arg = {0}.", "B", k="A") == "kwarg = A. arg = B."
  assert fmt("x = {0:.2f}, y = {1:.2e}", 10, 20) == "x = 10.00, y = 2.00e+01"

def test_namespace():

  ns = Namespace()
  ns.x = 10
  ns.y = 20

  assert ns.fmt("x = {x}, y = {y}") == "x = 10, y = 20"
  assert ns.fmt("x = {x:.1f}, y = {y:.1f}") == "x = 10.0, y = 20.0"

def test_formatting_strings_with_newline_chars():
  formatter = SFFormatter()

  assert formatter.fmt("A {str}.", missing="missing") == "A {str}."
  assert formatter.fmt('''A {
str
}.''', missing="missing") == "A {\nstr\n}."
