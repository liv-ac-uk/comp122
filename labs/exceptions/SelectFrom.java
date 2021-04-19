
public class SelectFrom {

	public int[] arrayOfNumbers;
	

	
	public SelectFrom(String[] args) {
		for (int i = 0; i <= arrayOfNumbers.length; i++) {
			arrayOfNumbers[i] = Integer.parseInt(args[i]);
		}
	}
	public int selectFromArray(int i) {
		if (arrayOfNumbers.length <= i || i < 0)
			return -1;
		return arrayOfNumbers[i];
	}
	
	
	public static void main(String[] args) {
		SelectFrom n = new SelectFrom(args);
		n.arrayOfNumbers = new int[args.length];
		System.out.println(n.selectFromArray(args.length-1));

	}

}
