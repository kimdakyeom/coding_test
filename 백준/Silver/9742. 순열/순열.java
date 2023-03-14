

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {

	static String answer;
	static String input, answerTmp;
	static int m, totalCnt;
	static int[] numbers;
	static int[] all;
	static boolean[] isSelected;
	static boolean flag;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line;
		while ((line=br.readLine())!=null) {
			StringTokenizer st = new StringTokenizer(line);
			answer = "No permutation";
			answerTmp = "";
			input = st.nextToken();
			m = Integer.parseInt(st.nextToken());
			int max = 0;
			numbers = new int[input.length()];
			all = new int[input.length()];
			totalCnt = 0;
			flag = true;
			if (isInteger(input)) {
				for (int i = 0; i < input.length(); i++) {
					int ii = input.charAt(i) - '0';
					numbers[i] = ii;
					if (ii > max) max = ii;
				}
				isSelected = new boolean[max+1];
			}
			else {
				flag = false;
				for (int i = 0; i < input.length(); i++) {
					numbers[i] = (int)(input.charAt(i)-97);
				}
				isSelected = new boolean[26];
			}
			perm(0);
			System.out.println(input + " " + m + " = " + answer);
			
		}
	}
	
	public static boolean isInteger(String strValue) {
	    try {
	      Integer.parseInt(strValue);
	      return true;
	    } catch (NumberFormatException ex) {
	      return false;
	    }
	  }
	
	static void perm(int cnt) {
		if (cnt == input.length()) {
			totalCnt++;
			if (totalCnt == m) {
				if (flag) {
					answerTmp = Arrays.toString(all).replaceAll("[^0-9]","");
				}
				else {
					for (int i = 0; i < all.length; i++) {
						answerTmp += (char)(all[i]+97);
					}
				}
				answer = answerTmp;
				return;
			}
		}
		if (flag) {
			for (int i = 0; i < input.length(); i++) {
				if (isSelected[numbers[i]]) continue;
				all[cnt] = numbers[i];
				isSelected[numbers[i]] = true;
				perm(cnt+1);
				isSelected[numbers[i]] = false;
			}
		}
		else {
			for (int i = 0; i < input.length(); i++) {
				if (isSelected[numbers[i]]) continue;
				all[cnt] = numbers[i];
				isSelected[numbers[i]] = true;
				perm(cnt+1);
				isSelected[numbers[i]] = false;
			}
		}
	}

}
