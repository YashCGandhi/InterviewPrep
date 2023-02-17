class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int n = s1.length();
        int m = s2.length();

        if (n > m){
            return false;
        }

        int[] count = new int[26];
        for ( int i = 0; i < n; i++){
            count[s1.charAt(i) - 'a']++;
            count[s2.charAt(i) - 'a']--;
        }
        if ( allZeros(count)) return true;

        for (int i = n; i < m; i++){
            count[s2.charAt(i) - 'a']--;
            count[s2.charAt(i - n) - 'a']++;
            if (allZeros(count)) return true;
        }
        return false;

    }

    private boolean allZeros(int[] count){
        for ( int i = 0; i < count.length; i++){
            if(count[i] != 0) return false;
        }
        return true;
    }
}
