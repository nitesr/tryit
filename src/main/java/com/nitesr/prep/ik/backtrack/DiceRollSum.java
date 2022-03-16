package com.nitesr.prep.ik.backtrack;

import java.util.ArrayList;
import java.util.List;

public class DiceRollSum {

    public List<List<Integer>> solve(int numOfDices, int[] diceValues, int targetSum) {
        List<List<Integer>> coll = new ArrayList<>();
        helper(numOfDices, diceValues, targetSum, new ArrayList<>(numOfDices), 0, coll);
        return coll;
    }

    void helper(int numOfDices, int[] diceValues, int targetSum, List<Integer> soFar, int runningSum, List<List<Integer>> dices) {
        if(runningSum > targetSum) {
            return;
        }

        if(numOfDices == 0) {
            if(runningSum == targetSum) {
                dices.add(new ArrayList<>(soFar));
            }
            return;
        }

        for(int i=0; i < diceValues.length; i++) {
            soFar.add(diceValues[i]);
            helper(numOfDices-1, diceValues, targetSum, soFar, runningSum + diceValues[i], dices);
            soFar.remove(soFar.size()-1);
        }
    }

    public static void main(String[] args) {
        List<List<Integer>> coll1 = new DiceRollSum().solve(2, new int[]{1, 2}, 3);
        for(List<Integer> option : coll1) {
            System.out.print(option+", ");
        }
        System.out.println();
    }
}
