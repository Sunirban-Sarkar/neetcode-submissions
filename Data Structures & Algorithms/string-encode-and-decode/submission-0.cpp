class Solution {
public:

    string encode(vector<string>& strs) {
        string res;
        for(const auto& s: strs){
            res += to_string(s.length())+"#"+s;
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> ans;
        int i=0;
        while(i<s.length()){
            int j=i;
            while(j<s.length() && s[j]!='#'){
                j++;
            }
            int len = stoi(s.substr(i, j-i+1));
            ans.push_back(s.substr(j+1, len));
            i=j+len+1;
        }
        return ans;
    }
};
