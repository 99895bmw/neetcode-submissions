class Solution {
public:
    bool isAnagram(string s, string t) {
        #include <unordered_set>

        unordered_multiset<char> map_s;
        unordered_multiset<char> map_t;
        for(auto letter : s) map_s.insert(letter);
        for(auto letter : t) map_t.insert(letter);

        if(map_s == map_t) return true;
        return false;
        

    }
};
