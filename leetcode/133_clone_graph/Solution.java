/*
  CS Problems
  Leetcode
  133. Clone Graph
 */


import java.util.HashMap;

// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}

class Solution {
    private HashMap<Integer, Node> nodes = new HashMap<>();

    public Node cloneGraph(Node node) {
        // check for empty graph case
        if(node == null) {
            return null;
        }
        // check if node has already been cloned, if so return cloned node
        if(nodes.containsKey(node.val)) {
            return nodes.get(node.val);
        }

        // clone current node
        Node cloneNode = new Node(node.val);
        nodes.put(node.val, cloneNode);
        for(Node neighbor: node.neighbors) {
            // recursively clone neighbor nodes
            cloneNode.neighbors.add(cloneGraph(neighbor));
        }
        return cloneNode;
    }
}