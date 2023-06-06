import numpy as np

def malthus(t,x,a):
    """Equação diferencial de Malthus
    """
    return a*x

def verhulst(t,x,a):
    """Equação diferencial de Verhulst
    """
    return a * x * (1-x)

def gompertz(t,x, a):
    """Equação diferencial de Gompertz
    """
    return a * x * np.log(1/x)

def runge_kutta(eq, t0, x0, tf, h, a):
    t = np.arange(t0, tf + h, h)
    x = np.zeros(len(t))
    x[0] = x0
    for i in range(1, len(t)):
        k1 = eq(t[i-1], x[i-1], a)
        k2 = eq(t[i-1] + h/2, x[i-1] + k1/2, a)
        k3 = eq(t[i-1] + h/2, x[i-1] + k2/2, a)
        k4 = eq(t[i-1] + h, x[i-1] + k3, a)
        x[i] = x[i-1] + h * (k1 + 2*k2 + 2*k3 + k4)/6
    return t, x