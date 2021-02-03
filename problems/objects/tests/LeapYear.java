public class Largest {
    public static void main(String[] args) {
        int n = Terminal.nextInt("");
        int[] myArray = new int[n];

        for (int i = 0;i < n; i++) {
            myArray[i] = Terminal.nextInt("");
        }

        int largestValue = 0;

        for (int i = 0; i < n; i++) {
            if (myArray[i] > largestValue) {
                largestValue = myArray[i];
            }
        }

        System.out.println(largestValue);
    }
}
