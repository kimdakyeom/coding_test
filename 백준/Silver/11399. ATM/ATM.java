

import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		int[] sortArr = new int[n];
		int answer = 0;
		for (int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}
		Arrays.sort(arr);
		sortArr[0] = arr[0];
		for (int i = 1; i < n; i++) {
			sortArr[i] = sortArr[i-1] + arr[i];
		}
		for (int a: sortArr) {
			answer += a;
		}
//		System.out.println(Arrays.toString(sortArr));
		System.out.println(answer);
	}

}
