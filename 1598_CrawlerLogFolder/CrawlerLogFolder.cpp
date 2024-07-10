
class Solution {
public:
    int minOperations(vector<string>& logs) {
        // own effeciant
        int need = 0;
        for(string s : logs) {
            if(s == "../") {
                if(need == 0) continue;
                need--; 
                continue;
            }
            else if(s == "./") continue;
            else if(s.back() == '/') need++;
        }
        return need;
    }
};
