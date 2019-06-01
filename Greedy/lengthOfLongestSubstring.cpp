class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> visited;
        int begin = -1;
        int maxlen = 0;
        for (int i = 0; i < s.size(); i++) {
            if (visited.find(s[i]) != visited.end() and begin < visited[s[i]])
                begin = visited[s[i]];
            else
                maxlen = std::max(maxlen, i-begin);
            visited[s[i]] = i;
        }
        return maxlen;
    }
};
