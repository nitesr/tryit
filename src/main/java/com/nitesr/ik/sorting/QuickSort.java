package com.nitesr.ik.sorting;

import java.util.Arrays;
import java.util.Random;

import static com.nitesr.ik.utils.PrintArray.printIntArray;

/**
 * Created by nitesh on 1/24/22.
 */
public class QuickSort {

    private int[] sort(int[] array) {
        int[] workingArray = Arrays.copyOf(array, array.length);
        quickSort(workingArray, 0, workingArray.length - 1);
        return workingArray;
    }

    private void quickSort(int[] array, int s, int e) {
        if (s >= e)
            return;

        int pvt = partition(array, s, e);

        quickSort(array, s, pvt - 1);
        quickSort(array, pvt + 1, e);

    }

    private int partition(int[] array, int s, int e) {
        int p = new Random().ints(s, e + 1).findFirst().getAsInt();
        swap(array, s, p);

        int smaller = s + 1;
        int bigger = e;

        while (smaller < bigger) {
            if (array[smaller] < array[s]) {
                smaller++;
            } else if (array[bigger] >= array[s]) {
                bigger--;
            } else {
                swap(array, smaller, bigger);
                smaller++;
                bigger--;
            }
        }
        swap(array, s, smaller - 1);
        return smaller - 1;
    }

    private void swap(int[] array, int p, int op) {
        int temp = array[p];
        array[p] = array[op];
        array[op] = temp;
    }

    public static void main(String[] args) {
        QuickSort quickSort = new QuickSort();

        int[] array1 = new int[]{10, 30, 5, 23, 60, 2, 45, 90};
        int[] sortedArray1 = quickSort.sort(array1);
        System.out.println(printIntArray(array1) + ".sort = " + printIntArray(sortedArray1));

        int[] array2 = new int[]{};
        int[] sortedArray2 = quickSort.sort(array2);
        System.out.println(printIntArray(array2) + ".sort = " + printIntArray(sortedArray2));

        int[] array3 = new int[]{10};
        int[] sortedArray3 = quickSort.sort(array3);
        System.out.println(printIntArray(array3) + ".sort = " + printIntArray(sortedArray3));

        int[] array4 = new int[]{10, 30};
        int[] sortedArray4 = quickSort.sort(array4);
        System.out.println(printIntArray(array4) + ".sort = " + printIntArray(sortedArray4));

        int[] array5 = new int[]{10, 5, 30};
        int[] sortedArray5 = quickSort.sort(array5);
        System.out.println(printIntArray(array5) + ".sort = " + printIntArray(sortedArray5));

        int[] array6 = new int[]{2, 30, 5, 23, 60, 2, 5, 90};
        int[] sortedArray6 = quickSort.sort(array6);
        System.out.println(printIntArray(array6) + ".sort = " + printIntArray(sortedArray6));

        int[] array7 = new int[]{1, 2, 3, 4, 5, 6, 7, 8};
        int[] sortedArray7 = quickSort.sort(array7);
        System.out.println(printIntArray(array7) + ".sort = " + printIntArray(sortedArray7));

        int[] array8 = new int[]{10, 10};
        int[] sortedArray8 = quickSort.sort(array8);
        System.out.println(printIntArray(array8) + ".sort = " + printIntArray(sortedArray8));
    }
}
