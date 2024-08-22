def f(x):
    return (x + 3) * (x + 3)


def optimize(xt, xt1, epsilon, accuracy):
    while abs(xt - xt1) > accuracy:
        f1 = (f(xt1 + epsilon) - f(xt1)) / epsilon
        f1epsilon = (f(xt1 + epsilon + epsilon) - f(xt1 + epsilon)) / epsilon
        f2 = (f1epsilon - f1) / epsilon

        a = xt

        xt = xt1 - f1 / f2
        xt1 = a

    return xt


print(optimize(100, 1, 0.0001, 0.0001))
