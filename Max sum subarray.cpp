/* Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
*/

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currsum = nums[0];
        int maxsum = nums[0];
        for(int i=1;i<nums.size();i++)
        {
            currsum = max(nums[i], currsum + nums[i]);
            if(currsum > maxsum)
                maxsum = currsum;
            
            /* saving indices to print subarray
            if(currsum + nums[i] >= nums[i])
            {
                currsum = currsum + nums[i];
            }
            else
            {
                currsum = nums[i];
                start = i;
            }
            
            if(currsum > maxsum)
            {
                maxsum = currsum;
                end = i;
            }*/
            
        }
        return maxsum;
    }
};