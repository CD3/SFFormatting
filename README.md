# Straight Forward Fromatting

A simple string formatter that stays out of the way.

## Motivation

I write python programs and I write LaTeX documents. Sometimes I write python programs that write LaTeX documents.
Using python's `string.format` function to format strings that contain LaTeX is a pain. All curly brackets that are part
of the LaTeX must be doubled up. For example, "\frac{1}{2}" must be written "\frac{{1}}{{2}}".

`SFFormatting` is a simple string formatting module that uses `pyparsing` to parse for tokens that need to be replaced, and then uses
the Python's `string.format` function to actually do the replacement. The parser does not complain about extra curly brackets in the text
to be formatted, or about missing parameters. So, for example, this just works:

```
#! /usr/bin/python

import sfformatting

mass = 2 # kg
velocity = 10 # m/s

text = r"Kinetic energy is $\frac{1}{2} m v^2$. So a {mass} kg mass moving at {velocity} m/s has a kinetic energy of {energy} J."
text = sfformatting.fmt( text, mass=mass, velocity=velocity, energy=0.5*mass*velocity**2 )

print text


Output:
>>> Kinetic energy is $\frac{1}{2} m v^2$. So a 2 kg mass moving at 10 m/s has a kinetic energy of 100.0 J.


```

I use the LaTeX [`siunitx` package](https://www.ctan.org/pkg/siunitx?lang=en) to format units. This works too:
```
#! /usr/bin/python

import sfformatting

mass = 2 # kg
velocity = 10 # m/s

text = r"Kinetic energy is $\frac{1}{2} m v^2$. So a \SI{{mass}}{\kilo\gram} mass moving at \SI{{velocity}}{\meter\per\second} has a kinetic energy of \SI{{energy}}{\joule}."
text = sfformatting.fmt( text, mass=mass, velocity=velocity, energy=0.5*mass*velocity**2 )

print text


Output:
>>> Kinetic energy is $\frac{1}{2} m v^2$. So a \SI{2}{\kilo\gram} mass moving at \SI{10}{\meter\per\second} has a kinetic energy of \SI{100.0}{\joule}.


```

## Installation

`SSFormatting` is a single file named `sfformatting.py`. Just stick it in your script's directory, or a directory
in your `PYTHONPATH`.
