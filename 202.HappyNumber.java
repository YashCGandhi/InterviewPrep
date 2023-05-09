class Solution {
    public boolean isHappy(int n) {
        Set<Integer> set = new HashSet<>();

        int s1 = n;
        while (s1 != 1){
            int tmp = 0;
            while (s1 > 0){
                tmp += Math.pow(s1%10, 2);
                s1 = (int)s1/10;
            }
            s1 = tmp;
            if (set.contains(s1)){
                return false;
            }else{
                set.add(s1);
            }

        }
    return true;
    }
}
