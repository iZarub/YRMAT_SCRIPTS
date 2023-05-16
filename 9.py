from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
from ipywidgets import widgets
from time import sleep


def main(*args):
    N = w_n.value
    alpha = w_alpha.value
    betta = w_betta.value
    q = w_q.value
    r = w_r.value
    h = 10/N
    t = np.linspace(0, 10, N)
    n = lambda x: np.exp(-alpha*(x-betta)**2) + 1
    f = lambda x, y: np.exp(y) - n(x)
    Phi = np.zeros(N)
    Phi[0] = q
    Phi[1] = q + h * r
    for i in range(2,N):
        Phi[i] = h**2 * f(h*(i-1), Phi[i-1]) + 2 * Phi[i-1] - Phi[i-2]
    with out2:
        clear_output(wait=True)
        fig = plt.figure(figsize=(7, 7))
        ax = fig.add_subplot(111)
        ax.plot(t, Phi)
        plt.show()


out1 = widgets.Output(layout={'width': '50%'})
out2 = widgets.Output(layout={'width': '50%'})  

w_alpha = widgets.IntSlider(description='Множитель под экспонентой ', min=1, max=100, step=1, value=3)
w_betta = widgets.IntSlider(description='Сдвиг под экспонентой ', min=0, max=1000, step=1, value=5)
w_q = widgets.IntSlider(description='Фи ', min=-100, max=0, step=1, value=0)
w_r = widgets.IntSlider(description='Фи штрих ', min=-100, max=0, step=1, value=0)
w_n = widgets.IntSlider(description='Число шагов ', min=10, max=1000, step=1, value=1000)

w_button = widgets.Button(description='Запустить', button_style='primary')
w_button.on_click(main)
display(widgets.HBox([out1, out2]))
with out1:
    display(
            w_n,
            w_alpha,
            w_betta,
            w_q,
            w_r,
            w_button,)
