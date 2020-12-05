import java.io.File;  
import java.util.*;

public class day5 {
	static ArrayList<String> data;
	static ArrayList<String> seats = new ArrayList<String>();
	
	public static void main(String[] args) {
		
		data = read_file("day5.txt");
		
		int highest_seat_id = 0;
		
		for(String d : data) {
			int row = get_value(d.substring(0, 7));
			int col = get_value(d.substring(7));
			int seat_id = get_seat_id(row, col);
			
			String seat = row + "," + col;
			seats.add(seat);
			
			// part 1
			// update highest seat id
			if (seat_id > highest_seat_id) {
				highest_seat_id = seat_id;
			}
		}

		System.out.println(highest_seat_id);
		get_missing_seat();
		
	}


	private static void get_missing_seat() {
		// TODO Auto-generated method stub		
		for (int r = 0; r < 102; r++) {
			for (int c = 0; c < 8; c++) {
				String seat = r + "," + c;
				
				if (! seats.contains(seat)) {
					System.out.println(seat + " " + get_seat_id(r, c));
				}
			}
		}
	}





	private static int get_seat_id(int row, int col) {
		// TODO Auto-generated method stub
		return 8 * row + col;
	}


	private static int get_value(String s) {
		// TODO Auto-generated method stub
		int[] rng = {0,0};
		if (s.length() == 7) {
			rng[1] = 127;
		}else {
			rng[1] = 7;
		}
		
		int i = 0;
		while (rng[1] > rng[0]) {
			int diff = rng[1] - rng[0];
			
			if (s.charAt(i) == 'B' || s.charAt(i) == 'R') {
				rng[0] += (diff / 2 + 1);
				
			}else if (s.charAt(i) == 'F' || s.charAt(i) == 'L') {
				rng[1] -= (diff / 2 + 1);
			}
			i++;
		}
		return rng[0];
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
