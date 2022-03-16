package com.nitesr.prep.ik.presort;

import java.util.ArrayList;

public class MergeKSortedLists {
    static class LinkedListNode {
        int value;
        LinkedListNode next;

        LinkedListNode(int value) {
            this.value = value;
            this.next = null;
        }

        LinkedListNode(int[] values) {
            LinkedListNode head = new LinkedListNode(-1);
            LinkedListNode tail = head;
            for (int i = 0; i < values.length; i++) {
                tail.next = new LinkedListNode(values[i]);
                tail = tail.next;
            }
            this.value = head.next.value;
            this.next = head.next.next;
        }

        @Override
        public boolean equals(Object obj) {
            LinkedListNode theirs = (LinkedListNode) obj;
            LinkedListNode ours = this;

            for (; theirs != null && ours != null && theirs.value == ours.value
                    ; theirs = theirs.next, ours = ours.next);

            return theirs == null && ours == null;
        }
    }

    static LinkedListNode merge_k_lists(LinkedListNode[] lists) {
        if (lists == null || lists.length == 0)
            return null;

        return merge(lists, 0, lists.length - 1);
    }

    static LinkedListNode merge(LinkedListNode[] lists, int s, int e) {

        if (s > e) {
            return null;
        }

        if (s == e) {
            return lists[s];
        }

        int m = (s + e) / 2;
        LinkedListNode l = merge(lists, s, m);
        LinkedListNode r = merge(lists, m + 1, e);
        return merge(l, r);
    }

    static LinkedListNode merge(LinkedListNode l, LinkedListNode o) {
        if (l == null && o == null) {
            return null;
        }

        if (o == null) {
            return l;
        }

        if (l == null) {
            return o;
        }

        LinkedListNode mTail = new LinkedListNode(-1);
        LinkedListNode mHead = mTail;

        while (l != null && o != null) {
            if (l.value < o.value) {
                mTail.next = l;
                l = l.next;
            } else {
                mTail.next = o;
                o = o.next;
            }

            mTail = mTail.next;
            mTail.next = null;
        }

        while (l != null) {
            mTail.next = l;
            l = l.next;
            mTail = mTail.next;
            mTail.next = null;
        }

        while (o != null) {
            mTail.next = o;
            o = o.next;
            mTail = mTail.next;
            mTail.next = null;
        }

        return mHead.next;
    }

    public static void main(String[] args) {
        LinkedListNode merged = merge_k_lists(new LinkedListNode[]{
                new LinkedListNode(new int[]{10, 20, 30}),
                new LinkedListNode(new int[]{5, 15, 25}),
                new LinkedListNode(new int[]{1, 9, 41})
        });
        System.out.println("true == " +
                new LinkedListNode(new int[]{1, 5, 9, 10, 15, 20, 25, 30, 41}).equals(merged));


    }
}


