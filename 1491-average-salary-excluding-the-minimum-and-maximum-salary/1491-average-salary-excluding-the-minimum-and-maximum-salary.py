class Solution:
    def average(self, salary: List[int]) -> float:
        result = sorted(salary)
        return float(format(((sum(result[1:len(result)-1]))/(len(result)-2)),".5f"))