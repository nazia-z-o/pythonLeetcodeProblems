class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        sumMN = mean * (m + n)
        totalM = sum(rolls)
        sumN = sumMN - totalM
        divN = int(sumN / n)
        rN = sumN % n
        if divN > 6 or divN <= 0:
            return []
        elif divN == 6 and rN > 0:
            return []
        result = [divN] * (n - rN)
        result.extend([divN + 1] * rN)
        return result
