class Solution:

    def encode(self, strs: List[str]) -> str:
        return "\n".join(strs) if strs else "kwasaksipasapugal"
    def decode(self, s: str) -> List[str]:
        if s != "kwasaksipasapugal":
            return s.split("\n")
        return []
        