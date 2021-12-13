import tkinter

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import dynamics


def update_graph(event):
    #Do usuniecia potem, ale narazie sie przydaje
    if str(event.key) == 'q':
        _quit()
    #----------
    try:
        w_y = int(event.key)
        line.set_ydata(np.sin(int(event.key) * t))
    except ValueError:
        w_y = 1
        line.set_ydata(np.sin(1 * t))
    fig.suptitle(f'Wykres dla: w1 = {w_x}, w2 = {w_y}')
    fig.canvas.draw()
    mpl.backend_bases.key_press_handler(event, canvas)


def set_up_canvas(c):
    c.draw()
    c.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    c.mpl_connect("key_press_event", update_graph)


def _quit():
    root.quit()
    root.destroy()


GRAPH_SIZE = 6
FONT_SIZE = 15
root = tkinter.Tk()
root.wm_title("Wykres drgan prostopadlych")

w_x = 2
w_y = 2
a_x = 1
a_y = 1
f = np.pi/2

t = np.arange(0, 10, 0.01)
x = a_x*np.sin(w_x*t)
y = a_y*np.sin(w_y*t + f)

fig = Figure(figsize=(GRAPH_SIZE, GRAPH_SIZE), dpi=100)
ax = fig.add_subplot(111)
line, = ax.plot(x, y, 'g-')
canvas = FigureCanvasTkAgg(fig, master=root)
fig.supxlabel("x [m]", fontsize=FONT_SIZE)
fig.supylabel("y [m]", fontsize=FONT_SIZE)
fig.suptitle("Wykres", fontsize=FONT_SIZE, fontweight=500)
set_up_canvas(canvas)

button = tkinter.Button(master=root, text="Zamknij", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()






#Propozycja jak będziemy mieli za dużo czasu:
def Td():
    ax = plt.axes(projection = '3d')

    t= np.arange(0,10,0.01)
    x = np.sin(2*t)
    y = np.sin(4*t)
    z = np.sin(6*t)

    ax.plot3D(x,y,z,'g-')
    plt.show()

#Td()

