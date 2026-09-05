class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []

        for log in logs:
            parts = log.split()

            if parts[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits