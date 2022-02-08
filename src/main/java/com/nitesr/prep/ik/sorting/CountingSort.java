package com.nitesr.prep.ik.sorting;

import com.nitesr.prep.utils.PrintArray;

import java.util.Arrays;

import static com.nitesr.prep.utils.PrintArray.printIntArray;

public class CountingSort {

    private int[] sort(int[] array) {
        if(array.length == 0)
            return array;

        int[] workingArray = Arrays.copyOf(array, array.length);

        int min = workingArray[0];
        int max = workingArray[0];
        for(int i=1; i < workingArray.length; i++) {
            min = Math.min(workingArray[i], min);
            max = Math.max(workingArray[i], max);
        }

        int size = max+1-min;
        int[] countingArray = new int[size];

        for(int i=0; i < workingArray.length; i++) {
            countingArray[workingArray[i]-min]++;
        }


        int i=0;
        for(int k=0; i < workingArray.length && k < countingArray.length; k++) {
            Arrays.fill(workingArray, i, i+countingArray[k], k+min);
            i = i+countingArray[k];
        }

        return workingArray;
    }

    public static void main(String[] args) {
        CountingSort countingSort = new CountingSort();

        int[] array1 = new int[]{10, 30, 5, 23, 60, 2, 45, 90};
        int[] sortedArray1 = countingSort.sort(array1);
        System.out.println(PrintArray.printIntArray(array1)+".sort = "+ PrintArray.printIntArray(sortedArray1));

        int[] array2 = new int[]{};
        int[] sortedArray2 = countingSort.sort(array2);
        System.out.println(PrintArray.printIntArray(array2)+".sort = "+ PrintArray.printIntArray(sortedArray2));

        int[] array3 = new int[]{10};
        int[] sortedArray3 = countingSort.sort(array3);
        System.out.println(PrintArray.printIntArray(array3)+".sort = "+ PrintArray.printIntArray(sortedArray3));

        int[] array4 = new int[]{10, 30};
        int[] sortedArray4 = countingSort.sort(array4);
        System.out.println(PrintArray.printIntArray(array4)+".sort = "+ PrintArray.printIntArray(sortedArray4));

        int[] array5 = new int[]{10, 5, 30};
        int[] sortedArray5 = countingSort.sort(array5);
        System.out.println(PrintArray.printIntArray(array5)+".sort = "+ PrintArray.printIntArray(sortedArray5));

        int[] array6 = new int[]{10, 5, 30, 2, 10, 30, 6, 5};
        int[] sortedArray6 = countingSort.sort(array6);
        System.out.println(PrintArray.printIntArray(array6)+".sort = "+ PrintArray.printIntArray(sortedArray6));

        int[] array7 = new int[]{2, 2, 2, 2, 2, 2, 2, 2, 1, 9};
        int[] sortedArray7 = countingSort.sort(array7);
        System.out.println(PrintArray.printIntArray(array7)+".sort = "+ PrintArray.printIntArray(sortedArray7));
    }
}
