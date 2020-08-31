import random
import math 
from typing import List


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        # in r, 2*r cycles with different probability
        d = math.sqrt(random.uniform(0, 1)) * self.r
        theta = random.random() * 2 * math.pi
        x = math.cos(theta) * d + self.x
        y = math.sin(theta) * d + self.y
        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()