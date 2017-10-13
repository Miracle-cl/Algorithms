# title: 42. Trapping Rain Water

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# For example,  Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        length = len(height)
        if length > 2:
            max_value = max(height)
            # find first and last maximum
            for i in range(length):
                if height[i] == max_value:
                    first_max = i
                    break
            for i in range(length):
                if height[length-i-1] == max_value:
                    last_max = length-i
                    break
            dif = last_max - first_max
            # volume of water in the left of first maximum
            i = 0
            while i < first_max:
                if height[i] > 0:
                    j = 1
                    while height[i+j] < height[i]:
                        water += (height[i] - height[i+j])
                        j += 1
                    i = i + j
                else:
                    i += 1
            # volume of water in the right of last maximum
            i = length - 1
            while i > last_max:
                if height[i] > 0:
                    j = 1
                    while height[i-j] < height[i]:
                        water += (height[i] - height[i-j])
                        j += 1
                    i = i - j
                else:
                    i -= 1
            # volume of water between first maximum and last maximum only when dif > 1
            if dif > 1:
                for i in range(first_max + 1, last_max):
                    water += (max_value - height[i])
        return water

height = [0,1,0,2,1,0,1,3,3,3,3,2,1,2,1]
height = [4,2,3]