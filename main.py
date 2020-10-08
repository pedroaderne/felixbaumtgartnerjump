from numpy import *
from math import *
import pandas as pd
import matplotlib.pyplot as plt

a = 0.68508  # área de contato
m = 96  # massa
s = 38970  # posição

def mov(s):  # descrição do movimento
    dt = 0.001  # deltaTw
    t = 0  # tempo inicial
    v = 0  # velocidade inicial
    gravity_acc = -9.68  # gravidade
    acc = -9.68  # aceleração inicial
    c = 0.7236  # coeficiente de arrasto
    agrupamento_de_grandezas = {'Velocity': [], 'Time': []}
    while s > 0:
        t = t + dt
        fi = (1.225 * e) ** (-s / 8882)
        fora_de_resistance_do_ar = (c * a * (v ** 2) * fi) / 2
        aceleracao_da_resitencia_do_ar = fora_de_resistance_do_ar / m
        acc_new = gravity_acc + aceleracao_da_resitencia_do_ar  # nova aceleração
# Velocity-Verlet
        s = s + v * dt + ((acc * (dt ** 2)) / 2)
        v = v + (acc_new + acc) * (dt / 2)
        acc = acc_new
        if t > 200:  # momento da abertura do paraquedas
            c =2
            print(s, v, t, aceleracao_da_resitencia_do_ar, acc)
        agrupamento_de_grandezas['Velocity'].append(-v)
        agrupamento_de_grandezas['Time'].append(t)
    return agrupamento_de_grandezas


descricao_do_movimento = mov(s)
df = pd.DataFrame(descricao_do_movimento['Velocity'], index=descricao_do_movimento['Time']).plot(kind='line',
                                                                                                 color='pink',
                                                                                                 title='Simulação '
                                                                                                       'salto Felix '
                                                                                                       'Baumgartner',
                                                                                                 legend=False,
                                                                                                 figsize=(8,4))
df.set_ylim(bottom=0, top=385)
df.set_xlim(left=0, right=270)
plt.xlabel('Tempo(s)')
plt.ylabel('Velocidade (m/s)')
plt.axvline(descricao_do_movimento['Time'][0], color='r')
plt.axhline(0, color='r')
plt.show()



