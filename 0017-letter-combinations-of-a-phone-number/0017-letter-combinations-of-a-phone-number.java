class Solution {
    private static final String[] kp = {"/",".","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};


     public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.length() == 0) return result;

        comb(digits, 0, "", result);
        return result;
    }


    private void comb(String digits, int idx, String combinations,List<String> result){
        if(idx == digits.length()){
            result.add(combinations);
            return;
        }
        char curr = digits.charAt(idx);
        String mapping = kp[curr - '0'];
        for(int i=0; i<mapping.length(); i++){
            comb(digits,idx+1,combinations + mapping.charAt(i),result);
        }
    }
}