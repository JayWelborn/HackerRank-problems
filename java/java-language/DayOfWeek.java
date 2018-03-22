import java.util.Scanner;
import java.util.Calendar;

public class Solution {
    public static String getDay(String day, String month, String year) {
        /*
        * Write your code here.
        */
        Calendar c = Calendar.getInstance();
        c.set(Integer.parseInt(year), Integer.parseInt(month) - 1, Integer.parseInt(day));

        String[] weekDays = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
        int dayOfWeek = c.get(Calendar.DAY_OF_WEEK);
        return (weekDays[dayOfWeek - 1]).toUpperCase();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String month = in.next();
        String day = in.next();
        String year = in.next();

        System.out.println(getDay(day, month, year));
    }
}
