import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Rebel {
    public static void main(String args[]) {
        String input = "It is a period of civil war. Rebel spaceships, striking from a hidden base, have won their first victory against the evil Galactic Empire. During the battle, Rebel spies managed to steal secret plans to the Empire's ultimate weapon, the DEATH STAR, an armored space station with enough power to destroy an entire planet.  Pursued by the Empire’s sinister agents, Princess Leia races home aboard her starship, custodian of the stolen plans that can save her people and restore freedom to the galaxy…";
        if (args[0].equals("0")) {
            // Define our pattern and matches
            matcher = matchRebel(input);
        }

        if (args[0].equals("1")) {
            // Define our pattern and matches
            matcher = matchEmpire(input);
        }
        
        if (args[0].equals("2")) {
            // Define our pattern and matches
            matcher = matchLeia(input);

            // Loop through our matches
        }

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

    public static Matcher matchUpper(String input) {
        Pattern pattern = Pattern.compile("Rebel");
        Matcher matcher = pattern.matcher(input);

        return matcher;
    }
}

