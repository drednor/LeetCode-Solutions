class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        memo = defaultdict(list)
        for path in paths:
            li = path.split(" ")
            folder = li[0]
            for x in li[1:]:
                temp = x.split(".txt")
                file = temp[0]
                content = temp[1]
                memo[content].append(folder+"/"+file+".txt")
        res = []
        for v in memo.values():
            if len(v)>1:
                res.append(v)
        return res
            
            
            
            