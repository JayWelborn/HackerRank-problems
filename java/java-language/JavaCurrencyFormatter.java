import java.util.*;
import java.text.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();

        NumberFormat usFormat = NumberFormat.getCurrencyInstance();
        String us = usFormat.format(payment);

        NumberFormat inFormat = NumberFormat.getCurrencyInstance(new Locale("en", "IN"));
        String india = inFormat.format(payment);

        NumberFormat chiFormat = NumberFormat.getCurrencyInstance(Locale.CHINA);
        String china = chiFormat.format(payment);

        NumberFormat fraFormat = NumberFormat.getCurrencyInstance(Locale.FRANCE);
        String france = fraFormat.format(payment);

        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}
