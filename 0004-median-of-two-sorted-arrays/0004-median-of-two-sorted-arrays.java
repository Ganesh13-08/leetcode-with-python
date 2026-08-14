import java.util.*;
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int[] list = new int[m + n]; // exact size
        int i = 0, j = 0, k = 0;
        while(i<m && j<n){
            if(nums1[i]<nums2[j]){
                list[k] = nums1[i];
                i++;
                k++;
            }else{
                list[k] = nums2[j];
                k++;
                j++;
            }
        }
        while(i<m){
            list[k] = nums1[i];
            k++;
            i++;
        }
        while(j<n){
            list[k] = nums2[j];
            k++;
            j++;
        }
        int total = m+n;
        if(k%2==1){
            return list[total/2];
        }
        else{
            return (list[total/2] + list[total/2-1])/2.0;
        }
    } 
}