# This is a sample Python script.
import numpy as np
import matplotlib.pyplot as plt
import dynamics


def test_module():
    # Funkcja tymczasowa do usuniecia potem
    print(dynamics.calc_kinetic_energy(3, 3))
    print(dynamics.calc_potential_energy(1, 5, 3))
    print(dynamics.calc_osc_speed(0.5, 3.14, 10))
    print(dynamics.calc_osc_acceleration_magnitude(0.5, 3.14, 10))

test_module()

#Inicjalizacja czestowsci wlasnych i amplitud
w_x = 2
w_y = 3
a_x = 1
a_y = 1
f = np.pi/2

#trajektoria w postaci paramatrycznej
t = np.arange(0,10,0.01)
x = a_x*np.sin(w_x*t)
y = a_y*np.sin(w_y*t + f)

plt.plot(x,y,'g-')
plt.show()
