class Solution {
    public int numTrees(int n) {
        int[] numTree = new int[n + 1];
        numTree[0] = numTree[1] = 1;
        for ( int nodes = 2; nodes <= n ; nodes++){
            int total = 0;
            for (int root = 1; root < nodes + 1; root++){
                int left = root - 1;
                int right = nodes - root;

                numTree[nodes] += numTree[left] * numTree[right];

            }
        }

        return numTree[n];

    }
}
