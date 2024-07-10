class Solution {
public:
    bool isPalindrome(int x) {
        //effeciant
        if(x < 0 || ( x%10 == 0 && x != 0 )) return false;
        int rev = 0;
        while( x > rev){
            rev = rev * 10 + x % 10;
            x /= 10;
        }
        return x == rev || x == rev/10;
        // 
        // if(x < 0) return false;
        // int num = x;
        // long int rev = 0;
        // do{
        //     rev = rev * 10 + num % 10;
        // }while((num/=10)>0);
        // if (rev == x) return true;
        // return false;
    }

};