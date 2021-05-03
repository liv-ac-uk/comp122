import java.io.BufferedWriter;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Scanner;

public class IOLabPartTwo {

	public IOLabPartTwo() {
		//Don't touch
	}
	
	public IOLabPartTwo(String[] args) throws IOException {
	//uncomment once parseCSVFile is working
	/*
		File file = new File("programs.csv");
		ArrayList<OurData> data = parseCSVFile(file.toPath());
		for (int i = 0; i < data.size(); i++) {
			System.out.println("Program Description " + (i+1));
			data.get(i).printData();
			System.out.println();
		}
	*/
	
	//uncomment once printCSVFile is working
	/*
	ArrayList<String> lines = (ArrayList<String>) Files.readAllLines(file.toPath());
	File newFile = new File("newprograms.csv");
	String[] headers = lines.get(0).split(",");
	printCSVFile(headers, data, newFile.toPath());
	*/
	}
	
	public static void main(String[] args) throws IOException {
		new IOLabPartTwo(args);
	}
	
	public OurData parseCSVLine(Scanner scan, String[] headers) {
		
		OurData od = new OurData(headers);
		int index = 0;
		/* Keep scanning until stream is empty i.e. scan.hasNext() returns false.
		Check if each element is a boolean or int, and if so, scan this value directly.
		Call od.setField(fieldName, value), where value is the value you scanned and
		fieldName is headers[index], where index is incremented after each value scanned.
 		Note: You can use programs.csv as an example, but it
		should work with any CSV file we provide. These files will be composed exclusively of
		String, int, and boolean values. */
		return od;
	}
	
	public ArrayList<OurData> parseCSVFile(Path path) throws IOException {
		//Don't Touch
		ArrayList<OurData> ourDataObjects = new ArrayList<>();
		//Every line of the file is read in for you into lines
		ArrayList<String> lines = (ArrayList<String>) Files.readAllLines(path);
		
		/*Populate ourDataObjects from any given csv file using Scanner scan to assist.
		Remember, the first line contains the headers, so we grab
		this and transform it into an array of Strings.
		 */
		
		String[] headers = lines.get(0).split(",");
		
		for (int i = 1; i < lines.size(); i++) {
			try (Scanner scan = new Scanner(lines.get(i))) {
				scan.useDelimiter(",");
				ourDataObjects.add(parseCSVLine(scan, headers));
			}
		}
		
		return ourDataObjects;
	}
	
	public void printCSVFile(String[] headers, ArrayList<OurData> ourDataObjects, Path outPath) throws IOException {
		/*
		 * Given the headers, ourDataObjects, and outPath, print out a new csv file "outPath.csv".
		 * String.join(",",aStringArray) takes an array of strings and then combines them into
		 * one string delimited by commas. Consequently, this is very useful for this part. 
		 * You can use OurData.getFieldAsString(String header) to get a value associated to a header in
		 * OurData.
		 */
		//this will automatically close the resource when done. If you don't close, or flush,
		//the write operation may not actually write to file.
		try (BufferedWriter bw = Files.newBufferedWriter(outPath)) {
			
		//build and write your csv to file here
		}
	
	}
	
}