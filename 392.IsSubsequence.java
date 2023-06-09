class Solution {
    public boolean isSubsequence(String s, String t) {
        int pointer = 0;
        int n = s.length();

        if (n == 0){
            return true;
        }
        for (int i = 0; i < t.length(); i++){
            if (s.charAt(pointer) == t.charAt(i)){
                pointer++;
            }
            if (pointer >= n){
                return true;
            }
        }
        

        return false;
    }
}
