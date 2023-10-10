import numpy as np


def calculate_G(L: float, D: float, N: float, time: float):
    T = time/N
    R = D/2
    _L = L + R
    return (4 * L * np.pi * np.pi)/(T * T)

def calculate_G(l: float, r: float, T: float):
    return 4 * np.pi * np.pi * (l + r)/(T * T)

ls = [75.7, 75.71, 75.72, 75.75, 75.72, 75.78]

Ds = [20.04, 20.04, 20.04, 20.04, 20.04, 20.06]

times = [87.72, 87.62, 87.75, 87.69, 87.88, 87.72]

l = np.mean(ls)/100
r = np.mean(Ds)/2000
T = np.mean(times)/50

g = calculate_G(l, r, T)

print("G is: {:.6f}".format(g))
print("The relative error is {:.4f}%".format(np.abs((g - 9.7887)/(9.7887))))