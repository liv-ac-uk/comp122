public class WC {
    public static void main(String[] args) {
        if (args[0].equals("-w")) {
            System.out.println(wordCount(args[1]));
        }

        if (args[0].equals("-m")) {
            System.out.println(charCount(args[1]));
        }
    }

    private static int wordCount(String input) {
        String[] words = input.split("\\s");
        return words.length;
    }

    private static int charCount(String input) {
        return input.length();
    }
}
