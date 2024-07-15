
#include<cstdlib>
class Solution {
public:
    int scoreOfString(string s) {
        int num = 0;
        for (int i = 0; i < s.length()-1; i++) {
            num +=  abs(s[i]-s[i+1]);
        }
        return num;
    }
};
