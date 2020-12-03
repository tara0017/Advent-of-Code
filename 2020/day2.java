
import java.io.File; 
import java.util.*; 

public class day2 {
	public static void main(String[] args) {
		int count  = 0;
		int count2 = 0;
		
		ArrayList<String> data = read_file("day2.txt");
		for (int i = 0; i < data.size(); i++) {
			String whole = data.get(i);
			String[] split = whole.split(" |-|: "); 

			// part 1
			if (is_valid_pwd(split)) {
				count++;
			}
			// part 2
			if (is_valid_pwd2(split)) {
				count2++;
			}
		}
		
		System.out.println("Valid Passwords: " + count);	// part 1
		System.out.println("Valid Passwords: " + count2);	// part 2
		
	}

	private static boolean is_valid_pwd2(String[] s) {
		int i      = Integer.parseInt(s[0]) - 1;
		int j      = Integer.parseInt(s[1]) - 1;
		char ch    = s[2].charAt(0);
		String pwd = s[3];
		
		if (pwd.charAt(i) != pwd.charAt(j)) {
			if (pwd.charAt(i) == ch || pwd.charAt(j) == ch) {
				return true;
			}
		}
		return false;
	}

	private static boolean is_valid_pwd(String[] s) {
		int least  = Integer.parseInt(s[0]);
		int most   = Integer.parseInt(s[1]);
		char ch    = s[2].charAt(0);
		String pwd = s[3];
		int num    = 0;
		
		for (char c: pwd.toCharArray()) {
			if (c == ch){
				num++;
			}
		}
		if (num >= least && num <= most) {
			return true;
		}
		return false;
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
