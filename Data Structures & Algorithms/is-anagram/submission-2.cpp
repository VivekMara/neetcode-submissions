class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        std::unordered_map<char, int> freq1;
        std::unordered_map<char, int> freq2;
        for (char c : s){
            freq1[c]++;
        }
        for (char c : t){
            freq2[c]++;
        }
        return freq1 == freq2;
    }
};
