#! /usr/bin/python


mass = 2 # kg
velocity = 10 # m/s

text = r"Kinetic energy is $\frac{1}{2} m v^2$. So a {mass} kg mass moving at {velocity} m/s has a kinetic energy of {energy} J."
text = text.format( mass=mass, velocity=velocity, energy=0.5*mass*velocity**2 )

print text
