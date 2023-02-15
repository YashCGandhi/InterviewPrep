class Solution {
    List<String> mapping = new ArrayList<>(List.of("","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"));
    List<String> result = new ArrayList<>();

    void backtrack(String digits, String letters, int index){

        if(digits.length() == letters.length()){
            result.add(letters);
            return;
        }
        // the "-'0'" -> in digits.charAt(index)-'0' -> converts the character into an integer.
        String currDigit = mapping.get(digits.charAt(index) - '0');
        for (int i = 0; i < currDigit.length(); i++){
            backtrack(digits, letters + currDigit.charAt(i), index + 1);
        }
    }


    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0){
            return result;
        }
        backtrack(digits, "", 0);
        return result;
        
    }
}
