class Solution {
    public int maximalNetworkRank(int n, int[][] roads) {
        int maxRank = 0;
        Map<Integer, Set<Integer>> connectedCities = new HashMap<>();

        for (int[] road: roads){
            connectedCities.computeIfAbsent(road[0], k -> new HashSet<>()).add(road[1]);
            connectedCities.computeIfAbsent(road[1], k -> new HashSet<>()).add(road[0]);
        }

        for (int i = 0; i < n - 1; i++){
            for (int j = i + 1; j < n; j++){
                int currentRank = connectedCities.getOrDefault(i, Collections.emptySet()).size() + connectedCities.getOrDefault(j, Collections.emptySet()).size();

                if (connectedCities.getOrDefault(i, Collections.emptySet()).contains(j)){
                    --currentRank;
                }
                maxRank = Math.max(maxRank, currentRank);
            }
        }

        return maxRank;
    }
}
