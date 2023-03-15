

import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Scanner;

public class Main {
	static int n, m;
	static List<int[]> answerArr;
	static int[] numbers, input;
	static boolean[] visit;
	static String tmp;
	static LinkedHashSet<String> ans;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		
		input = new int[n];
		numbers = new int[m];
		visit = new boolean[n];
		ans = new LinkedHashSet<>();
		
		for (int i = 0; i < n; i++) {
			input[i] = sc.nextInt();
		}
		Arrays.sort(input);
		comb(0, 0);
		ans.forEach(System.out::println);
	}
	
	private static void comb(int cnt, int startIndex) {
		if (cnt == m) {
			tmp = "";
			for (int p: numbers) {
				tmp += p + " ";
			}
			ans.add(tmp);
			return;
		}
		
		for (int i = startIndex; i < n; i++) {
			numbers[cnt] = input[i];
			comb(cnt+1, i+1);

		}
	}

}
