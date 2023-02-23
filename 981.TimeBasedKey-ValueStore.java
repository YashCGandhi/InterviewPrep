class Pair{
    int timestamp;
    String value;
    public Pair(String value, int timestamp){
        this.value = value;
        this.timestamp = timestamp;
    }
}
class TimeMap {
    HashMap<String, List<Pair>> map;
    public TimeMap() {
        map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        if(!map.containsKey(key)){
            map.put(key, new ArrayList<>());
        }
        map.get(key).add(new Pair(value, timestamp));
    }
    
    public String get(String key, int timestamp) {
        if(!map.containsKey(key)){
            return "";
        }else{
            return binarySearch(map.get(key), timestamp);
        }
    }

    public String binarySearch(List<Pair> arr, int timestamp){
        int low = 0, high = arr.size() - 1;
        String res = "";

        while (low <= high){
            int mid = (low + high) / 2;
            if(arr.get(mid).timestamp <= timestamp){
                res = arr.get(mid).value;
                low = mid + 1;
            }
            else{
                high = mid - 1;
            }
        }
        return res;
    }
}
