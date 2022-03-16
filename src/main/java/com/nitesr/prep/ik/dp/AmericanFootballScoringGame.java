package com.nitesr.prep.ik.dp;

public class AmericanFootballScoringGame {

    public int numberOfWays(int score) {
        if(score <= 6)
            return baseCase(score);

        int[] now = new int[score+1];
        for(int i=0; i <= score; i++) {
            now[i] = i <= 6 ? baseCase(i) : now[i-6] + now[i-2] + now[i-3];
        }
        return now[score];
    }

    int baseCase(int score) {
        if(score == 0) return 1;
        if(score == 1) return 0;
        if(score == 2) return 1;
        if(score == 3) return 1;
        if(score == 4) return 1;
        if(score == 5) return 2;
        if(score == 6) return 3;
        return 0;
    }

    public static void main(String[] args) {
        System.out.println("0 == "+ new AmericanFootballScoringGame().numberOfWays(1));
        System.out.println("6 == "+ new AmericanFootballScoringGame().numberOfWays(8));
    }
}
