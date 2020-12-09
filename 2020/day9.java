
import java.io.File; 
import java.util.*; 

public class day9 {
	static ArrayList<Integer> data = read_file("day9.txt");
	static int invalid;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		// part 1
		for (int i = 26; i < data.size(); i++) {
			if (! isSum(i)) {
				System.out.println(i + " " + data.get(i));
				invalid = data.get(i);
				break;
			}
		}
		

		// part 2
		for (int start_i = 0; start_i < data.size(); start_i++) {
			int end_i = end_i_to_invalid(start_i); 
			if (end_i > 0) {
				ArrayList<Integer> seq = new ArrayList<Integer>();
				for (int j = start_i; j < end_i + 1; j++) {
					seq.add(data.get(j));
				}
				
				// get min
				int m = get_min(seq);
				
				// get max
				int n = get_max(seq);
				
				// print result
				System.out.println(m + ", " + n + ", " + (m+n));
				break;
			}
		}		
	}


	private static int get_max(ArrayList<Integer> seq) {
		// TODO Auto-generated method stub
		return Collections.max(seq);
	}


	private static int get_min(ArrayList<Integer> seq) {
		// TODO Auto-generated method stub
		return Collections.min(seq);
	}


	private static int end_i_to_invalid(int i) {
		// TODO Auto-generated method stub
		int s = 0;
		while(s < invalid) {
			s += data.get(i);
			if (s == invalid) {
				return i;
			}
			i++;
		}
		return -1;
	}


	private static boolean isSum(int i) {
		// TODO Auto-generated method stub
		ArrayList<Integer> pre = new ArrayList<Integer>();
		
		// get 25 previous values
		for (int j = 0; j < 25; j++) {
			pre.add(data.get(i - j - 1));
		}
		
		int val = data.get(i);
		
		for (int n : pre) {
			if (val == 2*n) {
				continue;
			}
			else {
				if (pre.contains(val - n)) {
					return true;
				}
			}
		}
		
		return false;
	}


	private static ArrayList<Integer> read_file(String fileName) {
		ArrayList<Integer> list = new ArrayList<Integer>();
	    
	    try {
	    	Scanner scan = new Scanner(new File(fileName));
	    	while(scan.hasNext()){
	    		list.add(Integer.parseInt(scan.nextLine()));
	    	}
	    }
	    catch(Exception e) {	
	    }
	    
		return list;
	}
}
