
class Graph {
public:
    Graph(int n, vector<vector<int>>& edges) {
        // Initialize the adjacency list and edge costs
        adj.resize(n);
        cost.resize(n, vector<int>(n, -1));
        for (auto& e : edges) {
            int from = e[0], to = e[1], c = e[2];
            adj[from].push_back(to);
            cost[from][to] = c;
        }
    }
    
    void addEdge(const vector<int>& edge) {
        int from = edge[0], to = edge[1], c = edge[2];
        adj[from].push_back(to);
        cost[from][to] = c;
    }
    
    int shortestPath(int node1, int node2) {
        vector<int> dist(adj.size(), numeric_limits<int>::max());
        dist[node1] = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, node1});
        while (!pq.empty()) {
            int d = pq.top().first;
            int node = pq.top().second;
            pq.pop();
            if (d > dist[node]) {
                continue;
            }
            for (int neighbor : adj[node]) {
                if (cost[node][neighbor] != -1 && dist[node] + cost[node][neighbor] < dist[neighbor]) {
                    dist[neighbor] = dist[node] + cost[node][neighbor];
                    pq.push({dist[neighbor], neighbor});
                }
            }
        }
        return dist[node2] == numeric_limits<int>::max() ? -1 : dist[node2];
    }
    
private:
    vector<vector<int>> adj;
    vector<vector<int>> cost;
};

/**
 * Your Graph object will be instantiated and called as such:
 * Graph* obj = new Graph(n, edges);
 * obj->addEdge(edge);
 * int param_2 = obj->shortestPath(node1,node2);
 */