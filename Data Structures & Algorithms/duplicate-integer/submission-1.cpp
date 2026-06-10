class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        #include<unordered_map>

        unordered_map<int, int> mapper;

        for(auto number : nums){
            mapper[number]++;
        }

        for(auto it : mapper){
            if (it.second > 1) return true;
        }

        return false;
    }
};