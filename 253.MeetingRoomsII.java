class Solution {
    public int minMeetingRooms(int[][] intervals) {
        int[] start = new int[intervals.length];
        int[] end = new int[intervals.length];

        for(int i = 0; i < intervals.length; i++){
            start[i] = intervals[i][0];
            end[i] = intervals[i][1];
        }

        Arrays.sort(start);
        Arrays.sort(end);

        int s = 0;
        int e = 0;
        int count = 0;
        int res = 0;

        while (s < intervals.length) {
            if (start[s] < end[e]){
                count++;
                s++;
            } else{
                count--;
                e++;
            }
            res = Math.max(res, count);
        }


        return res;
    }
}
