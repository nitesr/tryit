package com.nitesr.prep.ik.sorting;

import com.nitesr.prep.utils.PrintArray;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.function.Function;

public class CountingObjectSort<T> {
    T[] array;
    int minBucketNumber;
    int maxBucketNumber;
    Function<T, Integer> getBucketNumber;

    public CountingObjectSort(T[] array, int minBucketNumber, int maxBucketNumber, Function<T, Integer> getBucketNumber) {
        this.array = array;
        this.minBucketNumber = minBucketNumber;
        this.maxBucketNumber = maxBucketNumber;
        this.getBucketNumber = getBucketNumber;

        assert minBucketNumber >= maxBucketNumber;
    }

    public T[] sort() {
        if(array.length == 0)
            return array;

        T[] workingArray = Arrays.copyOf(array, array.length);

        int size = maxBucketNumber+1-minBucketNumber;
        LinkedList<T>[] countingArray = new LinkedList[size];

        for(int i=0; i < workingArray.length; i++) {
            int ci = getBucketNumber.apply(workingArray[i]);
            if(countingArray[ci] == null) {
                countingArray[ci] = new LinkedList<>();
            }
            countingArray[ci].add(workingArray[i]);
        }

        final int[] i = {0};
        for(int k=0; k < countingArray.length; k++) {
            if(countingArray[k] == null) {
                continue;
            }
            countingArray[k].forEach(val -> {workingArray[i[0]] = val; i[0]++; });
        }

        return workingArray;
    }

    public static void main(String[] args) {

        Function<Integer, Integer> intBucketFunction = o -> o;

        Integer[] array1 = new Integer[]{10, 30, 5, 23, 60, 2, 45, 90};
        CountingObjectSort<Integer> countingSort1 = new CountingObjectSort(array1, 0, 100, intBucketFunction);
        Integer[] sortedArray1 = countingSort1.sort();
        System.out.println(PrintArray.printObjectArray(array1)+".sort = "+ PrintArray.printObjectArray(sortedArray1));

        Integer[] array2 = new Integer[]{};
        CountingObjectSort<Integer> countingSort2 = new CountingObjectSort(array2, 0, 100, intBucketFunction);
        Integer[] sortedArray2 = countingSort2.sort();
        System.out.println(PrintArray.printObjectArray(array2)+".sort = "+ PrintArray.printObjectArray(sortedArray2));

        Integer[] array3 = new Integer[]{10};
        CountingObjectSort<Integer> countingSort3 = new CountingObjectSort(array3, 0, 100, intBucketFunction);
        Integer[] sortedArray3 = countingSort3.sort();
        System.out.println(PrintArray.printObjectArray(array3)+".sort = "+ PrintArray.printObjectArray(sortedArray3));

        Integer[] array4 = new Integer[]{10, 30};
        CountingObjectSort<Integer> countingSort4 = new CountingObjectSort(array4, 0, 100, intBucketFunction);
        Integer[] sortedArray4 = countingSort4.sort();
        System.out.println(PrintArray.printObjectArray(array4)+".sort = "+ PrintArray.printObjectArray(sortedArray4));

        Integer[] array5 = new Integer[]{10, 5, 30};
        CountingObjectSort<Integer> countingSort5 = new CountingObjectSort(array5, 0, 100, intBucketFunction);
        Integer[] sortedArray5 = countingSort5.sort();
        System.out.println(PrintArray.printObjectArray(array5)+".sort = "+ PrintArray.printObjectArray(sortedArray5));

        Integer[] array6 = new Integer[]{10, 5, 30, 2, 10, 30, 6, 5};
        CountingObjectSort<Integer> countingSort6 = new CountingObjectSort(array6, 0, 100, intBucketFunction);
        Integer[] sortedArray6 = countingSort6.sort();
        System.out.println(PrintArray.printObjectArray(array6)+".sort = "+ PrintArray.printObjectArray(sortedArray6));

        Integer[] array7 = new Integer[]{2, 2, 2, 2, 2, 2, 2, 2, 1, 9};
        CountingObjectSort<Integer> countingSort7 = new CountingObjectSort(array7, 0, 100, intBucketFunction);
        Integer[] sortedArray7 = countingSort7.sort();
        System.out.println(PrintArray.printObjectArray(array7)+".sort = "+ PrintArray.printObjectArray(sortedArray7));

    }
}
