package com.nitesr.prep.ik.dp;

public class MaximizeProfitOnAorBProductProduction {
    public int calculateMaxProfile(int[][] dayProfits, int n) {
        int[][] maxProfits = new int[2][dayProfits[0].length];

        for(int i=0; i < n; i++) {
            maxProfits[0][i] = Math.max(i < 1 ? 0 : maxProfits[0][i-1], i < 2 ? 0 : maxProfits[1][i-2]) + dayProfits[0][i];
            maxProfits[1][i] = Math.max(i < 1 ? 0 : maxProfits[1][i-1], i < 2 ? 0 : maxProfits[0][i-2]) + dayProfits[1][i];
        }

        return Math.max(maxProfits[0][n-1], maxProfits[1][n-1]);
    }

    public static void main(String[] args) {
        System.out.println("10 == " + new MaximizeProfitOnAorBProductProduction().calculateMaxProfile(new int[][]{new int[]{1, 2, 3, 4}, new int[]{1, 2, 3, 4}}, 4));
        System.out.println("161 == " + new MaximizeProfitOnAorBProductProduction().calculateMaxProfile(new int[][]{new int[]{5, 2, 80, 1}, new int[]{80, 2, 1, 2}}, 4));
    }
}
