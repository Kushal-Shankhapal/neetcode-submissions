class Solution(object):
    def groupAnagrams(self, strs):

        index_map = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in index_map.keys():
                index_map[sorted_word].append(word)
            else:
                index_map[sorted_word] = [word]

        return list(index_map.values())