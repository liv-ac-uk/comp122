import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;

public class IOLabPartOne {

	public IOLabPartOne() {
		//Don't touch, used for testing your code
	}
	
	public IOLabPartOne(String[] args) throws IOException {
		//You can uncomment the code below to test if your function is correct
		//Just run the code and then compare the output in the terminal to programs.txt
		/*
		File file = new File("programs.txt");
		ArrayList<OurData> data = parseStructuredTextFile(file.toPath());
		for (int i = 0; i < data.size(); i++) {
			System.out.println("Program Description " + (i+1));
			data.get(i).printData();
			System.out.println();
		}
		*/
	}
	
	public static void main(String[] args) throws IOException {
		new IOLabPartOne(args);
	}

	
	public ArrayList<OurData> parseStructuredTextFile(Path path) throws IOException {
		ArrayList<OurData> ourDataObjects = new ArrayList<>();
		String[] fieldNames = {"problem", "program", "program_length", "passed_tests","total_tests","correct"};
		/*Populate ourDataObjects from a structured file a la programs.txt, we recommend iterating
		through the file using either a BufferedReader or by reading in as ArrayList
		with Files.readAllLines. Pay attention to the pattern of programs.txt. We have a line
		where we encounter Program_Description <number>. We then have have 6 lines of data followed
		by a blank line. How can we take advantage of this pattern? One approach would be to process
		the data 8 lines at a time, grabbing the data from the middle 6 lines. An alternative would
		be to take advantage of the blank line, using this as a marker that tells you where one ProgramDescription
		object ends and the other begins. You can check if a line is blank by calling yourString.isBlank().
		
		Once you've figured out the pattern, you can use a substring trick
		to get the field and value. For a given line with data in it, grab
		the index of the first "-" with yourString.indexOf("-"). Then use two calls of
		yourString.substring, one that goes from the beginning of the string to the index 
		of the first "-" to grab the field name (i.e. yourString.substring(0,yourIndex)), and the
		other that goes from the index after the first "-" to the end to get the value. An alternative
		approach would be to split the String on "-", where the resulting array's first element would be your
		field and the second element your value. There is an edge case where "-" is included in the value itself,
		we won't test this but if this was an assignment we would test this so your code would need to account for it.
		
		Once you've cracked all that you'll be ready to populate ourDataObjects.
		You can instantiate a new OurData object like so:
		OurData od = new OurData(fieldNames);
		You can update it's field
		with the function setField(fieldName,value). Note that the value needs to be of the correct type,
		for example program_length should have it's value passed in as an int, not a String, while
		the field correct should be passed in as a boolean. You could use the functions Integer.parseInt(String)
		and Boolean.parseInt(String) for this. */
			
		return ourDataObjects;
	}
	
	
}
