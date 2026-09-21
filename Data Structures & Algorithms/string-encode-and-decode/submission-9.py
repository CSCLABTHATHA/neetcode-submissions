class Solution:

    def encode(self, strs: List[str]) -> str:
        return "\n".join(strs) if strs else "\b"
    def decode(self, s: str) -> List[str]:
        if s != "\b":
            return s.split("\n")
        return []
        