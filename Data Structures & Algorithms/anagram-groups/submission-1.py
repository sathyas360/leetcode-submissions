class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_anagrams = {}
        for string in strs:
            sort_str = "".join(sorted(string))
            if sort_str not in dict_anagrams:
                dict_anagrams[sort_str] = [string]
            else:
                dict_anagrams[sort_str].append(string)
        grp_anagrams = []
        for key in dict_anagrams:
            grp_anagrams.append(dict_anagrams[key])
        return grp_anagrams