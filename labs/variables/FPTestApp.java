public class FPTestApp {
    public static void main (String args[]) {
        double x = 0.1;
        double y = x+x+x+x+x+x+x+x+x+x;  //  Not equal to 1 (in Java-land)
        System.out.println(y);
     }
}