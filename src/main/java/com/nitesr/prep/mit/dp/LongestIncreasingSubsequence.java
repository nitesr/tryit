package com.nitesr.prep.mit.dp;

public class LongestIncreasingSubsequence {
    Integer[] memo = new Integer[0];

    public int lis(String S) {
        if(S == null) {
            return 0;
        }

        memo = new Integer[S.length()+1];

        int maxLen = 0;
        //Topological order decreasing i; T in SRTBOT
        //Original problem; O in SRTBOT
        for(int i = S.length(); i >=0; i--) {
            maxLen = Math.max(maxLen, lis(S, i));
        }

        return maxLen;
    }

    //Sub-problem; S in SRTBOT
    int lis(String S, int i) {

        if(memo[i] != null) {
            return memo[i];
        }

        //Base case; B in SRTBOT
        if(i == S.length()) {
            return memo[i] = 0;
        }

        int maxLen = 0;
        //Brute force all possibilities
        for(int j = i+1; j < S.length(); j++) {
            //Recurrence relation; R in SRTBOT
            if(S.charAt(j) >= S.charAt(i)) {
                maxLen = Math.max(maxLen, lis(S, j));
            }
        }

        return memo[i] = 1 + maxLen;
    }

    public int lisBottomUp(String S) {
        if(S == null) {
            return 0;
        }

        memo = new Integer[S.length()+1];
        //Topological order decreasing i; T in SRTBOT
        for(int i = S.length(); i>= 0; i--) {
            if(memo[i] != null) {
                continue;
            }

            //Base case; B in SRTBOT
            if(i == S.length()) {
                memo[i] = 0;
                continue;
            }

            int max = 0;
            //Brute force all possibilities
            for(int j=i+1; j < S.length(); j++) {
                //Relation; R in SRTBOT
                if(S.charAt(j) >= S.charAt(i)) {
                    max = Math.max(max, memo[j]);
                }
            }
            memo[i] = 1 + max;
        }

        int maxLen = 0;
        for(int i = S.length(); i >=0; i--) {
            maxLen = Math.max(maxLen, memo[i]);
        }

        return maxLen;
    }

    public static void main(String[] args) {
        String ip1 = "empathy";
        System.out.println(ip1 + ".lis() = " +
                "empty".length() + " == " +
                new LongestIncreasingSubsequence().lis(ip1) + " == " +
                new LongestIncreasingSubsequence().lisBottomUp(ip1));

        String ip2 = "carbohydrate";
        System.out.println(ip2 + ".lis() = " +
                "abort".length() + " == " +
                new LongestIncreasingSubsequence().lis(ip2) + " == " +
                new LongestIncreasingSubsequence().lisBottomUp(ip2));

        String ip3 = "";
        System.out.println(ip3 + ".lis() = " +
                "".length() + " == " +
                new LongestIncreasingSubsequence().lis(ip3) + " == " +
                new LongestIncreasingSubsequence().lisBottomUp(ip3));
    }
}
