class Solution:
    def permute(self, nums):
        result = []

        def backtrack(path, used):
            # If permutation is complete
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    # Choose
                    path.append(nums[i])
                    used[i] = True

                    # Explore
                    backtrack(path, used)

                    # Undo choice
                    path.pop()
                    used[i] = False

        backtrack([], [False] * len(nums))
        return result