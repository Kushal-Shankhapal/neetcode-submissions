class Solution(object):
    def groupAnagrams(self, strs):

        index_map = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            index_map[sorted_word].append(word)

        return list(index_map.values())