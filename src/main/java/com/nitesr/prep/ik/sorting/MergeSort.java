package com.nitesr.prep.ik.sorting;

import java.util.Arrays;

import static com.nitesr.prep.utils.PrintArray.printIntArray;

/**
 * Created by nitesh on 1/22/22.
 */
public class MergeSort {
    private int[] sort(int[] array) {
        int[] workingArray = Arrays.copyOf(array, array.length);
        sortInternal(workingArray, 0, workingArray.length-1);
        return workingArray;
    }

    private void sortInternal(int[] array, int s1, int e1) {
        int m = (s1+e1)/2;
        int n = e1-s1+1;

        if(n <= 1) {
            return;
        }

        sortInternal(array, s1, m);
        sortInternal(array, m + 1, e1);
        int[] mergedArray = merge(array, s1, m, m+1, e1);


        for(int i=0; i < n; i++) {
            array[i+s1] = mergedArray[i];
        }
    }

    private int[] merge(int[] array, int s1, int e1, int s2, int e2) {
        int n = e1-s1+1+e2-s2+1;

        int[] mergedArray = new int[n];
        int p1 = s1;
        int p2 = s2;

        for(int k=0; k < n;) {
            for(; p2 <= e2 && p1 <= e1 && array[p1] < array[p2]; p1++) {
                mergedArray[k++] = array[p1];
            }

            for(; p1 <= e1 && p2 <= e2 && array[p2] < array[p1]; p2++) {
                mergedArray[k++] = array[p2];
            }

            if(p1 > e1) {
                for(; p2 <= e2; p2++) {
                    mergedArray[k++] = array[p2];
                }
            }

            if(p2 > e2) {
                for(; p1 <= e1; p1++) {
                    mergedArray[k++] = array[p1];
                }
            }
        }

        return mergedArray;
    }

    public static void main(String[] args) {
        MergeSort mergeSort = new MergeSort();

        int[] array1 = new int[]{10, 30, 5, 23, 60, 2, 45, 90};
        int[] sortedArray1 = mergeSort.sort(array1);
        System.out.println(printIntArray(array1)+".sort = "+printIntArray(sortedArray1));

        int[] array2 = new int[]{};
        int[] sortedArray2 = mergeSort.sort(array2);
        System.out.println(printIntArray(array2)+".sort = "+printIntArray(sortedArray2));

        int[] array3 = new int[]{10};
        int[] sortedArray3 = mergeSort.sort(array3);
        System.out.println(printIntArray(array3)+".sort = "+printIntArray(sortedArray3));

        int[] array4 = new int[]{10, 30};
        int[] sortedArray4 = mergeSort.sort(array4);
        System.out.println(printIntArray(array4)+".sort = "+printIntArray(sortedArray4));

        int[] array5 = new int[]{10, 5, 30};
        int[] sortedArray5 = mergeSort.sort(array5);
        System.out.println(printIntArray(array5)+".sort = "+printIntArray(sortedArray5));
    }
}
