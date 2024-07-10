class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # own but need improve
        need = 0
        for s in logs:
            if s == ("../"):
                if need == 0:
                    continue
                need -= 1
                continue
            elif s == ("./"):
                continue
            elif s[-1] == ("/"):
                need += 1
        return need
