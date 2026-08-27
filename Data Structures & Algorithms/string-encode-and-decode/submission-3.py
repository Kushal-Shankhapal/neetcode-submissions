class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "\0"
        return "erf23443fd".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "\0":
            return []
        return s.split("erf23443fd")