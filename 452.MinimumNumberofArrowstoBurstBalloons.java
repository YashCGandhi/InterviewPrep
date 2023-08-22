class Solution {
    public int findMinArrowShots(int[][] points) {
        if(points.length == 0) return 0;

        Arrays.sort(points, (o1, o2) -> {
            if (o1[1] == o2[1]) return 0;
            if (o1[1] < o2[1]) return -1;
            return 1;
        });

        int arrows = 1;
        int lastEnd = points[0][1];
        int start, end;

        for (int[] p: points){
            start = p[0];
            end = p[1];

            if (start > lastEnd){
                arrows++;
                lastEnd = end;
            }
        }

        return arrows;
    }
}
