class TimeMap:

    def __init__(self):
        self.dict = defaultdict(dict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append([value,timestamp])
        
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        
        l = 0 
        r = len(self.dict[key])-1
        while l<=r:
            mid = (l+r)//2
            if self.dict[key][mid][1] == timestamp:
                return self.dict[key][mid][0]
            elif self.dict[key][mid][1] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        return self.dict[key][r][0] if self.dict[key][r][1]<=timestamp else ""
            # for i in sorted(self.dict[key].keys()):
            #     if i <= timestamp:
            #         temp = i
            # if temp is None:
            #     return ""
            # else:
            #     return self.dict[key][temp]
        return self.dict[key][timestamp]
                
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)