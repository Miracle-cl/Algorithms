# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

import random


def rand7():
    return random.randint(1, 7)


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            r = rand7()
            c = rand7()
            n = c + (r - 1) * 7
            if n <= 40:
                break
        return 1 + (n-1) % 10

    def rand10_1(self):
        """
        :rtype: int
        """
        while True:
            r = rand7()
            c = rand7()
            n = c + (r - 1) * 7
            if n <= 40:
                return 1 + (n-1) % 10 # fixed n = 40
            r = n - 40
            c = rand7()
            n = c + (r - 1) * 7
            if n <= 60:
                return 1 + (n-1) % 10
            r = n - 60
            c = rand7()
            n = c + (r - 1) * 7
            if n <= 20:
                return 1 + (n-1) % 10
            # else residual 1
        