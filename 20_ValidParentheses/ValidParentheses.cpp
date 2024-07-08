
#include <stack>
using namespace std;
class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        for(char c: s){
            if (c == '{' || c == '[' || c == '(') {
                stack.push(c);
            } else {
                if (stack.empty()) return false;
                char temp = stack.top();
                stack.pop();
                if (c == '}' && temp != '{' || c == ']' && temp != '[' || c == ')' && temp != '(') return false;
            }
        }
        return stack.empty();
    }
    /* *
        bool isValid(string s) {

        char stack[s.length()];
        int t=-1; 
        for(char c: s){
            if (c == '{' || c == '[' || c == '(') {
                stack[++t] = c;
            } else {
                if (t == -1) return false;
                char temp = stack[t--];
                if (c == '}' && temp != '{' || c == ']' && temp != '[' || c == ')' && temp != '(') return false;
            }
        }
        return t == -1;



        }
    }
    */
};
