package com.nitesr.mit.dp;

import static com.nitesr.utils.PrintArray.printObjectArray;

public class LongestCommonSubsequence {

    //sub-problem (S in SRTBOT)
    int lcs(String s1, int i, String s2, int j) {
        if (memo[i][j] != null) {
            return memo[i][j];
        }

        //base case (B in SRTBOT)
        if (i == s1.length() || j == s2.length()) {
            return memo[i][j] = 0;
        }

        //recurrence relation (R in SRTBOT)
        if (s1.charAt(i) == s2.charAt(j)) {
            memo[i][j] = 1 + lcs(s1, i + 1, s2, j + 1);
        } else {
            memo[i][j] = Math.max(lcs(s1, i + 1, s2, j), lcs(s2, i, s2, j + 1));
        }

        return memo[i][j];
    }

    Integer[][] memo = new Integer[0][0];

    public int lcs(String s1, String s2) {
        if (s1 == null || s2 == null)
            return 0;

        memo = new Integer[s1.length() + 1][s2.length() + 1];

        //original problem (O in SRTBOT)
        return lcs(s1, 0, s2, 0);
    }

    public int lcsBottomUp(String s1, String s2) {
        if (s1 == null || s2 == null)
            return 0;

        Integer[][] memo = new Integer[s1.length() + 1][s2.length() + 1];

        //Topological order; T in SRTBOT
        for (int i = s1.length(); i >= 0; i--) {
            for (int j = s2.length(); j >= 0; j--) {

                //base case; B in SRTBOT
                if (i == s1.length() || j == s2.length()) {
                    memo[i][j] = 0;
                    continue;
                }

                //recurrence relation;  R in SRTBOT
                if (s1.charAt(i) == s2.charAt(j)) {
                    memo[i][j] = 1 + memo[i + 1][j + 1];
                } else {
                    memo[i][j] = Math.max(memo[i + 1][j], memo[i][j + 1]);
                }
            }
        }

        //Original Problem; O in SRTBOT
        return memo[0][0];
    }

    public static void main(String[] args) {
        String[] ip1 = {"empathy", "empty"};
        System.out.println(printObjectArray(ip1) + ".lcs() = " +
                "empty".length() + " == " +
                new LongestCommonSubsequence().lcs(ip1[0], ip1[1]) + " == " +
                new LongestCommonSubsequence().lcsBottomUp(ip1[0], ip1[1]));

        String[] ip2 = {"empathy", ""};
        System.out.println(printObjectArray(ip2) + ".lcs() = " +
                "".length() + " == " +
                new LongestCommonSubsequence().lcs(ip2[0], ip2[1]) + " == " +
                new LongestCommonSubsequence().lcsBottomUp(ip2[0], ip2[1]));

        String[] ip3 = {"empathy", "empathy"};
        System.out.println(printObjectArray(ip3) + ".lcs() = " +
                "empathy".length() + " == " +
                new LongestCommonSubsequence().lcs(ip3[0], ip3[1]) + " == " +
                new LongestCommonSubsequence().lcsBottomUp(ip3[0], ip3[1]));
    }
}
