import java.io.IOException;

public class ExceptronPlatform {


	
	public String runExceptron(Exceptron exceptron) throws IOException {
		//exceptron.doSomeStuff();
		return "Everything's Fine\n";
	}
	public static void main(String[] args) throws IOException {
		//You can run the scenarios directly and debug in this main section,
		//but don't forget to test directly using ExceptronTest as
		//described in the Lab
		int[] scenarios = {0,1,2,3,4,5,6,7,8,9};
		/*
		 * Scenarios by index, Exceptron throws exceptions in order given 
		 * 0 - Exception
		 * 1 - NumberFormatException
		 * 2 - SQLException 
		 * 3 - ArrayIndexOutOfBoundsException
		 * 4 - SuperCoolException
		 * 5 - Exception,IOException,SQLException, IOException,Exception, IOException
		 * 6 - Exception,IOException,SQLException, IOException,Exception, IOException, ArrayIndexOutOfBoundsException, IOException
		 * 7 - Exception,IOException,SQLException, IOException,Exception, IOException, SQLException, IOException, ArrayIndexOutOfBoundsException
		 * 8 - Should return Everything's Fine\n
		 */
		ExceptronPlatform ex = new ExceptronPlatform();
		//for (int i = 0; i < scenarios.length; i++) {
			System.out.println(ex.runExceptron(new Exceptron(0)));
		//}
	}

}
