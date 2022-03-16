package com.nitesr.prep.ik.combinatrics;

import java.util.*;

public class PermutateIntArrayOfDuplicates {

    static ArrayList<List<Integer>> get_permutations(List<Integer> arr) {
        ArrayList<List<Integer>> perms = new ArrayList<>();

        Collections.sort(arr);
        if(arr != null && arr.size() > 0) helper(arr, 0, perms);
        //if(arr != null && arr.size() > 0) helperWithSet(arr, 0, new ArrayList<>(), perms);

        return perms;
    }


    static void helper(List<Integer> arr, int idx, ArrayList<List<Integer>> perms) {

        if(idx == arr.size()) {
            perms.add(new ArrayList(arr));
            return;
        }

        for(int i=idx; i < arr.size(); i++) {
            if(i > idx && arr.get(i) == arr.get(i-1)) {
                continue;
            }

            Collections.swap(arr, idx, i);
            helper(arr, idx+1, perms);
            Collections.swap(arr, i, idx);
        }
    }

    static void helperWithSet(List<Integer> arr, int idx, List<Integer> soFar, ArrayList<List<Integer>> perms) {

        if(idx == arr.size()) {
            perms.add(new ArrayList(soFar));
            return;
        }

        HashSet<Integer> set = new HashSet<>();
        for(int i=idx; i < arr.size(); i++) {
            if(set.contains(arr.get(i))) {
                continue;
            }
            set.add(arr.get(i));

            Collections.swap(arr, idx, i);
            soFar.add(arr.get(idx));
            helperWithSet(arr, idx+1, soFar, perms);
            soFar.remove(soFar.size()-1);
            Collections.swap(arr, i, idx);
        }
    }

    public static void main(String[] args) {
        /*
        System.out.println("210 == "
                + get_permutations(Arrays.asList(3, 3, 8, 8, 9, 9, 9)).size());

        System.out.println("4 == "
                + get_permutations(Arrays.asList(1, 1, 1, 2)).size());

        System.out.println("4 == "
                + get_permutations(Arrays.asList(1, 2, 2, 2)).size());

        System.out.println("6 == "
                + get_permutations(Arrays.asList(1, 1, 2, 2)).size());

        System.out.println("12 == "
                + get_permutations(Arrays.asList(1, 2, 2, 3)).size());
*/
        System.out.println("30 == "
                + get_permutations(Arrays.asList(1, 1, 2, 2, 3)).size());
        print(get_permutations(Arrays.asList(1, 1, 2, 2, 3)));
/*
        System.out.println("60 == "
                + get_permutations(Arrays.asList(1, 1, 2, 2, 2, 3)).size());*/
    }

    static void print(ArrayList<List<Integer>> list) {
        for(List<Integer> l : list)
            System.out.println(l);
    }
}
