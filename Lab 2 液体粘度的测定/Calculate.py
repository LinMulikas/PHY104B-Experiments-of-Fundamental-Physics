import numpy as np

def calculate(phi: float, rho: float, rho_0: float, g: float, v_f: float, D: float, H: float):
    return np.power(phi, 2)*g*(rho - rho_0)/(18*v_f*(1 + 2.4*phi/D)*(1 + 1.7*phi/H))


print(calculate())