
class LRUCache {
    private Map<Integer, Node> cache;
    private int cap;

    private Node left;
    private Node right;


    public LRUCache(int capacity) {
        this.cap = capacity;
        cache = new HashMap<>();

        this.left = new Node(0,0);
        this.right = new Node(0,0);
        this.left.next = this.right;
        this.right.prev = this.left; 
    }
    
    public int get(int key) {
        if (cache.containsKey(key)){
            remove(cache.get(key));
            insert(cache.get(key));
            return cache.get(key).val;
        }   
        else{
            return -1;
        }
        
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)){
            remove(cache.get(key));
        }
        cache.put(key, new Node (key, value));
        insert(cache.get(key));

        if (cache.size() > this.cap){
            Node lru = this.left.next;
            remove(lru);
            cache.remove(lru.key);

        }
    }

    public void remove(Node node){
        Node prev = node.prev;
        Node nxt = node.next;
        prev.next = nxt;
        nxt.prev = prev;
    }

    public void insert(Node node){
        Node prev = this.right.prev;
        Node nxt = this.right;

        prev.next = node;
        nxt.prev = node;

        node.prev = prev;
        node.next = nxt;
    }

    private class Node {
        private int key;
        private int val;

        Node prev;
        Node next;

        public Node(int key, int value){
            this.key = key;
            this.val = value;    
        }
    }
}




/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
