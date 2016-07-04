#Uses python3

import sys


def explore(adj, x, visited):
    #write your code here
    visited[x] = True
    for each in adj[x]:
        if not visited[each]:
            explore(adj, each, visited)

def number_of_components(adj):
    result = 0
    #write your code here
    visited = [False] * len(adj)
    for i,each in enumerate(visited):
        if not each:
            result +=1
            explore(adj, i, visited)
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
