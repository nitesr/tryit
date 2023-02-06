package com.nitesr.prep.leetcode;

/**
 * Created by nitesh on 3/30/20.
 * You are given two non-empty linked lists representing two non-negative integers.
 * The digits are stored in reverse order and each of their nodes contain a single digit.
 * Add the two numbers and return it as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 * Example:
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 * Explanation: 342 + 465 = 807.
 */
public class AddTwoNumbers {

    static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(l1.val+l2.val);
        ListNode i = l1.next;
        ListNode j = l2.next;
        ListNode nextDigit = result;

        while(i != null || j != null) {
            int sum = 0;
            if(nextDigit.val > 9) {
                nextDigit.val = nextDigit.val-10;
                sum++;
            }
            sum = sum + (i != null ? i.val : 0) + (j != null ? j.val : 0);
            nextDigit.next = new ListNode(sum);
            i = i != null ? i.next : null;
            j = j != null ? j.next : null;
            nextDigit = nextDigit.next;
        }

        if(nextDigit.val > 9) {
            nextDigit.val = nextDigit.val-10;
            nextDigit.next = new ListNode(1);
        }

        return result;
    }

    public static void main(String[] args) {
        ListNode l1 = new ListNode(2);
        l1.next = new ListNode(4);
        l1.next.next = new ListNode(3);

        ListNode l2 = new ListNode(5);
        l2.next = new ListNode(6);
        l2.next.next = new ListNode(4);

        new AddTwoNumbers().addTwoNumbers(l1, l2);
    }
}

