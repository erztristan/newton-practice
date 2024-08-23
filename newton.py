def f(x):
    """Get back the value of a function to a defined point.

    Keyword arguments:
    x -- the parameter
    """
    return (x + 3) * (x + 3)


def optimize (f, xt, xt1, epsilon, accuracy):

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


