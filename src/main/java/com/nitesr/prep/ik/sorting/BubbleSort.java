package com.nitesr.prep.ik.sorting;

import com.nitesr.prep.utils.PrintArray;

import java.util.Arrays;

import static com.nitesr.prep.utils.PrintArray.printIntArray;

/**
 * Created by nitesh on 1/22/22.
 */
public class BubbleSort {

    private int[] sort(int[] array) {
        int[] workingArray = Arrays.copyOf(array, array.length);

        for (int i = 0; i < workingArray.length; i++) {

            for (int j = workingArray.length - 1 - i; j > i; j--) {
                if (workingArray[j] < workingArray[j - 1]) {
                    int temp = workingArray[j - 1];
                    workingArray[j - 1] = workingArray[j];
                    workingArray[j] = temp;
                }
            }

        }

        return workingArray;
    }

    public static void main(String[] args) {
        BubbleSort bubbleSort = new BubbleSort();

        int[] array1 = new int[]{10, 30, 5, 2, 60, 23, 45, 90};
        int[] sortedArray1 = bubbleSort.sort(array1);
        System.out.println(PrintArray.printIntArray(array1) + ".sort = " + PrintArray.printIntArray(sortedArray1));

        int[] array2 = new int[]{};
        int[] sortedArray2 = bubbleSort.sort(array2);
        System.out.println(PrintArray.printIntArray(array2) + ".sort = " + PrintArray.printIntArray(sortedArray2));

        int[] array3 = new int[]{10};
        int[] sortedArray3 = bubbleSort.sort(array3);
        System.out.println(PrintArray.printIntArray(array3) + ".sort = " + PrintArray.printIntArray(sortedArray3));
    }

}
