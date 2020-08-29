import java.lang.Math;
import java.util.Scanner;

public class Newton_final {
    public static void main(String[] args) {
        Scanner myScanner = new Scanner(System.in);

        double n = myScanner.nextDouble();
        double guess = myScanner.nextDouble();
                
        sqRoot(n, guess);
    }

    public static void sqRoot(double n, double guess) {
        double epsilon = 0.0000001;
        double new_guess = ((n / guess) + guess) / 2;
        int i = 1;

        if (Math.abs(guess - new_guess) < epsilon) {
            System.out.println(i);
            System.out.println(new_guess);
            return;
        }

        else {
            i += 1;
        }

        while (Math.abs(guess - new_guess) > epsilon) {
            i += 1;
            guess = new_guess;
            new_guess = ((n / guess) + guess) / 2;
        }

        System.out.println(i);
        System.out.println(new_guess);
    }
}