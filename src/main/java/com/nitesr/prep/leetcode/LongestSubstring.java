package com.nitesr.prep.leetcode;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

/**
 * Created by nitesh on 4/1/20.
 */
public class LongestSubstring {

    public int lengthOfLongestSubstringOptimal(String s) {
        int n = s.length();
        Set<Character> set = new HashSet<>();
        int ans = 0, i = 0, j = 0;
        while (i < n && j < n) {
            // try to extend the range [i, j]
            if (!set.contains(s.charAt(j))){
                set.add(s.charAt(j++));
                ans = Math.max(ans, j - i);
            }
            else {
                set.remove(s.charAt(i++));
            }
        }
        return ans;
    }

    public int lengthOfLongestSubstring(String s) {
        int ml = 0;

        char chars[] = s.toCharArray();
        int startIndex = 0;
        for(int i=0; i< chars.length; i++) {
            int charFoundIndex = -1;
            for(int j=startIndex; j<i; j++) {
                if(chars[j] == chars[i]) {
                    charFoundIndex = j;
                    break;
                }
            }

            if(charFoundIndex > -1) {
                if(ml < (i-startIndex)) {
                    ml = i-startIndex;
                }
                startIndex = charFoundIndex+1;
            }
        }
        if(ml < chars.length - startIndex) {
            ml = chars.length - startIndex;
        }
        return ml;
    }

    public int lengthOfLongestSubstringPass1(String s) {
        int ml = 0;

        char chars[] = s.toCharArray();
        IndexedLinkHashSet workingSet = new IndexedLinkHashSet();
        for(char c : chars) {
            if(!workingSet.contains(c)) {
                workingSet.add(c);
            }else {
                if(ml < workingSet.size()) {
                    ml = workingSet.size();
                }
                workingSet.trim(c);
                workingSet.add(c);
            }
        }
        if(ml < workingSet.size()) {
            ml = workingSet.size();
        }
        return ml;
    }

    static class LinkNode {
        Object value;
        LinkNode next;
        LinkNode prev;
        LinkNode(Object val) {
            this.value = val;
        }

        boolean equals(LinkNode node) {
            return value != null ? node != null && value.equals(node.value) : node.value == null;
        }
    }

    static class IndexedLinkHashSet {
        HashMap map = new HashMap();
        LinkNode head;
        LinkNode tail;

        boolean add(Object o) {
            if(!map.containsKey(o)) {
                LinkNode node = new LinkNode(o);
                map.put(o, node);
                if(head == null) {
                    head = node;
                }

                if(tail != null) {
                    tail.next = node;
                    node.prev = tail;
                }
                tail = node;
                return true;
            }
            return false;
        }

        boolean contains(Object o) {
            return map.containsKey(o);
        }

        int size() {
            return map.size();
        }

        void trim(Object o) {
            LinkNode node = (LinkNode)map.get(o);
            if(node != null) {
                for(LinkNode curNode=node; curNode != null; curNode = curNode.prev) {
                    map.remove(curNode.value);
                }

                if(node.equals(tail)) {
                    tail = null;
                }

                head = node.next;
                if(head != null) {
                    head.prev = null;
                }
            }
        }
    }

    public static void main(String[] args){
        System.out.println("pwwkewp"+":"+new LongestSubstring().lengthOfLongestSubstringOptimal("pwwkewp"));
        System.out.println("pwwkew"+":"+new LongestSubstring().lengthOfLongestSubstringOptimal("pwwkew"));
        System.out.println("abcdef"+":"+new LongestSubstring().lengthOfLongestSubstringOptimal("abcdef"));
        System.out.println(""+":"+new LongestSubstring().lengthOfLongestSubstringOptimal(""));
        System.out.println("abcabcbb"+":"+new LongestSubstring().lengthOfLongestSubstringOptimal("abcabcbb"));
        System.out.println("a"+":"+new LongestSubstring().lengthOfLongestSubstringOptimal("a"));
        System.out.println("bbbb"+":"+new LongestSubstring().lengthOfLongestSubstringOptimal("bbbb"));
    }
}

