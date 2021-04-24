import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Spam {
    public static void main(String[] args) {
        // First read in the file
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

        // Define your pattern to return only the email addresses of spammers
        Pattern pattern = Pattern.compile("From:(.*)");

        // Instantiate our pattern matcher object
        Matcher matcher = pattern.matcher(spam);
        int count = 0;

        // Loop through our matches
        while(matcher.find()) {
            count++;
            System.out.println("Match number: " + count);
            System.out.println("Index Start: " + matcher.start());
            System.out.println("Index End: " + matcher.end());
            System.out.println("Complete Match: " + matcher.group(0));
            System.out.println("After From: " + matcher.group(1));
        }
    }
}