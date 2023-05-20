class DetectSquares {
    int[][] cntPoints = new int[1001][1001];
    List<int[]> points = new ArrayList<>();
    public DetectSquares() {
        
    }
    
    public void add(int[] point) {
        cntPoints[point[0]][point[1]]++;
        points.add(point);
    }
    
    public int count(int[] point) {
        int x = point[0], y = point[1], res = 0;
        for(int[] p: points){
            int px = p[0], py = p[1];
            if (Math.abs(x - px) != Math.abs(y - py) || x == px || y == py){
                continue;
            }
            res += cntPoints[x][py] * cntPoints[px][y]; 
        }

        return res;
    }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * DetectSquares obj = new DetectSquares();
 * obj.add(point);
 * int param_2 = obj.count(point);
 */
