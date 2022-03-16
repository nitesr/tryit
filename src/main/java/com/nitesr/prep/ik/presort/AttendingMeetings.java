package com.nitesr.prep.ik.presort;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class AttendingMeetings {
    public static int can_attend_all_meetings(ArrayList<int[]> intervals) {
        Collections.sort(intervals, Comparator.comparingInt(a -> a[0]));

        for(int i=1; i < intervals.size(); i++) {
            int[] previous = intervals.get(i-1);
            int[] current = intervals.get(i);

            if(current[0] < previous[1]) {
                return 0;
            }
        }

        return 1;
    }

    public static void main(String[] args) {
        ArrayList<int[]> intervals1 = new ArrayList<>(3);
        intervals1.add(new int[]{10, 20});
        intervals1.add(new int[]{30, 40});
        intervals1.add(new int[]{5, 15});
        System.out.println("0 == "+ can_attend_all_meetings(intervals1));
    }
}
