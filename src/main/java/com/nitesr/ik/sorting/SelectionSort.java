package com.nitesr.ik.sorting;

import java.util.Arrays;

import static com.nitesr.ik.utils.PrintArray.*;

/**
 * Created by nitesh on 1/22/22.
 */
public class SelectionSort {

    private int[] sort(int[] array) {
        int[] workingArray = Arrays.copyOf(array, array.length);

        for(int i=0; i < workingArray.length; i++) {
            int minPos = i;

            for(int j=i+1; j < workingArray.length; j++) {
                if(workingArray[j] < workingArray[minPos]) {
                    minPos = j;
                }
            }

            int temp = workingArray[i];
            workingArray[i] = workingArray[minPos];
            workingArray[minPos] = temp;
        }

        return workingArray;
    }

    public static void main(String[] args) {
        SelectionSort selectionSort = new SelectionSort();

        int[] array1 = new int[]{10, 30, 5, 2, 60, 23, 45, 90};
        int[] sortedArray1 = selectionSort.sort(array1);
        System.out.println(printIntArray(array1)+".sort = "+printIntArray(sortedArray1));

        int[] array2 = new int[]{};
        int[] sortedArray2 = selectionSort.sort(array2);
        System.out.println(printIntArray(array2)+".sort = "+printIntArray(sortedArray2));

        int[] array3 = new int[]{10};
        int[] sortedArray3 = selectionSort.sort(array3);
        System.out.println(printIntArray(array3)+".sort = "+printIntArray(sortedArray3));
    }

}
