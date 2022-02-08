package com.nitesr.prep.mit.dp;

public class LongestIncreasingSubsequence {
    Integer[] memo = new Integer[0];

    public int lis(String S) {
        if(S == null) {
            return 0;
        }

        memo = new Integer[S.length()+1];

        int maxLen = 0;

        //Topological order (T in SRTBOT):
        //  decreasing i
        //Original problem (O in SRTBOT):
        //  find max LIS for all the subsequences S[i:] where i -> |S| ... 0
        //Time Analysis (T in SRTBOT):
        //  T(relation) * sum(no. of sub-problems) + T(additional work on original problem)
        //   =  |S|*C * |S| + |S| = O(pow(n, 2) + pow(n)) = O(pow(n, 2))
        for(int i = S.length(); i >=0; i--) {
            maxLen = Math.max(maxLen, lis(S, i));
        }

        return maxLen;
    }

    //Sub-problem (S in SRTBOT):
    //   find LIS for subsequence S[i:] which starts with S[i]
    //   Note: we are adding a constraint (LIS(S[i:]) includes S[i])
    int lis(String S, int i) {

        if(memo[i] != null) {
            return memo[i];
        }

        //Base case (B in SRTBOT):
        //  LIS of empty subsequence is 0 i.e LIS(S[|S|:]) = 0
        if(i == S.length()) {
            return memo[i] = 0;
        }

        int maxLen = 0;
        //Recurrence relation (R in SRTBOT):
        //  Brute force to find max LIS of all subsequences after S[i] i.e. S[j:] where j -> i+1 .. |S|
        for(int j = i+1; j < S.length(); j++) {
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
        //Topological order (T in SRTBOT)  is decreasing i
        for(int i = S.length(); i>= 0; i--) {
            if(memo[i] != null) {
                continue;
            }

            //Base case (B in SRTBOT):
            if(i == S.length()) {
                memo[i] = 0;
                continue;
            }

            int max = 0;
            //Relation (R in SRTBOT):
            //  Brute force to find max LIS of all subsequences starting after i
            for(int j=i+1; j < S.length(); j++) {
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
        System.out.println("\"" + ip1 + "\"" + ".lis() = " +
                "empty".length() + " == " +
                new LongestIncreasingSubsequence().lis(ip1) + " == " +
                new LongestIncreasingSubsequence().lisBottomUp(ip1));

        String ip2 = "carbohydrate";
        System.out.println("\"" + ip2 + "\"" + ".lis() = " +
                "abort".length() + " == " +
                new LongestIncreasingSubsequence().lis(ip2) + " == " +
                new LongestIncreasingSubsequence().lisBottomUp(ip2));

        String ip3 = "";
        System.out.println("\"" + ip3 + "\"" + ".lis() = " +
                "".length() + " == " +
                new LongestIncreasingSubsequence().lis(ip3) + " == " +
                new LongestIncreasingSubsequence().lisBottomUp(ip3));

        String ip4 = "aaa";
        System.out.println("\"" + ip4 + "\"" + ".lis() = " +
                ip4.length() + " == " +
                new LongestIncreasingSubsequence().lis(ip4) + " == " +
                new LongestIncreasingSubsequence().lisBottomUp(ip4));

        String ip5 = "abc";
        System.out.println("\"" + ip5 + "\"" + ".lis() = " +
                ip5.length() + " == " +
                new LongestIncreasingSubsequence().lis(ip5) + " == " +
                new LongestIncreasingSubsequence().lisBottomUp(ip5));

        String ip6 = "cba";
        System.out.println("\"" + ip6 + "\"" + ".lis() = " +
                "a".length() + " == " +
                new LongestIncreasingSubsequence().lis(ip6) + " == " +
                new LongestIncreasingSubsequence().lisBottomUp(ip6));
    }
}
