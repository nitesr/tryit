package com.nitesr.prep.ik.dp;

import java.util.ArrayList;

/**
 * Given the prices for rod pieces of every size between 1 inch and n inches,
 *   find the maximum total profit that can be made by cutting an n inches long rod inch into pieces.
 *
 * e.g. [1, 5, 8, 9]  the answer is $10 by cutting the 4in rod in 2in each.
 */
public class CutTheRodToMaximizeProfit {

    /**
     * 1 -> $1
     * 2 -> $2 or $5 => $5
     * 3 -> $3 or $6 or $8 => $8
     * 4 -> $4 or $10 or $9
     *
     * Subproblem:
     * i -> 1 to n;   maxProfit(i) -> maximum profit you can get for i inches long rod
     *
     * Recurrence:
     *  maxProfit(i) = max of (profit(i), maxProfit(i-1) + maxProfit(1), maxProfit(i-2) + maxProfit(2), ...); i -> 1 to n
     *
     * Base case:
     *  maxProfit(1) = profit[1] * n
     *
     * Orignal case: maxProfit(n)
     *
     * Time complexity: O(pow(n,2))
     * Space Complexity: O(n)
     */

    static Integer get_maximum_profit(int[] price) {
        int maxProfit = 0;

        int n = price.length;
        int[] memo = new int[n+1];

        for(int i=1; i <= n; i++) {
            int iMaxProfit = price[i-1];
            for(int j=1; j < i; j++) {
                iMaxProfit = Math.max(memo[j] + memo[i-j], iMaxProfit);
            }
            memo[i] = iMaxProfit;
            maxProfit = Math.max(iMaxProfit, maxProfit);
        }
        return maxProfit;
    }

    public static void main(String[] args) {
        System.out.println("10 == "+get_maximum_profit(new int[]{1, 5, 8, 9}));
        System.out.println("4 == "+get_maximum_profit(new int[]{1, 1, 1, 1}));
        System.out.println("8 == "+get_maximum_profit(new int[]{1, 2, 4, 8}));
    }


}
