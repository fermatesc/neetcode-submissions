class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            k = ''.join(sorted(s))
            if k not in anagrams:
                anagrams[k] = [s]
            else:
                anagrams[k].append(s)

        return list(anagrams.values())