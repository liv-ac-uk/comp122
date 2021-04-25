/**
 * 
 * 
 * IMPORTANT NOTE: DO NOT MODIFY THIS CODE, IT WILL NOT BE SUBMITTED TO CHECK50!
 * 
 * @author Thomas Welsch
 * 
 * A data helper class that emulates the operations of a database.
 * 
 * 
 */
import java.util.HashMap;

public class OurData {
	
	private HashMap<String,String> stringFields = new HashMap<>();
	private HashMap<String, Integer> intFields = new HashMap<>();
	private HashMap<String, Boolean> booleanFields = new HashMap<>();
	
	private String[] fieldNames;
	
	/**
	 * A Constructor that takes an array of Strings as a parameter and uses these
	 * to set fieldNames.
	 * @param fieldNames - An array of Strings containing the name of the fields.
	 */
	public OurData(String[] fieldNames) {
		this.fieldNames = fieldNames;
	}
	
	/**
	 * Sets a field associated with fieldName with value.
	 * @param fieldName - The name of the field whose value you wish to set.
	 * @param value - The String value you wish to set for the field.
	 */
	public void setField(String fieldName, String value) {
		stringFields.put(fieldName, value);
	}
	
	/**
	 * Sets a field associated with fieldName with value.
	 * @param fieldName - The name of the field whose value you wish to set.
	 * @param value - The int value you wish to set for the field.
	 */
	public void setField(String fieldName, int value) {
		intFields.put(fieldName, value);
	}
	
	/**
	 * Sets a field associated with fieldName with value.
	 * @param fieldName - The name of the field whose value you wish to set.
	 * @param value - The boolean value you wish to set for the field.
	 */
	
	public void setField(String fieldName, boolean value) {
		booleanFields.put(fieldName, value);
	}
	
	/**
	 * Takes fieldName as a param and looks up the field associated with the fieldName. If it exists,
	 * the string value of the field is returned. Otherwise returns "N/A".
	 * @param fieldName - The name of the field whose value you wish to retrieve.
	 * @return String - Checks if the field exists, if so returns its String content, otherwise returns "N/A"
	 */
	public String getFieldAsString(String fieldName) {
		if (stringFields.containsKey(fieldName)) {
			return stringFields.get(fieldName);
		} else if(intFields.containsKey(fieldName)) {
			return Integer.toString(intFields.get(fieldName));
		} else if(booleanFields.containsKey(fieldName)) {
			return Boolean.toString(booleanFields.get(fieldName));
		} else {
			return "N/A";
		}
	}
	
	/**
	 * Returns the OurData object as a String in a format matching with programs.txt.
	 * @return String - The OurData object as a String, adhering to the format of the 6 field lines in programs.txt
	 */
	public String toString() {
		String retVal = "";
		for (String fieldName : fieldNames) {
			String val = "";
			if (stringFields.containsKey(fieldName)) {
				val = stringFields.get(fieldName);
			} else if(intFields.containsKey(fieldName)) {
				val = Integer.toString(intFields.get(fieldName));
			} else if(booleanFields.containsKey(fieldName)) {
				val = Boolean.toString(booleanFields.get(fieldName));
			} 
			retVal += fieldName + "-" + val + "\n";
		}
		return retVal;
	}
	
	/**
	 * Prints out the OurData object as a String 
	 */
	
	public void printData() {
		System.out.print(toString());
	}

	/**
	 * 
	 * @return HashMap<String,String> - A map containing the String fields. 
	 */
	public HashMap<String, String> getStringFields() {
		return stringFields;
	}

	/**
	 * 
	 * @return HashMap<String,Integer> - A map containing the int fields. 
	 */
	public HashMap<String, Integer> getIntFields() {
		return intFields;
	}

	/**
	 * 
	 * @return HashMap<String,Boolean> - A map containing the boolean fields. 
	 */
	public HashMap<String, Boolean> getBooleanFields() {
		return booleanFields;
	}

	/**
	 * 
	 * @return String[] - An array of Strings containing field names.
	 */
	public String[] getFieldNames() {
		return fieldNames;
	}

	/**
	 * Sets fieldNames value to be the passed in parameter.
	 * @param fieldNames - An array of Strings
	 */
	public void setFieldNames(String[] fieldNames) {
		this.fieldNames = fieldNames;
	}

}
