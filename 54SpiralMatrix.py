    def sizeof(self,row,col):
        return row*col
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0])-1
        top = 0
        bottom = len(matrix)-1
        size = len(matrix) * len(matrix[0])
        res = []
        while len(res) < size:
            i = left
            while i <= right and len(res) < size:
                res.append(matrix[top][i])
                i+=1
            print(res)
            top += 1
            i = top
            while i <= bottom and len(res) < size:
                res.append(matrix[i][right])
                i+=1
            print(res)
            right -= 1
            i = right
            while i >= left and len(res) < size:
                res.append(matrix[bottom][i])
                i -= 1
            print(res)
            bottom -= 1
            i = bottom
            while i >= top and len(res) < size:
                res.append(matrix[i][left])
                i-=1
            left += 1
            print(res)
        return res
    
                
