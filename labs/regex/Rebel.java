import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Rebel {
    public static void main(String args[]) {
        String input = "It is a period of civil war. Rebel spaceships, striking from a hidden base, have won their first victory against the evil Galactic Empire. During the battle, Rebel spies managed to steal secret plans to the Empire's ultimate weapon, the DEATH STAR, an armored space station with enough power to destroy an entire planet.";

        Pattern pattern = Pattern.compile("Rebel");
        Matcher matcher = pattern.matcher(input);
        while(matcher.find()) {
            System.out.println(matcher.start());
            System.out.println(matcher.end());
            System.out.println(input.substring(matcher.start(), matcher.end()));
        }
    }
}