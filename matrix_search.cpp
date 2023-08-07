class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        for(auto i:matrix){
            for(auto j:i){
                if(j==target) return true;
            }
        }
        return false;
    }
};

// can also be solved by binary search and 2 pointer matrix traversal.