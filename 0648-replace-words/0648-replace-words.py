class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        ans = []

        for word in words:
            root = word

            for d in dictionary:
                if word.startswith(d) and len(d) < len(root):
                    root = d

            ans.append(root)

        return " ".join(ans)