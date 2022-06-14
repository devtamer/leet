# remeber cache LRU works like LIFO and should remove the index that has been accessed least 
# recently, there will be "put" operations to store in cache and "get" used to access data
# stored in cache, we'll use a hashmap to instantly look up the value of every key when "get"
# operation is needed

