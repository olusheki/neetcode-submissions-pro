class Solution {
    public int pivotIndex(int[] nums) {
        int arrSum = 0;
        for (int i = 0; i<nums.length;i++) {
            arrSum += nums[i];
        }
        int curSum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (curSum == arrSum - curSum - nums[i]) {
                return i;
            }
            curSum += nums[i];
        }
        return -1;
    }
}