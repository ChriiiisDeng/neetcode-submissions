class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(idx, path, current_sum):
            if current_sum == target:
                res.append(path[:])
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if current_sum + candidates[i] > target:
                    break
                path.append(candidates[i])
                dfs(i + 1, path, current_sum + candidates[i])
                path.pop()

        dfs(0, [], 0)

        return res