class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        right=len(matrix)-1

        while left<=right:
            mid=(left+right)//2
            if target > matrix[mid][len(matrix[0])-1]:
                left=mid+1
            elif target < matrix[mid][0]:
                right=mid-1
            else:
                low=0
                high=len(matrix[0])-1
                while low <= high:
                    middle = (low+high)//2
                    if matrix[mid][middle] ==target:
                        return True
                    elif matrix[mid][middle] < target:
                        low=middle + 1
                    else:
                        high=middle -1
                return False

        return False



        