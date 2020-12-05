import java.io.File;  
import java.util.*;
import java.util.Map.Entry;

public class day4 {
	static ArrayList<HashMap<String, String>> data;
	
	public static void main(String[] args) {
		
		data = read_file("day4.txt");
		int count = 0;
		for (HashMap<String, String> passport : data) {
			if (is_it_valid(passport)) {
				count++;
			}
		}
		System.out.println("valid passports: " + count);
		
	}

	private static boolean is_it_valid(HashMap<String, String> passport) {
		// part 1
		if (!passport.containsKey("byr")) {			return false;		}
		if (!passport.containsKey("iyr")) {			return false;		}
		if (!passport.containsKey("eyr")) {			return false;		}
		if (!passport.containsKey("hgt")) {			return false;		}
		if (!passport.containsKey("hcl")) {			return false;		}
		if (!passport.containsKey("ecl")) {			return false;		}
		if (!passport.containsKey("pid")) {			return false;		}

		// part 2
		if (!is_byr_valid(passport)) {			return false;		}
		if (!is_iyr_valid(passport)) {			return false;		}
		if (!is_eyr_valid(passport)) {			return false;		}
		if (!is_hgt_valid(passport)) {			return false;		}
		if (!is_hcl_valid(passport)) {			return false;		}
		if (!is_ecl_valid(passport)) {			return false;		}
		if (!is_pid_valid(passport)) {			return false;		}
		
		return true;
	}

	private static boolean is_pid_valid(HashMap<String, String> passport) {
		// a nine-digit number, including leading zeroes
		String id = passport.get("pid");
		if (id.length() != 9) {
			return false;
		}
		try {
			int v = Integer.parseInt(id);
		}
		catch (Exception e){
			return false;
		}
		return true;
	}

	private static boolean is_ecl_valid(HashMap<String, String> passport) {
		// exactly one of: amb blu brn gry grn hzl oth
		String ecl = passport.get("ecl");
		if(ecl.equals("amb") || ecl.equals("blu") || ecl.equals("brn") || ecl.equals("gry") || ecl.equals("hzl") || ecl.equals("grn") || ecl.equals("oth")) {
			return true;
		}
		return false;
	}

	private static boolean is_hcl_valid(HashMap<String, String> passport) {
		// a # followed by exactly six characters 0-9 or a-f
		String hcl = passport.get("hcl");
		if (hcl.length() != 7) {
			return false;
		}
		if (hcl.charAt(0) != '#'){
				return false;
		}
		String allowed_chars = "abcdef1234567890";
		for (int i = 1; i < hcl.length(); i++) {
			String c = hcl.substring(i, i+1);
			if (!allowed_chars.contains(c)) {
				return false;
			}
		}
		return true;
	}

	private static boolean is_hgt_valid(HashMap<String, String> passport) {
		// a number followed by either cm or in:
		// If cm, the number must be at least 150 and at most 193.
		// If in, the number must be at least 59 and at most 76.
		String hgt = passport.get("hgt");
		String units = hgt.substring(hgt.length() - 2);
		int value = Integer.parseInt(hgt.substring(0, hgt.length() - 2));

		if (units.equals("cm")) {
			if (value >= 150 && value <= 193) {
				return true;
			}
		}
		else if (units.equals("in")) {
			if (value >= 59 && value <= 76) {
				return true;
			}
		}
		return false;
	}

	private static boolean is_eyr_valid(HashMap<String, String> passport) {
		// four digits; at least 2020 and at most 2030
		int yr = Integer.parseInt(passport.get("eyr"));
		if (yr < 2020 || yr > 2030) {
			return false;
		}
		return true;
	}

	private static boolean is_iyr_valid(HashMap<String, String> passport) {
		// four digits; at least 2010 and at most 2020
		int yr = Integer.parseInt(passport.get("iyr"));
		if (yr < 2010 || yr > 2020) {
			return false;
		}
		return true;
	}

	private static boolean is_byr_valid(HashMap<String, String> passport) {
		// four digits; at least 1920 and at most 2002
		int yr = Integer.parseInt(passport.get("byr"));
		if (yr < 1920 || yr > 2002) {
			return false;
		}
		return true;
	}

	private static ArrayList<HashMap<String, String>> read_file(String fileName) {
		ArrayList<HashMap<String, String>> info = new ArrayList<HashMap<String, String>>();
	    String str = "";
	    try {
	    	Scanner scan = new Scanner(new File(fileName));
	    	while(scan.hasNext()){
	    		String s = scan.nextLine();
	    		if (s.length() <= 1) {
	    			HashMap<String, String> passport = process_info(str);
	    			info.add(passport);
	    			str = "";
	    		}else {
	    			str = str + s + " ";
	    		}
	    	}
	    }
	    catch(Exception e) {	
	    }
	    
		return info;
	}

	private static HashMap<String, String> process_info(String s) {
		// TODO Auto-generated method stub
		HashMap<String, String> hm = new HashMap<String, String>() ;
		
		String[] split = s.split(" "); 
		for (int i = 0; i < split.length; i++) {
			hm.put(split[i].substring(0, 3), split[i].substring(4));
		}
		return hm;
	}
	
}
