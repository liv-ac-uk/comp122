import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Spam {
    public static void main(String[] args) {
        // First read in the file
        String spam = getSpam();    

        Matcher matcher = matchFrom(spam);
            int count = 0;
            // // Loop through our matches
            // while(matcher.find()) {
            //     count++;
            //     System.out.println("Match number: " + count);
            //     System.out.println("Index Start: " + matcher.start());
            //     System.out.println("Index End: " + matcher.end());
            // }
            
        if (args[0].equals("0")) {
            System.out.println(spam);
            // Define our pattern and matches
            matcher = matchFrom(spam);
            count = 0;
            // Loop through our matches
            while(matcher.find()) {
                count++;
                System.out.println("Match number: " + count);
                System.out.println("Index Start: " + matcher.start());
                System.out.println("Index End: " + matcher.end());
            }
        }

        if (args[0].equals("1")) {
            // Define our pattern and matches
            matcher = matchEmails(spam);

            // Loop through our matches
        }
        
        if (args[0].equals("2")) {
            // Define our pattern and matches
            matcher = matchSenders(spam);

            // Loop through our matches
        }

        if (args[0].equals("3")) {
            // Define our pattern and matches
            matcher = matchRecipients(spam);

            // Loop through our matches
        }
    }

    public static String getSpam() {
        File input_file = new File("./Spam.txt");
        StringBuffer spam = new StringBuffer(); // Basically, a conglomerate of all of the lines in the file
        String line;

        try {
            Scanner file_reader = new Scanner(input_file);

            while (file_reader.hasNext()) {
                spam.append("\n" + file_reader.nextLine());
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        return spam.toString();
    }

    public static Matcher matchFrom(String input) {
        Pattern pattern = Pattern.compile("From:.*");

        // Instantiate our pattern matcher object
        Matcher matcher = pattern.matcher(input);

        return matcher;
    }

    public static Matcher matchEmails(String input) {
        Pattern pattern = Pattern.compile("\\w*@.*");

        // Instantiate our pattern matcher object
        Matcher matcher = pattern.matcher(input);

        return matcher;
    }

    public static Matcher matchSenders(String input) {
        Pattern pattern = Pattern.compile("From:.*");

        // Instantiate our pattern matcher object
        Matcher matcher = pattern.matcher(input);
 
        return matcher;
    }

    public static Matcher matchRecipients(String input) {
        Pattern pattern = Pattern.compile("From:.*");

        // Instantiate our pattern matcher object
        Matcher matcher = pattern.matcher(input);

        return matcher;
    }
}
