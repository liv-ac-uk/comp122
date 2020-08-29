import java.util.Scanner;

public class LeapYear_final {
    public static void main(String[] args) {
        Scanner myScanner = new Scanner(System.in);
        int year = myScanner.nextInt();
        System.out.println(isLeapYear(year));
    }

    public static boolean isLeapYear(int year) {
        return (year % 4 == 0 && !(year % 400 == 0));
    }
/*
    public static boolean isLeapYearCondensed(int year) {
        return (Your code here);
    }
*/
}

