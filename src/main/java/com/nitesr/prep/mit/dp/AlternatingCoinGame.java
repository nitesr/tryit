package com.nitesr.prep.mit.dp;

import static com.nitesr.prep.mit.dp.AlternatingCoinGame.PLAYER.me;
import static com.nitesr.prep.mit.dp.AlternatingCoinGame.PLAYER.you;
import static com.nitesr.prep.utils.PrintArray.printIntArray;

/**
 * Problem :
 *   Given a sequence of coins,  two players (me & you) will alternatively pick
 *   a coin from edges (first or last) with 'me' going first. Goal of the game
 *   is to score maximum. What is the max score 'me' gets ?
 *
 *   e.g 5, 25, 100, 30; 'me' scores maximum of 105
 */
public class AlternatingCoinGame {
    static enum PLAYER {
        me(0), you(1);

        final int v;
        PLAYER(int v) {
            this.v = v;
        }

        PLAYER inverse() {
            return this.v == me.v ? you : me;
        }
    };

    Integer memo[][][] = new Integer[0][0][2];

    /**
     *  SubProblem (S in "S"RTBOT): G(i, j, p) is the maximum score
     *      I get on V[i:j] coins when player p goes first
     *
     *      G(i, j, me) - max score I get when I go first
     *      G(i, j, you) - max score I get when you go first
     */
    private int maximizeMyScore(int[] v, int i, int j, PLAYER p) {
        if (memo[i][j][p.v] != null)
            return memo[i][j][p.v];

        // Base case (B in SRT"B"OT): only one coin is left
        //    G(i,i,me) = v[i]; G(i, i, you) = 0
        if (i == j) {
            return memo[i][j][p.v] = p == me ? v[i] : 0;
        }

        //Relation (R in SRTBOT):
        //  on my turn, maximize my score by brute forcing
        //      available options (i.e. trying both edges)
        // on other player turn, they minimize my score by brute forcing
        //      available options (i.e. trying both edges)
        // G(i, j, me) = max(V[i]+G(i+1, j, you), V[j]+G(i, j-1, you))
        // G(i, j, you) = min(0+G(i+1, j, me), 0+G(i, j-1, me))

        //Topological Order (T in SR"T"BOT):
        //  compute from increasing j-i
        if (p == me) {
            memo[i][j][p.v] = Math.max(
                    v[i] + maximizeMyScore(v, i + 1, j, you),
                    v[j] + maximizeMyScore(v, i, j - 1, you)
            );
        } else {
            memo[i][j][p.v] = Math.min(
                    maximizeMyScore(v, i + 1, j, me),
                    maximizeMyScore(v, i, j - 1, me)
            );
        }

        return memo[i][j][p.v];
    }

    public int maximizeMyScore(int[] v) {
        if (v == null || v.length == 0)
            return 0;

        memo = new Integer[v.length + 1][v.length + 1][2];

        //Original case (O in SRTB"O"T):
        //  maximum score I ('me') get on all the coins
        //      G(0, n, me)
        return maximizeMyScore(v, 0, v.length - 1, me);

        //Time Analysis (T in SRTBO"T"):
        //  non-recursive work * num. of sub-problems
        //  =  C * for all i,j combinations
        //  =  C * T(i.j)
        //  =  O(pow(n, 2))
    }

    public int maximizeMyScoreBottomUp(int[] v) {
        if (v == null || v.length == 0)
            return 0;

        memo = new Integer[v.length][v.length][1];

        //  5 10 5 25
        // j-i+1 (player) -> 1 (you), 2 (me), 3 (you), 4 (me)
        //     | 5 | 10 | 5  | 25
        //
        //  i  j
        //    | 0  | 1  | 2  | 3
        //  0 | 0  |    |    |
        //  1 | 10 | 0  |    |
        //  2 | 10 | 10 | 0  |
        //  3 | 35 | 10 | 25 | 0
        // max-score = [3,0] = 35

        for(int i=0; i < v.length; i++) {

            //for even number coins, you end up picking last
            PLAYER player = v.length%2 == 0 ? you : me;

            //coins of length (=j-i+1) -> 1, 2, 3, .. v.length
            for(int j=i; j >= 0; j--) {
                if(i == j) {
                    //last coin value for the length (j-i+1)
                    memo[i][j][0] = player == me ? v[i] : 0;
                }else {
                    if(player == me) {
                        memo[i][j][0] = Math.max(v[j]+memo[i][j+1][0], v[i]+memo[i-1][j][0]);
                    }else {
                        memo[i][j][0] = Math.min(memo[i][j+1][0], memo[i-1][j][0]);
                    }
                }
                player = player.inverse();
            }
        }

        return memo[v.length-1][0][0];
    }

    public static void main(String[] args) {
        int[] coins = {5, 25, 100, 30};
        System.out.println(printIntArray(coins) + ".maximizeMyScore() == " +
                " 105 == " +
                new AlternatingCoinGame().maximizeMyScore(coins) + " == " +
                new AlternatingCoinGame().maximizeMyScoreBottomUp(coins)
        );

        int[] coins1 = {100, 30};
        System.out.println(printIntArray(coins1) + ".maximizeMyScore() == " +
                " 100 == " +
                new AlternatingCoinGame().maximizeMyScore(coins1) + " == " +
                new AlternatingCoinGame().maximizeMyScoreBottomUp(coins1)
        );

        int[] coins2 = {100};
        System.out.println(printIntArray(coins2) + ".maximizeMyScore() == " +
                " 100 == " +
                new AlternatingCoinGame().maximizeMyScore(coins2) + " == " +
                new AlternatingCoinGame().maximizeMyScoreBottomUp(coins2)
        );

        int[] coins3 = {};
        System.out.println(printIntArray(coins3) + ".maximizeMyScore() == " +
                " 0 == " +
                new AlternatingCoinGame().maximizeMyScore(coins3) + " == " +
                new AlternatingCoinGame().maximizeMyScoreBottomUp(coins3)
        );

        int[] coins4 = {5, 5, 5};
        System.out.println(printIntArray(coins4) + ".maximizeMyScore() == " +
                " 10 == " +
                new AlternatingCoinGame().maximizeMyScore(coins4) + " == " +
                new AlternatingCoinGame().maximizeMyScoreBottomUp(coins4)
        );

        int[] coins5 = {5, 25, -100, 30};
        System.out.println(printIntArray(coins5) + ".maximizeMyScore() == " +
                " 55 == " +
                new AlternatingCoinGame().maximizeMyScore(coins5) + " == " +
                new AlternatingCoinGame().maximizeMyScoreBottomUp(coins5)
        );

        int[] coins6 = {5, 10, 5, 25};
        System.out.println(printIntArray(coins6) + ".maximizeMyScore() == " +
                " 40 == " +
                new AlternatingCoinGame().maximizeMyScore(coins6) + " == " +
                new AlternatingCoinGame().maximizeMyScoreBottomUp(coins6)
        );
    }
}
