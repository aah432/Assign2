# Amber Harding Assign 2
import numpy as np

l = [[0, 1], [1, 1]]        # Representation for L as matrix


def nth_power(matrix, n):
    if n == 1:
        return matrix
    if (n % 2) == 0:
        temp = nth_power(matrix, n / 2)
        return np.dot(temp, temp)
    else:
        temp = nth_power(matrix, n // 2)
        return np.dot(matrix, np.dot(temp, temp))


def fibPow(l, n):               # Write a function fibPow that takes a natural number n, and returns (L^n(0, 1))
    ln = nth_power(l, n)
    return np.dot(ln, [0, 1])[1]


if __name__ == '__main__':
    print(fibPow(l, 6))

