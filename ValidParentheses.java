import java.util.*;

class Solution {
    boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '{' || c == '[' || c == '(') {
                stack.push(c);
            } else {
                if (stack.isEmpty())
                    return false;
                char temp = stack.pop();
                if (c == '}' && temp != '{' || c == ']' && temp != '[' || c == ')' && temp != '(')
                    return false;
            }
        }
        return stack.isEmpty();
    }
    /*
     * *
     * bool isValid(string s) {
     * char[] stack = new char[s.length()];
     * int t=-1;
     * for(char c: s.toCharArray()){
     * if (c == '{' || c == '[' || c == '(') {
     * stack[++t] = c;
     * } else {
     * char temp = stack[t--];
     * if (c == '}' && temp != '{' || c == '}' && temp != '{' || c == '}' && temp !=
     * '{') {
     * return false;
     * }
     * }
     * }
     * return t == -1;
     * }
     * }
     */
}