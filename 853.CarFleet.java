class Solution {
    public int carFleet(int target, int[] pos, int[] speed) {
        int N = pos.length, res = 0;
        double[][] pair = new double[N][2];

        for ( int i = 0; i < N; i++){
            pair[i] = new double[]{pos[i], (double)(target - pos[i]) / speed[i]};
        }
        Arrays.sort(pair,(a, b) -> Double.compare(a[0], b[0]));
        double curr = 0;
        for ( int i = N - 1; i >= 0; i--){
            if(pair[i][1] > curr){
                curr = pair[i][1];
                res ++;
            }

        }
        return res;

    }
}
