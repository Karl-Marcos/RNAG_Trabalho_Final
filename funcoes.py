import numpy as np

def malthus(t,x,k):
    """Equação diferencial de Malthus
    """
    return k*x

def verhulst(t,x,a):
    """Equação diferencial de Verhulst
    """
    return a * x * (1-x)

def gompertz(t,x, a):
    """Equação diferencial de Gompertz
    """
    return a * x * np.log(1/x)


def runge_kutta(dx, t0, x0, tf, h, k):
    t_values = [t0]  # List to store time values
    x_values = [x0]  # List to store x values

    while t0 < tf:
        if t0 + h > tf:
            h = tf - t0  # Adjust the step size for the last iteration if necessary
        k1 = dx(t0, x0, k)
        k2 = dx(t0 + h/2, x0 + h/2 * k1, k)
        k3 = dx(t0 + h/2, x0 + h/2 * k2, k)
        k4 = dx(t0 + h, x0 + h * k3, k)

        x0 = x0 + (h/6) * (k1 + 2*k2 + 2*k3 + k4)  # Update x using the Runge-Kutta formula
        t0 += h  # Increment the time
        t_values.append(t0)  # Add current time and x value to the lists
        x_values.append(x0)

    return np.array(t_values), np.array(x_values)