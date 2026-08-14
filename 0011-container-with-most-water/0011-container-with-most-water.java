import java.util.*;
class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length-1;
        List<Integer> list = new ArrayList<Integer>();
        while(left < right){
            if(height[left] == height[right]){
                list.add(height[left]*(right-left));
                left++;
            }
            if(height[left] < height[right]){
                list.add(height[left]*(right-left));
                left++;
            }
            if(height[left] > height[right]){
                list.add(height[right]*(right-left));
                right--;
            }
        }
        int max = Collections.max(list);
        return max;
    }
}