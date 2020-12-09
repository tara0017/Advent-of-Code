import java.io.File;  
import java.util.*;
import java.util.Map.Entry;

public class day6 {
	static int totalPart1 = 0;
	static int totalPart2 = 0;
	
	public static void main(String[] args) {
		read_file("day6.txt");	
		
		System.out.println("Part 1: " + totalPart1);
		System.out.println("Part 2: " + totalPart2);
	}


	private static void read_file(String fileName) {
		ArrayList<String> group = new ArrayList<String>();
		
	    try {
	    	Scanner scan = new Scanner(new File(fileName));
	    	while(scan.hasNext()){
	    		String s = scan.nextLine();
	    		
	    		if (s.length() == 0) {
	    			
	    			totalPart1 += num_yes(group);
	    			totalPart2 += consensusYes(group);
	    			
	    			//reset group
	    			group.clear();
	    			
	    		}else {
	    			group.add(s);
	    		}
	    	}
	    }
	    catch(Exception e) {	
	    	System.out.println(e);
	    }

	}

	private static int consensusYes(ArrayList<String> group) {
		// TODO Auto-generated method stub
		ArrayList<Character> answers = new ArrayList<Character>();
		ArrayList<Character> itemsToRemove = new ArrayList<Character>();
		
		String firstItem = group.get(0);
		for (int i = 0; i < firstItem.length(); i++) {
			answers.add(firstItem.charAt(i));
		}
		
		for (int i = 1; i < group.size(); i++) {
			String item = group.get(i);
			
			itemsToRemove.clear();
			
			for (char c : answers) {
				String str_c = "" + c;
			
				if (! item.contains(str_c)) {
					itemsToRemove.add(c);
				}
			}
			
			ArrayList<Character> temp = new ArrayList<Character>();
			
			for (char c : answers) {
				if (! itemsToRemove.contains(c)) {
					temp.add(c);
				}
			}
			answers.clear();
			for (char c : temp)
				answers.add(c);
			
		}
		return answers.size();
	}


	private static int num_yes(ArrayList<String> group) {
		// TODO Auto-generated method stub
		ArrayList<Character> answers = new ArrayList<Character>();
		
		for (String s: group) {
			for (int i = 0; i < s.length(); i++) {
				char c = s.charAt(i);
				if (! answers.contains(c)) {
					answers.add(c);
				}
			}
		}
		return answers.size();
	}
	
}
