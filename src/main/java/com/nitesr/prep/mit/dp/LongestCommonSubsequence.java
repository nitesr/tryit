package com.nitesr.prep.mit.dp;

import com.nitesr.prep.utils.PrintArray;

public class LongestCommonSubsequence {

    //Sub-problem (S in SRTBOT):
    //  what is LCS for subsequences S1[i:] & S2[j:] where 0 <= i <= |S1| & 0 <= j <= |S2| ?
    int lcs(String s1, int i, String s2, int j) {
        if (memo[i][j] != null) {
            return memo[i][j];
        }

        //Base case (B in SRTBOT):
        //  S1[i:] or S2[j:] is empty then LCS is 0
        if (i >= s1.length() || j >= s2.length()) {
            return memo[i][j] = 0;
        }

        //Recurrence relation (R in SRTBOT):
        //  if S1[i] & S[j] chars match find LCS of subsequences S1[i+1:] & S2[j+1:]
        //    else find max LCS with subsequences S1[i+1:], S2[j:]
        if (s1.charAt(i) == s2.charAt(j)) {
            memo[i][j] = 1 + lcs(s1, i + 1, s2, j + 1);
        } else {
            memo[i][j] = Math.max(lcs(s1, i + 1, s2, j), lcs(s1, i, s2, j + 1));
        }

        return memo[i][j];
    }

    Integer[][] memo = new Integer[0][0];

    public int lcs(String s1, String s2) {
        if (s1 == null || s2 == null)
            return 0;

        memo = new Integer[s1.length() + 1][s2.length() + 1];

        //Original problem (O in SRTBOT):
        //  is on S1[0:] & S2[0:] subsequences which are nothing but given strings.
        // Time Analysis (T in SRTBOT):
        //   is T(relation) * sum(no. of sub-problems) = C * (|S1| * |S2|) = O(pow(n,2))
        return lcs(s1, 0, s2, 0);
    }

    public int lcsBottomUp(String s1, String s2) {
        if (s1 == null || s2 == null)
            return 0;

        Integer[][] memo = new Integer[s1.length() + 1][s2.length() + 1];

        //Topological order; T in SRTBOT
        for (int i = s1.length(); i >= 0; i--) {
            for (int j = s2.length(); j >= 0; j--) {

                //Base case (B in SRTBOT):
                //  S1[i:] or S2[j:] is empty then LCS is 0
                if (i == s1.length() || j == s2.length()) {
                    memo[i][j] = 0;
                    continue;
                }

                //Recurrence relation (R in SRTBOT):
                //  if S1[i] & S[j] chars match find LCS of subsequences S1[i+1:] & S2[j+1:]
                //    else find max LCS with subsequences S1[i+1:], S2[j:]
                if (s1.charAt(i) == s2.charAt(j)) {
                    memo[i][j] = 1 + memo[i + 1][j + 1];
                } else {
                    memo[i][j] = Math.max(memo[i + 1][j], memo[i][j + 1]);
                }
            }
        }

        //Original problem (O in SRTBOT):
        //  is on S1[0:] & S2[0:] subsequences which are nothing but given strings.
        // Time Analysis (T in SRTBOT):
        //   is T(relation) * sum(no. of sub-problems) = C * (|S1| * |S2|) = O(pow(n,2))
        return memo[0][0];
    }

    public static void main(String[] args) {
        String[] ip1 = {"empathy", "empty"};
        System.out.println(PrintArray.printObjectArray(ip1) + ".lcs() = " +
                "empty".length() + " == " +
                new LongestCommonSubsequence().lcs(ip1[0], ip1[1]) + " == " +
                new LongestCommonSubsequence().lcsBottomUp(ip1[0], ip1[1]));

        String[] ip2 = {"empathy", ""};
        System.out.println(PrintArray.printObjectArray(ip2) + ".lcs() = " +
                "".length() + " == " +
                new LongestCommonSubsequence().lcs(ip2[0], ip2[1]) + " == " +
                new LongestCommonSubsequence().lcsBottomUp(ip2[0], ip2[1]));

        String[] ip3 = {"empathy", "empathy"};
        System.out.println(PrintArray.printObjectArray(ip3) + ".lcs() = " +
                "empathy".length() + " == " +
                new LongestCommonSubsequence().lcs(ip3[0], ip3[1]) + " == " +
                new LongestCommonSubsequence().lcsBottomUp(ip3[0], ip3[1]));

        String[] ip4 = {"", ""};
        System.out.println(PrintArray.printObjectArray(ip4) + ".lcs() = " +
                "".length() + " == " +
                new LongestCommonSubsequence().lcs(ip4[0], ip4[1]) + " == " +
                new LongestCommonSubsequence().lcsBottomUp(ip4[0], ip4[1]));

        String[] ip5 = {"company", "brisk"};
        System.out.println(PrintArray.printObjectArray(ip5) + ".lcs() = " +
                "".length() + " == " +
                new LongestCommonSubsequence().lcs(ip5[0], ip5[1]) + " == " +
                new LongestCommonSubsequence().lcsBottomUp(ip5[0], ip5[1]));
    }
}
