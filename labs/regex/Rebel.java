import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Rebel {
    private static String input = "It is a period of civil war. Rebel spaceships, striking from a hidden base, have won their first victory against the evil Galactic Empire. During the battle, Rebel spies managed to steal secret plans to the Empire's ultimate weapon, the DEATH STAR, an armored space station with enough power to destroy an entire planet.  Pursued by the Empire’s sinister agents, Princess Leia races home aboard her starship, custodian of the stolen plans that can save her people and restore freedom to the galaxy…";

    public static void main(String args[]) {
        Matcher matcher = null;

        // Part 1
        if (args[0].equals("0")) {
            // Define our pattern and matches
            matcher = matchRebel(input);
        }

        // Part 2
        if (args[0].equals("1")) {
            // Define our pattern and matches
            matcher = matchEmpire(input);
        }
        
        // Part 3
        if (args[0].equals("2")) {
            // Define our pattern and matches
            matcher = matchLeia(input);

            // Loop through our matches
        }

        // Part 4,5
        if (args[0].equals("3")) {
            // Define our pattern and matches
            matcher = matchUpper(input);
        }
        
        while(matcher.find()) {
            System.out.println(matcher.start());
            System.out.println(matcher.end());
            System.out.println(input.substring(matcher.start(), matcher.end()));
        }
    }
    
    public static Matcher matchRebel(String input) {
        Pattern pattern = Pattern.compile("Rebel");
        Matcher matcher = pattern.matcher(input);

        return matcher;
    }

    public static Matcher matchEmpire(String input) {
        Pattern pattern = Pattern.compile("Rebel");
        Matcher matcher = pattern.matcher(input);

        return matcher;
    }

    public static Matcher matchLeia(String input) {
        Pattern pattern = Pattern.compile("Rebel");
        Matcher matcher = pattern.matcher(input);

        return matcher;
    }

    // Parts 4,5
    public static Matcher matchUpper(String input) {
        Pattern pattern = Pattern.compile("Rebel");
        Matcher matcher = pattern.matcher(input);

        return matcher;
    }
}

