import numdifftools as nd
import scipy

def f(x):
    """Get back the value of a function to a defined point.

    Keyword arguments:
    x -- the parameter
    """
    return (x + 3) * (x + 3)


def optimize_netwons_method (f, xt, xt1, epsilon, accuracy):
    """Get back the minimum value of a function

    Keyword arguments:
    f -- numpy function
    xt -- value
    xt1 -- value
    epsilon -- value
    accuracy -- value
    """
    if type(xt) != int:
        raise TypeError(f"xt must be numeric")
         
    while abs(xt-xt1) > accuracy:

        f1 = (f(xt1+epsilon) - f(xt1)) / epsilon
        f1epsilon = (f(xt1+epsilon+epsilon) - f(xt1+epsilon)) / epsilon
        f2 =  (f1epsilon - f1) / epsilon

        a = xt
        
        xt = xt1 - f1 / f2
        xt1 = a
    
    return xt

def optimize_multivariate_newtons_method(x0, f, tol=1e-4):
    xt1 = x0
    xt = x0 * 2
    while abs(xt-xt1) > 0.0001:
        xt1 = xt
        grad = nd.Gradient(f)
        hessian = nd.Hessian(f)
    
        xt= xt1 - scipy.linalg.solve(hessian(xt1), grad(xt1))
    return xt
    


