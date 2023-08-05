class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        vector<int> arr2=arr;
        sort(arr.begin(),arr.end());
        int max=arr[arr.size()-1];
        int i=0;
        while(arr2[i]<max){
            i++;
        }
        return i;
    }
    //can also be solved by using search algorithms like linear and binary search algorithms.
};