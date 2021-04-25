import static org.junit.jupiter.api.Assertions.*;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class IOLabPartOneTest {

	String fileStringOne;
	String fileStringTwo;
	String[] intFieldNames;
	String[] boolFieldNames;
	String[] stringFieldNames;

	ArrayList<OurData> dataToTestOne;
	ArrayList<OurData> dataToTestTwo;

	@BeforeEach
	public void setup() throws IOException {

		intFieldNames = new String[] { "program_length", "passed_tests", "total_tests" };
		boolFieldNames = new String[] { "correct" };
		stringFieldNames = new String[] { "program", "problem" };

		File fileOne = new File("programs.txt");
		File fileTwo = new File("programsTwo.txt");

		fileStringOne = Files.readString(fileOne.toPath()) + "\n";
		fileStringTwo = Files.readString(fileTwo.toPath()) + "\n";

		IOLabPartOne ioLab = new IOLabPartOne();
		dataToTestOne = ioLab.parseStructuredTextFile(fileOne.toPath());
		dataToTestTwo = ioLab.parseStructuredTextFile(fileTwo.toPath());
	}

	public void checkDataFields(String fileString, ArrayList<OurData> data, String errorMessage) throws IOException {

		String comp = "";
		for (int i = 0; i < data.size(); i++) {
			comp += "Program_Description " + (i + 1) + "\n" + data.get(i).getDataAsString() + "\n";
		}

		String compNoWs = comp.replaceAll("\\s+", "");
		String fileStringNoWs = fileString.replaceAll("\\s+", "");

		if (!compNoWs.equals(fileStringNoWs)) {
			fail(errorMessage + " expected\n" + fileString + " but data from your code resulted in\n" + comp);
		}
	}

	public void checkFieldsForType(HashMap<String, ?> processedMap, String[] fieldNames, String expectedType) {
		for (String fieldName : fieldNames) {
			if (!processedMap.containsKey(fieldName)) {
				fail(fieldName + " was not stored as an " + expectedType);
			}
		}
	}

	@Test
	public void typeCorrectTest() {
		try {
			for (OurData od : dataToTestTwo) {
				checkFieldsForType(od.getBooleanFields(), boolFieldNames, "boolean");
				checkFieldsForType(od.getIntFields(), intFieldNames, "int");
				checkFieldsForType(od.getStringFields(), stringFieldNames, "String");
			}
		} catch (Exception e) {
			fail("Encountered the following exception " + e.toString()
					+ " while testing that your program stores each value as the correct type");
		}
	}

	// builds and compares the String content against the file being read with
	// Files.readString
	@Test
	public void defaultFileCorrect() {
		try {
			String errorMessage = "Your data did not match with the default programs.txt file,";
			checkDataFields(fileStringOne, dataToTestOne, errorMessage);
		} catch (Exception e) {
			fail("Encountered the following exception " + e.toString()
					+ " while testing the default programs.txt file");
		}

	}

	// We test this one to make sure they aren't hardcoding.
	@Test
	public void differentFileCorrect() {
		String errorMessage = "Your data did not match with a different file of the same format"
				+ ", make sure you aren't hardcoding values,";
		try {
			checkDataFields(fileStringTwo, dataToTestTwo, errorMessage);
		} catch (Exception e) {
			fail("Encountered the following exception " + e.toString()
					+ " while testing a different file from the default.");
		}
	}

}
