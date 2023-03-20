

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static int n, m;
	static ArrayList<Integer>[] adjList;
	static boolean[] visited;
	static int cnt;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		adjList = new ArrayList[n+1];
		visited = new boolean[n+1];
		
		for (int i = 1; i < n+1; i++) {
			adjList[i] = new ArrayList();
		}
		for (int i = 0; i < m; i++) {
			int from = sc.nextInt();
			int to = sc.nextInt();
			adjList[from].add(to);
			adjList[to].add(from);
		}
//		System.out.println(Arrays.toString(adjList));
		cnt = 0;
		for (int i = 1; i < n+1; i++) {
			if (!visited[i])
			{
//				System.out.println(Arrays.toString(visited));
				BFS(i);
				cnt++;
			}
		}
		System.out.println(cnt);
	}
	
	private static void BFS(int startNode) {
		Queue<Integer> queue = new LinkedList();
		queue.add(startNode);
		visited[startNode] = true;
		
		while(!queue.isEmpty()) {
			int currNode = queue.poll();
//			System.out.println(Arrays.toString(visited));
			visited[currNode] = true;
			for (int node : adjList[currNode]) {
				if (!visited[node]) {
					queue.add(node);
					visited[node] = true;
				}
			}
		}
	}
}
