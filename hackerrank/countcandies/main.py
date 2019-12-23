#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumPasses function below.
def minimumPasses(m, w, p, n):
    candies = 0
    step = 0
    while candies < n:
        step = step + 1
        candies = candies + m*w
        if candies > n:
            break
        extra = int(candies/p)
        if extra*p < (n - candies):
            candies = candies - extra*p
            max_candies = (m+extra)*w
            m_next = m + extra
            w_next = w
            for i in range(extra + 1):
                print((m+ extra - i)*(w + i), m , w)
                if (m+ extra - i)*(w + i) > max_candies:
                    max_candies = (m+ extra - i)*(w + i)
                    m_next = m + extra - i
                    w_next = w + i
            m = m_next
            w = w_next
    return step

if __name__ == '__main__':

    mwpn = input().split()

    m = int(mwpn[0])

    w = int(mwpn[1])

    p = int(mwpn[2])

    n = int(mwpn[3])

    result = minimumPasses(m, w, p, n)

    print(result)


