# LeetCode 74: Search a 2D Matrix
#
# Name: Parjad Minooei
# Date: October 20, 2025
#
# Time Complexity: O(log(m*n)) - Standard binary search on the total number of elements.
# Space Complexity: O(1) - We only use pointers.
#
# Key Insight: (Binary Search on a "Virtual" 1D Array)
# The matrix is sorted in a way that allows us to treat it as a single, flattened, sorted array.
# We can perform a classic binary search on the range of indices from 0 to (m*n - 1).
# The only trick is converting the 1D "middle" index back into a 2D (row, col) coordinate
# to check the value in the actual matrix.

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, (ROWS * COLS) - 1

        while l <= r:
            m_index = (l + r) // 2
            
            # Convert the 1D middle index to 2D coordinates
            m_val = matrix[m_index // COLS][m_index % COLS]

            if m_val > target:
                r = m_index - 1
            elif m_val < target:
                l = m_index + 1
            else:
                return True
        
        return False

