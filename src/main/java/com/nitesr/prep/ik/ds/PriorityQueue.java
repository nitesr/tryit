package com.nitesr.prep.ik.ds;

import java.util.Arrays;
import java.util.Comparator;

import static com.nitesr.prep.utils.PrintArray.printIntArray;


public class PriorityQueue {
    private Comparator<Integer> priority = new IntMaxPriority();
    private int[] array;
    private int length;
    private final int MAX_LENGTH;

    public PriorityQueue(int[] array) {
        MAX_LENGTH = length = array.length;
        this.array = Arrays.copyOf(array,length);
        heapify();
    }

    public PriorityQueue(int[] array, Comparator<Integer> priority) {
        this(array);
        this.priority = priority;
        heapify();
    }

    public int get() {
        if (isEmpty())
            throw new ArrayIndexOutOfBoundsException("QUEUE_IS_EMPTY");

        return array[0];
    }

    public int delete() {
        int value = get();
        swap(length - 1, 0);
        length--;
        heapifyDown(0);
        return value;
    }

    public boolean isEmpty() {
        return length == 0;
    }

    public StringBuffer stringyfy() {
        PriorityQueue pq = new PriorityQueue(Arrays.copyOf(array, length), priority);
        while (!pq.isEmpty()) {
            pq.delete();
        }
        return printIntArray(pq.array);
    }

    // 1, 2, 3, 4, 5, 6, 7, 8, ....
    //  i -> (2i+1, 2i+2) ; e.g 0 -> 1, 2; 1 -> 3, 4; 2 -> 5, 6; 3 -> 7, 8
    //  (j-1)/2 <- j ; e.g. 0 -> 2; 1 <- 3; 2 <- 6; 3 <- 7

    // 2i+1 is an odd; 2i+1 = n-1; i = (n-2)/2
    // or 2i+2 is an even; 2i+2 = n-1; i = (n-3)/2
    // = n/2 - 1
    private void heapify() {
        //skip leaf nodes as they are already satisfy heap properties (structure & condition)
        int parent = length/2 - 1;

        for (int p = parent; p >= 0; p--) {
            heapifyDown(p);
        }
    }

    private void heapifyDown(int pi) {
        int li = 2 * pi + 1;
        int ri = li + 1;

        if (li >= length) {
            return;
        }

        int pl = priority.compare(array[pi], array[li]);
        int pr = ri < length ? priority.compare(array[pi], array[ri]) : Integer.MAX_VALUE;
        if (pl >= 0 && pr >= 0) {
            return;
        }

        int lr = ri < length ? priority.compare(array[li], array[ri]) : Integer.MAX_VALUE;
        if (lr < 0) {
            swap(pi, ri);
            heapifyDown(ri);
        } else {
            swap(pi, li);
            heapifyDown(li);
        }
    }

    private void swap(int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
        return;
    }

    static class IntMinPriority implements Comparator<Integer> {
        @Override
        public int compare(Integer o1, Integer o2) {
            return o2 - o1;
        }
    }

    static class IntMaxPriority implements Comparator<Integer> {
        @Override
        public int compare(Integer o1, Integer o2) {
            return o1 - o2;
        }
    }

    public static void main(String[] args) {
        int[] array1 = new int[]{10, 30, 5, 23, 60, 2, 45, 90};
        PriorityQueue priorityQueue1 = new PriorityQueue(array1);
        System.out.println(printIntArray(array1) + ".sort = " + priorityQueue1.stringyfy());

        int[] array2 = new int[]{10, 30, 2, 5, 23, 60, 2, 45, 90};
        PriorityQueue priorityQueue2 = new PriorityQueue(array2);
        System.out.println(printIntArray(array2) + ".sort = " + priorityQueue2.stringyfy());

        int[] array3 = new int[]{10, 30};
        PriorityQueue priorityQueue3 = new PriorityQueue(array3);
        System.out.println(printIntArray(array3) + ".sort = " + priorityQueue3.stringyfy());

        int[] array4 = new int[]{10};
        PriorityQueue priorityQueue4 = new PriorityQueue(array4);
        System.out.println(printIntArray(array4) + ".sort = " + priorityQueue4.stringyfy());

        int[] array5 = new int[]{};
        PriorityQueue priorityQueue5 = new PriorityQueue(array5);
        System.out.println(printIntArray(array5) + ".sort = " + priorityQueue5.stringyfy());
    }
}
