class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if(target<=nums[0]) return 0;
        if(target>nums[nums.size()-1]) return nums.size();
        int i=1;
        while(nums[i]<=target){
            if(nums[i]==target){return i;}
            i++;
        }
        return i;
    }
};