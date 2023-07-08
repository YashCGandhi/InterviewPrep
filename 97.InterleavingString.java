class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1.length() + s2.length() != s3.length()){
            return false;
        }
        boolean [][] dp = new boolean[s1.length() + 1][s2.length() + 1];

        for (int i = 0; i <= s1.length(); i++){
            for (int j = 0; j <= s2.length(); j++){
                dp[i][j] = false;
            }   
        }

        dp[s1.length()][s2.length()] = true;


        for (int i = s1.length(); i >= 0; i--){
            for (int j = s2.length(); j >= 0; j--){
                if (i < s1.length() && s1.charAt(i) == s3.charAt(i + j) && dp[i + 1][j] == true){
                    dp[i][j] = true;
                } 
                if (j < s2.length() && s2.charAt(j) == s3.charAt(i + j) && dp[i][j + 1] == true){
                    dp[i][j] = true;
                }
            }
        }
        return dp[0][0];


    }
}
