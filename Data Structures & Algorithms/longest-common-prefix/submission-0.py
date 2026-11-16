class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(min(strs,key=len))
        for j in range(min_len):
            for i in range(1,len(strs)):
                if strs[0][j]!=strs[i][j]:
                    return strs[0][:j]
        return strs[0][:min_len]