class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for string in strs:
            sort_str = ''.join(sorted(string))
            if sort_str in groups:
                groups[sort_str].append(string)
            else:
                groups[sort_str] = [string]

        return list(groups.values())