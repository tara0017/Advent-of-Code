import java.io.File;  
import java.util.*;

public class day3 {
	static ArrayList<String> data;
	
	public static void main(String[] args) {
		
		data = read_file("day3.txt");
		
		// part 1
		int num_trees = check_slope(3, 1);
		System.out.println("Trees hit: " + num_trees);
		
		// part 2
		long product = 1;
		product *= check_slope(1, 1);
		product *= check_slope(3, 1);
		product *= check_slope(5, 1);
		product *= check_slope(7, 1);
		product *= check_slope(1, 2);
		System.out.println("Trees hit: " + product);
	}


	private static int check_slope(int x_change, int y_change) {
		int x = 0;
		int y = 0;
		int num_trees = 0;
		
		for (int i = 0; i < data.size(); i += y_change) {
			if (data.get(y).charAt(x) == '#') {
				num_trees += 1;
			}
			x = (x + x_change) % data.get(0).length();
			y += y_change;
		}
		
		return num_trees;
	}


	private static ArrayList<String> read_file(String fileName) {
		ArrayList<String> list = new ArrayList<String>();
	    
	    try {
	    	Scanner scan = new Scanner(new File(fileName));
	    	while(scan.hasNext()){
	    		list.add(scan.nextLine());
	    	}
	    }
	    catch(Exception e) {	
	    }
	    
		return list;
	}
	
}
