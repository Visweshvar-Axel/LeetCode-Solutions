
class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0) return false;
        int num = x;
        int rev = 0;
        do{
            rev = rev * 10 + num % 10;
        }while((num/=10)>0);
        if (rev == x) return true;
        return false;
        // String num = Integer.toString(x);
        // int n = num.length();
        // for(int i = 0; i < n; i++) {
        //     if (num.charAt(i) != num.charAt(n-1-i)) return false;
        // }
        // return true;
    }
}
