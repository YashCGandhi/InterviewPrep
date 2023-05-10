class Solution {
    public int[] plusOne(int[] digits) {
        final int len = digits.length;
        int[] newDigits = new int[len + 1];
        int carry = 1;
        int curSum = 0;

        for (int i = len - 1; i >= 0; i--){
            curSum = digits[i] + carry;
            if (curSum > 9){
               digits[i] = curSum % 10;
               newDigits[i + 1] = digits[i];
               carry = 1; 
            } else{
                digits[i] = curSum;
                newDigits[i + 1] = digits[i];
                carry = 0;
                break;
            }
        }

        if (carry == 1){
            newDigits[0] = 1;
            return newDigits;
        }

        return digits;
    }
}
