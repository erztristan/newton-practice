import pytest
import numpy as np
import math

import newton

def test_basic_function():
    assert np.isclose(newton.optimize(np.cos, 3,2,0.00001, 0.00001), math.pi)

def test_bad_input():
    with pytest.raises(TypeError, match='xt must be numeric'):
        newton.optimize(3, np.cos ,2,0.001, 0.001)

