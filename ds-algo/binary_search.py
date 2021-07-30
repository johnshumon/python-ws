"""Binary search module"""

from typing import List


class Solution:
    """Solution class"""

    def search(self, nums: List[int], target: int) -> int:
        """Search function. returns the index of the
        target element if found otherwise -1.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return -1


def main():
    solution = Solution()
    bs_result = solution.search([-1, 0, 3, 5, 9, 12], 2)
    print("bs_result: ", bs_result)


if __name__ == "__main__":
    main()
