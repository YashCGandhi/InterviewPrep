class Solution {
    public boolean mergeTriplets(int[][] triplets, int[] target) {
        boolean[] trip = new boolean[target.length];
        for (int i = 0; i < trip.length; i++){
            trip[i] = false;
        }

        for (int[] t : triplets){
            if (t[0] > target[0] || t[1] > target[1] || t[2] > target[2]){
                continue;
            }

            for ( int j = 0; j < t.length; j++){
                if (t[j] == target[j]){
                    trip[j] = true;
                }
            }
            boolean checker = true;
            for ( boolean b : trip){
                if (b == false){
                    checker = false;
                }
            }
            if (checker){
                return true;
            }
        }
        return false;
    }
}
