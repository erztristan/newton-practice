def f(x):
    """Get back the value of a function to a defined point.

    Keyword arguments:
    x -- the parameter
    """
    return (x + 3) * (x + 3)


def optimize(xt, xt1, epsilon, accuracy):
    """Get back the zero point for a function defined in f(x)

    Keyword arguments:
    xt -- start of the optimization
    xt1 -- second start point of the optimization
    epsilon -- value for the calculation of the derivation
    accuracy -- value when the algorithmus stop
    """
    while abs(xt - xt1) > accuracy:
        f1 = (f(xt1 + epsilon) - f(xt1)) / epsilon
        f1epsilon = (f(xt1 + epsilon + epsilon) - f(xt1 + epsilon)) / epsilon
        f2 = (f1epsilon - f1) / epsilon

        a = xt

        xt = xt1 - f1 / f2
        xt1 = a

    return xt


print(optimize(100, 1, 0.0001, 0.0001))
