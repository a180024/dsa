class Solution:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()

        def combinations(temp, curSum, index):
            if curSum == target:
                res.append(temp)
                return
            if index == len(candidates):
                return
            for i in range(index, len(candidates)):  # ensure only unique combinations
                if curSum + candidates[i] <= target:
                    combinations(temp + [candidates[i]], curSum + candidates[i], i)
                else:
                    break

        combinations([], 0, 0)
        return res


sol = Solution()
print(sol.combinationSum([2, 3, 6, 7], 7))
