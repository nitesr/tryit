package com.nitesr.ik.sorting;

import java.util.Arrays;

import static com.nitesr.utils.PrintArray.printIntArray;

/**
 * Created by nitesh on 1/22/22.
 */
public class InsertionSort {

    private int[] sortRecursively(int[] array) {
        int[] workingArray = Arrays.copyOf(array, array.length);
        sortRecursivelyInt(workingArray, workingArray.length - 1);
        return workingArray;
    }

    private void sortRecursivelyInt(int[] array, int lastPos) {
        if (lastPos <= 0)
            return;

        sortRecursivelyInt(array, lastPos - 1);
        int lastPosEle = array[lastPos];
        insert(array, lastPos, lastPosEle);
    }

    private void insert(int[] array, int n, int ele) {
        int i = n - 1;
        for (; i >= 0 && array[i] > ele; i--) {
            array[i + 1] = array[i];
        }
        array[i + 1] = ele;
    }

    private int[] sort(int[] array) {
        int[] workingArray = Arrays.copyOf(array, array.length);
        for (int i = 1; i < workingArray.length; i++) {
            insert(workingArray, i, workingArray[i]);
        }
        return workingArray;
    }

    public static void main(String[] args) {
        InsertionSort insertionSort = new InsertionSort();

        System.out.println("********************** TOP DOWN *************************************");

        int[] array1 = new int[]{10, 30, 5, 2, 60, 23, 45, 90};
        int[] sortedArray1 = insertionSort.sortRecursively(array1);
        System.out.println(printIntArray(array1) + ".sortRecursively = " + printIntArray(sortedArray1));

        int[] array2 = new int[]{};
        int[] sortedArray2 = insertionSort.sortRecursively(array2);
        System.out.println(printIntArray(array2) + ".sortRecursively = " + printIntArray(sortedArray2));

        int[] array3 = new int[]{10};
        int[] sortedArray3 = insertionSort.sortRecursively(array3);
        System.out.println(printIntArray(array3) + ".sortRecursively = " + printIntArray(sortedArray3));

        System.out.println("********************** BOTTOM UP *************************************");

        int[] array4 = new int[]{10, 30, 5, 2, 60, 23, 45, 90};
        int[] sortedArray4 = insertionSort.sort(array4);
        System.out.println(printIntArray(array1) + ".sort = " + printIntArray(sortedArray4));

        int[] array5 = new int[]{};
        int[] sortedArray5 = insertionSort.sort(array5);
        System.out.println(printIntArray(array5) + ".sort = " + printIntArray(sortedArray5));

        int[] array6 = new int[]{10};
        int[] sortedArray6 = insertionSort.sort(array6);
        System.out.println(printIntArray(array6) + ".sort = " + printIntArray(sortedArray6));
    }
}
