class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int left = 1, right = 1;
        for (int p : piles){
            right = Math.max(right, p);
        }
        int res = right;
        while (left < right){
            int mid = (left + right) / 2;
            int hoursSpent = 0;
            for ( int p : piles){
                hoursSpent += Math.ceil((double) p / mid);
            }

            if(hoursSpent <= h){
                res = Math.min(res, mid);
                right = mid;
            }
            else{
                left = mid + 1;
            }
        }
        return res;
    }
}
