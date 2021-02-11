import java.util.Scanner;
import java.util.InputMismatchException;


public class Comp122 {

    public static String getString(String prompt) {
      System.out.print(prompt);
      Scanner scan = new Scanner(System.in);
      return scan.nextLine();
    }

    public static long getLong(String prompt) {
      long l;

      do{
        try {
            System.out.print(prompt);
            Scanner scan = new Scanner(System.in);
            l = scan.nextLong();
            break;
        }
        catch (InputMismatchException e)  {}
      }while(true);

      return l;
    }

    public static int getInt(String prompt) {
      int i;

      do{
        try {
            System.out.print(prompt);
            Scanner scan = new Scanner(System.in);
            i = scan.nextInt();
            break;
        }
        catch (InputMismatchException e)  {}
      }while(true);

      return i;
    }
}
