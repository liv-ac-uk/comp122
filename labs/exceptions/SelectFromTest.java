
public class SelectFromTest {
	
	public SelectFromTest() {
			boolean testPassed = true;
			try {
				String[] args = { "4", "6", "3" };
				int[] expected = { 4, 6, 3 };
				SelectFrom s = new SelectFrom(args);
				for (int i = 0; i < args.length; i++) {
					if (!(s.selectFromArray(i) == expected[i])) {
						System.out.println("Test Failed: When selecting element " + i + " we expected " + expected[i] + " but got"
								+ s.selectFromArray(i));
						testPassed = false;
					}
				}

			} catch (ArrayIndexOutOfBoundsException aie) {
				System.out.println("Test Failed: " + aie.toString());
				return;
			} catch (NullPointerException npe) {
				System.out.println("Test Failed: " + npe.toString());
				return;
			} catch (Exception e) {
				System.out.println("Test Failed: " + e.toString());
				return;
			}
			
			if (testPassed)
				System.out.println("Test Passed");
		
	}
	public static void main(String[] args) {
		new SelectFromTest();
	}

}
