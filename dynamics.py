import numpy as np


def calc_kinetic_energy(m, v):
    return m*v**2/2


def calc_potential_energy(m, w, x):
    return m*(w*x)**2/2


def calc_total_energy(m, w, a):
    return m*(w*a)**2/2


def calc_deviation (a, w, t, f):
    return a * np.sin(w * t + np.pi/6*f)


def calc_osc_speed(t, w, a, f):
    return a*w*np.cos(w*t + np.pi/6*f)


def calc_osc_acceleration_magnitude(t, w, a, f):
    return -a*w**2*np.sin(w*t + np.pi/6*f)


def calc_tangential_acceleration(v_x, v_y, a_x, a_y):
    return (a_x * v_x + a_y * v_y)/(v_x ** 2 + v_y ** 2)**(1/2)


def calc_centripetal_acceleration(v_x, v_y, a_x, a_y):
    if (a_x**2 + a_y**2 - calc_tangential_acceleration(v_x,v_y,a_x,a_y)**2) < 0:
        return 0
    return (a_x**2 + a_y**2 - calc_tangential_acceleration(v_x,v_y,a_x,a_y)**2)**(1/2)


def calc_curvature(v_x, v_y, a_x, a_y):
    return calc_centripetal_acceleration(v_x,v_y,a_x,a_y)/(v_x**2+v_y**2)

