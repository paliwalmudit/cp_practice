class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int t=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==target){t++; return i;}
        }
        if(t==0){
            for(int i=0;i<nums.size();i++){
                if(nums[i]>target){t=i;break;}
                else{t++;}
            }
        }
        return t;

    }
};