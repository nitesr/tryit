package com.nitesr.ik.sorting;

import com.nitesr.utils.Pair;

import java.util.Arrays;
import java.util.function.Function;

import static com.nitesr.utils.PrintArray.printObjectArray;

public class RadixSort<T> {
    final T[] array;
    final int minBucketNumber;
    final int maxBucketNumber;
    final Function<T, Integer> lengthify;
    final Function<Pair<T, Integer>, Integer> bucketify;

    public RadixSort(T[] array, int minBucketNumber, int maxBucketNumber, Function<T, Integer> lengthify, Function<Pair<T, Integer>, Integer> bucketify) {
        this.array = array;
        this.minBucketNumber = minBucketNumber;
        this.maxBucketNumber = maxBucketNumber;
        this.lengthify = lengthify;
        this.bucketify = bucketify;
    }

    private T[] sort() {
        if (array.length == 0)
            return array;

        int maxWordLength = lengthify.apply(array[0]);
        for (T s : array) {
            maxWordLength = Math.max(lengthify.apply(s), maxWordLength);
        }

        T[] workingArray = Arrays.copyOf(array, array.length);
        for (int bi = 0; bi <= maxWordLength - 1; bi++) {
            final int finalBi = bi;
            CountingObjectSort<T> countingSort
                    = new CountingObjectSort<>(workingArray,
                    minBucketNumber, maxBucketNumber,
                    o -> bucketify.apply(new Pair<>(o, finalBi)));
            workingArray = countingSort.sort();
        }

        return workingArray;
    }

    static char toUpperCase(char c) {
        return c >= 'a' ? (char) (c - ('a' - 'A')) : c;
    }

    static Function<Pair<String, Integer>, Integer> stringCaseSensitiveBucketify =
        o -> o.getK().length() > o.getV() ? (o.getK().charAt(o.getK().length()-1-o.getV()) - 'A') : 0;

    static Function<Pair<String, Integer>, Integer> stringCaseInSensitiveBucketify =
        o -> o.getK().length() > o.getV() ? (toUpperCase(o.getK().charAt(o.getK().length()-1-o.getV())) - 'A') : 0;

    static Function<String, Integer> stringLengthify = o -> o != null ? o.length() : 0;

    static Function<Integer, Integer> intBase10Lengthify = i ->  {
        if(i == null)
            return 0;

        return len(i);
    };

    static int len(int n) {
        int l = 0;
        while(n > 0) {
            l++;
            n = n/10;
        }
        return l;
    }

    static Function<Pair<Integer, Integer>, Integer> intBase10Bucketify = pair -> {
        int n = pair.getK();
        for(int k=len(n)-1; k > pair.getV(); k--) {
            n = n % (int)Math.pow(10, k);
        }
        return n/(int)Math.pow(10, pair.getV());
    };


    public static void main(String[] args) {
        String[] array1 = new String[]{"axz", "byn", "axyp", "an"};
        RadixSort<String> radixSort1 = new RadixSort<>(array1, 'A', 'z', stringLengthify, stringCaseInSensitiveBucketify);
        String[] sortedArray1 = radixSort1.sort();
        System.out.println(printObjectArray(array1) + ".sort = " + printObjectArray(sortedArray1));

        String[] array2 = new String[]{"axz", "Byn", "axyp", "an"};
        RadixSort<String> radixSort2 = new RadixSort<>(array2, 'A', 'z', stringLengthify, stringCaseInSensitiveBucketify);
        String[] sortedArray2 = radixSort2.sort();
        System.out.println(printObjectArray(array2) + ".sort = " + printObjectArray(sortedArray2));

        String[] array3 = new String[]{};
        RadixSort<String> radixSort3 = new RadixSort<>(array3, 'A', 'z', stringLengthify, stringCaseInSensitiveBucketify);
        String[] sortedArray3 = radixSort3.sort();
        System.out.println(printObjectArray(array3) + ".sort = " + printObjectArray(sortedArray3));

        Integer[] array4 = new Integer[]{10, 30, 5, 23, 60, 2, 45, 90};
        RadixSort<Integer> radixSort4 = new RadixSort<>(array4, 0, 9, intBase10Lengthify, intBase10Bucketify);
        Integer[] sortedArray4 = radixSort4.sort();
        System.out.println(printObjectArray(array4)+".sort = "+printObjectArray(sortedArray4));

        Integer[] array5 = new Integer[]{2, 2, 2, 2, 2, 2, 2, 2, 1, 9};
        RadixSort<Integer> radixSort5 = new RadixSort(array5, 0, 9, intBase10Lengthify, intBase10Bucketify);
        Integer[] sortedArray5 = radixSort5.sort();
        System.out.println(printObjectArray(array5)+".sort = "+printObjectArray(sortedArray5));
    }
}
