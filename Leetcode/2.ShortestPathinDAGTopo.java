// https://www.google.com/search?sca_esv=cfaaa28257c63847&sxsrf=AHTn8zqD6RVi36Civns4n8FTWfi94qlgkA:1742777814444&q=shortest+path+in+DAGs&udm=7&fbs=ABzOT_CWdhQLP1FcmU5B0fn3xuWp6IcynRBrzjy_vjxR0KoDMp_4ut2Z3jppK72fzdIpWsAPKqaCEsfYDVEIw_Cc-oJMWwrTY6kC1WBAHAiNYD6D8adeHgx_u5frMn1f8vwBWSX9BxeKJHa9Wwza_-h6-q2zrBi1LOUtIamr_utCLq4YHPfTPwYeC6Jv1oXmfbPB8AS-lkhJ-L63G31RTou2q7LVMcqaEA&sa=X&ved=2ahUKEwjArLWkwaGMAxXvFTQIHUvoCVsQtKgLegQIGBAB&biw=732&bih=812&dpr=2#fpstate=ive&vld=cid:af223ec8,vid:ZUFQfFaU-8U,st:0

import java.util.ArrayList;
import java.util.Stack;



class Pair {
    int first, second;
    Pair(int _first, int _second) {
        this.first = _first;
        this.second = _second;
    }
}

// User function Template for Java
class Solution {
    private void topoSort(int node, ArrayList<ArrayList<Pair>> adj, int vis[], Stack<Integer> st) {
        vis[node] = 1;
        for (int i = 0; i < adj.get(node).size(); i++) {
            int v = adj.get(node).get(i).first;
            if (vis[v] == 0) {
                topoSort(v, adj, vis, st);
            }
        }
        st.add(node);
    }

    public int shortestPath(int N, int M, int[][] edges) {
        ArrayList<ArrayList<Pair>> adj = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            ArrayList<Pair> temp = new ArrayList<>();
            adj.add(temp);
        }

        for (int i = 0; i < M; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            int wt = edges[i][2];
            adj.get(u).add(new Pair(v, wt));
        }

        int vis[] = new int[N];
        Stack<Integer> st = new Stack<>();
        for (int i = 0; i < N; i++) {
            if (vis[i] == 0) {
                topoSort(i, adj, vis, st);
            }
        }

        int dist[] = new int[N];
        for (int i = 0; i < N; i++) {
            dist[i] = (int)(1e9);
        }

        dist[0] = 0;
        while (!st.isEmpty()) {
            int node = st.peek();
            st.pop();
            if (dist[node] != (int)(1e9)) {
                for (int i = 0; i < adj.get(node).size(); i++) {
                    int v = adj.get(node).get(i).first;
                    int wt = adj.get(node).get(i).second;
                    if (dist[node] + wt < dist[v]) {
                        dist[v] = dist[node] + wt;
                    }
                }
            }
        }

        return dist[N - 1];
    }
}



