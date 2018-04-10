import numpy as np
from maxima import find_maxima

x = [0, 1, 2, 1, 2, 1, 0]
print(len(x))
print(range(len(x)))
print(find_maxima(x))
x = [-i**2 for i in range(-3, 4)]
print(find_maxima(x))
x = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
print(find_maxima(x))

x = [4, 2, 1, 3, 1, 2]
print(len(x))
print(range(len(x)))
print(find_maxima(x))
x = [4, 2, 1, 3, 1, 5]
print(find_maxima(x))
x = [4, 2, 1, 3, 1]
print(find_maxima(x))
