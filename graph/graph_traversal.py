from collections import deque
class Graph:
    def __init__(self):
        num_nodes, num_edges = map(int, input().split())
        self.bidirected= int(input('양방향 여부 (1:양방향, 0:단방향) : '))
        self.graph = [[] for _ in range(num_nodes+1)]
        for _ in range(num_edges):
            u, v = map(int, input().split())
            self.graph[u].append(v)
            if self.bidirected:
                self.graph[v].append(u)

        self.visited = []

    def dfs(self, node):
        print(node, end=' ')
        self.visited.append(node)
        for adj_node in self.graph[node]:
            if adj_node not in self.visited:
                self.dfs(adj_node)

    def bfs(self, start):
        visited = []
        queue = deque()
        #시작 노드에 대해 작업
        queue.append(start)
        visited.append(start)
        print(start, end = ' ')
        # 다음에 방문할 노드 찾아서 처리
        # (방문한 적이 없는 인접 노드를 찾을 노드)
        while queue:
            prev_node = queue.popleft()
            for node in sorted(self.graph[prev_node]):
                if node not in visited:
                    queue.append(node)
                    visited.append(node)
                    print(node, end=' ')

        
if __name__ == "__main__":
    g = Graph()
    start = int(input("시작 노드 번호 : "))
    g.dfs(start)
    print()
    g.bfs(start)