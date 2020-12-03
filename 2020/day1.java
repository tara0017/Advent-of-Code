
import java.io.File; 
import java.util.*; 

public class day1 {

	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList<String> data = read_file("day1.txt");
		// part 1
		
		for (int i = 0; i < data.size(); i++) {
			for (int j = i+1; j < data.size(); j++) {
				int iv = Integer.parseInt(data.get(i));
				int jv = Integer.parseInt(data.get(j));
				if (iv + jv == 2020){
					System.out.println(iv + " " + jv + "\tPRODUCT: " + (iv * jv));
				}
			}
		}
		
		// part 2
		for (int r = 0; r < data.size(); r++) {
			for (int s = r+1; s < data.size(); s++) {
				for (int t = s+1; t < data.size(); t++) {
					int rv = Integer.parseInt(data.get(r));
					int sv = Integer.parseInt(data.get(s));
					int tv = Integer.parseInt(data.get(t));
					if (rv + sv+ tv == 2020) {
						System.out.println(rv + " " + sv + " " + tv + "\tPRODUCT: " + (rv*sv*tv) );
					}
				}
			}
		}
		
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
