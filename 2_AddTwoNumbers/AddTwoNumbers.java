 
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int rem = 0;
        ListNode res = null;
        ListNode cur = null;
        while(l1 != null || l2 != null){
            int v1 = 0;
            int v2 = 0;
            if(l1 != null) v1 = l1.val;
            if(l2 != null) v2 = l2.val;
            int sum = v1+v2+rem;
            rem = sum / 10;
            if(res == null){
                res = new ListNode(sum%10);
                cur = res;
            } else {
                cur.next = new ListNode(sum%10);
                cur = cur.next;
            }
            if(l1 != null) l1 = l1.next;
            if(l2 != null) l2 = l2.next;
        }
        if(rem > 0){
            cur.next = new ListNode(rem);
        }
        return res;
    }
}
