- graph -> linked list -> tree have common operations

* adjancency matrix: 2d array, O(V^2) space
* O(1) to check if there is an edge between 2 nodes
* iterate over all edges, O(V^2)
* O(1) to add/remove an edge
* to remove an vertex, remove the row and column of that vertex, O(V^2)

  ```python
  [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0]
  ]
  ```

* adjancency list: array of linked lists, O(V+E) space
* O(V+E) to iterate over all edges
* fast to add/remove edges O(|E|)
* to check if there is an edge between 2 nodes, O(|V|)
* To remove vertex, remove all edges to that vertex, then remove the vertex itself, O(|V| + |E|)

  ```python
  {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
  }
  ```
