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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
        ListNode newList = new ListNode();
        ListNode alias = newList;

        while (list1 != null && list2 != null) {
            int l1val = list1 != null ? list1.val : -101;
            int l2val = list2 != null ? list2.val : -101;

            if (l1val == -101 && l2val == -101) {

                break;
            }
            if (l1val <= l2val) {
                newList.next = list1;
                list1 = list1.next;  
            } else  {
                newList.next = list2;
                list2 = list2.next;
            }

            newList = newList.next;
        }

        if (list1 != null) {
            newList.next = list1;
        } else if (list2 != null) {
            newList.next = list2;
        }

        return alias.next;
    }
}