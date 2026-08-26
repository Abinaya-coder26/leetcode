class Solution:
    def combinationSum(self, candidates, target):
        ans = []

        def dfs(start, path, remain):
            if remain == 0:
                ans.append(path[:])
                return

            if remain < 0:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                if num > remain:
                    continue

                path.append(num)

                dfs(i, path, remain - num)

                path.pop()

        dfs(0, [], target)

        return ans