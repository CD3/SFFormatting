#! /usr/bin/python

import sfformatting

mass = 2 # kg
velocity = 10 # m/s

text = r"Kinetic energy is $\frac{1}{2} m v^2$. So a \SI{{mass}}{\kilo\gram} mass moving at \SI{{velocity}}{\meter\per\second} has a kinetic energy of \SI{{energy}}{\joule}."
text = sfformatting.fmt( text, mass=mass, velocity=velocity, energy=0.5*mass*velocity**2 )

print text
