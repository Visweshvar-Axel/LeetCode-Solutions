
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        // own eff
        int near = 0;
        int val = 0;
        for(int i = 0 ; i < nums.size(); i++) {
            if (nums[i] == target) {
                return i;
            }
            else if (nums[i] < target) {
                near = i;
                val = nums[i];
                }
        }
        if(val == 0) return near;
        return near+1;
    }
};
