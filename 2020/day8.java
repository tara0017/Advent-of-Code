
import java.io.File; 
import java.util.*; 

public class day8 {
	static ArrayList<String> instructions = read_file("day8.txt");
	static int acc_value = 0;
	static boolean answer_found = false;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		// part 1
		run_instructions();
		System.out.println(acc_value);
		
		
		// part 2
		int current_i = 0;
		
		while(! answer_found) {
			for (int i = current_i; i < instructions.size(); i++) {
				String code = instructions.get(i).substring(0,3);
				if (code.equals("nop") || code.equals("jmp")) {
					switch_command(i);
					current_i = i;
					run_instructions();
					break;
				}
			}
			
			if (! answer_found) {
				switch_command(current_i);
				current_i++;
				acc_value = 0;
			}
		}
		System.out.println(acc_value);
				
	}

	private static void switch_command(int i) {
		// TODO Auto-generated method stub
		String s = instructions.get(i);
		String code = s.substring(0,3);
		

		if (code.equals("nop")) {
			String new_s = "jmp" + s.substring(3);
			instructions.set(i, new_s);
		}else {
			String new_s = "nop" + s.substring(3);
			instructions.set(i, new_s);
		}
	}

	private static void run_instructions() {
		// TODO Auto-generated method stub
		int index = 0;
		ArrayList<Integer> visited_indices = new ArrayList<Integer>();

		while(! visited_indices.contains(index)) {
			if (index == instructions.size()) {
				answer_found = true;
				System.out.println("Part 2:");
				break;			
			}
			
			visited_indices.add(index);
			
			String inst = instructions.get(index);
			String code = inst.substring(0, 3);
			int val = Integer.parseInt(inst.substring(4));
			
			if (code.equals("nop")) {
				index++;
			}
			else if (code.equals("acc")) {
				acc_value += val;
				index++;
			}else if (code.equals("jmp")) {
				index += val;
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
