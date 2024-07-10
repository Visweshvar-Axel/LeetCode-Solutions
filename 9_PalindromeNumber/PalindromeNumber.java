class Solution {
    public boolean isPalindrome(int x) {
        // effeciant
        if (x < 0 || (x % 10 == 0 && x != 0))
            return false;
        int rev = 0;
        while (x > rev) {
            rev = rev * 10 + x % 10;
            x /= 10;
        }
        return x == rev || x == rev / 10;
        // if(x < 0) return false;
        // int num = x;
        // int rev = 0;
        // do{
        // rev = rev * 10 + num % 10;
        // }while((num/=10)>0);
        // if (rev == x) return true;
        // return false;
        //
        // String num = Integer.toString(x);
        // int n = num.length();
        // for(int i = 0; i < n; i++) {
        // if (num.charAt(i) != num.charAt(n-1-i)) return false;
        // }
        // return true;
    }
}