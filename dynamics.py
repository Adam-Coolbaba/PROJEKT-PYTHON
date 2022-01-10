import numpy as np


def calc_kinetic_energy(m, v):
    return m*v**2/2


def calc_potential_energy(m, w, x):
    return m*(w*x)**2/2


def calc_deviation (a, w, t, f):
    return a * np.sin(w * t + np.pi/6*f)


def calc_osc_speed(t, w, a, f):
    return a*w*np.cos(w*t + np.pi/6*f)


def calc_osc_acceleration_magnitude(t, w, a, f):
    return -a*w**2*np.sin(w*t + np.pi/6*f)


def calc_curvature(v_x, v_y, a_x, a_y):
    return (v_x**2+v_y**2)/(a_x**2+a_y**2 - (a_x*v_x+a_y*v_y)**2/(v_x**2+v_y**2))**(1/2)

