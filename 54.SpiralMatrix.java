class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        
        if (matrix.length == 0){
            return result;
        }

        int left = 0;
        int right = matrix[0].length - 1;
        int top = 0;
        int bottom = matrix.length - 1;

        while (top <= bottom && left <= right){
            
            // top left -> top right
            for (int j = left; j <= right; j++){
                result.add(matrix[top][j]);
            }
            top++;
            
            // top right -> bottom right
            for (int j = top; j <= bottom; j++){
                result.add(matrix[j][right]);
            }
            right--;
            

            if (top <= bottom){
                // bottom right -> bottom left
                for (int j = right; j >= left; j--){
                    result.add(matrix[bottom][j]);
                }
            }
            
            bottom--;
            
            if (left <= right){
                // bottom left -> top left
                for( int j = bottom; j >= top; j--){
                    result.add(matrix[j][left]);
                }
            }
            left++;

        }
       
       return result;
        
    }
}
