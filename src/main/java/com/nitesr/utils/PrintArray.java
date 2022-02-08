package com.nitesr.utils;

/**
 * Created by nitesh on 1/22/22.
 */
public class PrintArray {

    public static StringBuffer printIntArray(int[] array) {
        return printIntArray(array, new StringBuffer());
    }

    public static StringBuffer printObjectArray(Object[] array) {
        return printArray(array, new StringBuffer());
    }

    public static StringBuffer printIntArray(int[] array, StringBuffer buffer) {
        buffer.append("[ ");
        for (int i = 0; i < array.length; i++) {
            buffer.append(array[i] + ", ");
        }
        if (array.length > 0) {
            buffer.delete(buffer.length() - 2, buffer.length());
        }
        buffer.append(" ]");
        return buffer;
    }

    public static StringBuffer printArray(Object[] array, StringBuffer buffer) {
        buffer.append("[ ");
        for (int i = 0; i < array.length; i++) {
            buffer.append(array[i] + ", ");
        }
        if (array.length > 0) {
            buffer.delete(buffer.length() - 2, buffer.length());
        }
        buffer.append(" ]");
        return buffer;
    }
}
