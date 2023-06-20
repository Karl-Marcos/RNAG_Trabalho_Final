import numpy as np


##############################################################
##                   MODELOS POPULACIONAIS                  ## 
##############################################################
def malthus(t,x,k):
    """Equação diferencial de Malthus: dx/dt = kx
    Args:
        t: float variável t
        x: float variável x
        k: float constante k
    Returns:
        derivada dx/dt no ponto x
    """
    return k*x

def verhulst(t,x,k):
    """Equação diferencial de Verhulst: dx/dt = k x (1-x)
    Args:
        t: float variável t
        x: float variável x
        k: float constante k
    Returns:
        derivada dx/dt no ponto x
    """
    return k * x * (1-x)

def gompertz(t,x,k):
    """Equação diferencial de Gompertz: dx/dt = k x ln(1/x)
    Args:
        t: float variável t
        x: float variável x
        k: float constante k
    Returns:
        derivada dx/dt no ponto x
    """
    return k * x * np.log(1/x)


def runge_kutta(dx, t0, x0, tf, h, k):
    """ Resolve numericamente uma equação diferencial usando o método de runge-kutta.
    Args:
        dx: função da derivada (equação diferencial) ex: malthus, verhulst, gompertz.
        t0: instante inicial
        x0: valor inicial de x
        tf: valor final de t
        h: esaçamento dos pontos em t
        k: constante k
    Returns: 
        array dos pontos t, array dos pontos calculados de x
    """
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

##############################################################
##             FUNÇÔES RELACIONADAS A BUSCA                 ## 
##############################################################

def Div(left, right):
    if type(right) == float:
        if right == 0:
            #print('div error')
            return 1
        else:
            return left / right
    else:
        # Replace zero terms in the divider array with 1
        right_without_zeros = np.where(right == 0, 1, right)

        # Perform element-wise division
        result = left / right_without_zeros
        return result

def Exp(x):
    try:
        result = np.exp(x)
    except OverflowError:
        print('exp error')
        result = np.ones_like(x)
    return result