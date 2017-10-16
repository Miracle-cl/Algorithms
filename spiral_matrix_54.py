class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix:
            m = len(matrix)
            n = len(matrix[0])
            number = m * n
            result = []
            left = top = 0
            right = n-1
            bottom = m -1
            j = -1
            i = 0
            while left < right and top < bottom:
                while j < right:
                    j += 1
                    result.append(matrix[top][j])
                top += 1
                while i < bottom:
                    i += 1
                    result.append(matrix[i][right])
                right -= 1
                while j > left:
                    j -= 1
                    result.append(matrix[bottom][j])
                bottom -= 1
                while i > top:
                    i -= 1
                    result.append(matrix[i][left])
                left += 1
            if left == right and top == bottom:
                result.append(matrix[top][left])
            elif left == right:
                for i in range(top, bottom+1):
                    result.append(matrix[i][left])
            elif top == bottom:
                for i in range(left, right+1):
                    result.append(matrix[top][i])
            return result
        else:
            return []
