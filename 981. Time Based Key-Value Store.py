class TimeMap(object):

    def __init__(self):
      self.m = {}
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.m:
          self.m[key] = []
        self.m[key].append((value, timestamp)) 

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.m:
          return ""
        v = self.m[key]
        for val, times in reversed(v):
          if timestamp < times:
            pass
          else:
            return val
        else:
          return ""

# Your TimeMap object will be instantiated and called as such:
timeMap = TimeMap();
timeMap.set("foo", "bar", 1)  # store the key "foo" and value "bar" along with timestamp = 1.
print(timeMap.get("foo", 1))         # return "bar"
print(timeMap.get("foo", 3))         # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 print(is "bar".
timeMap.set("foo", "bar2", 4); # store the key "foo" and value "bar2" along with timestamp = 4.
print(timeMap.get("foo", 4))         # return "bar2"
print(timeMap.get("foo", 5))         # return "bar2"