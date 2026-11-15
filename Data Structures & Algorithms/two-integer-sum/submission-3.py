class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = sorted((n,i) for i,n in enumerate(nums))
        i, j = 0, len(pairs)-1
        while i<j:
            if pairs[i][0]+pairs[j][0]==target:
                return sorted([pairs[i][1],pairs[j][1]])
            elif pairs[i][0]+pairs[j][0]<target:
                i+=1
            else:
                j-=1