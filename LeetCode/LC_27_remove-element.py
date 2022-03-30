class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if val in nums:  # check if val in nums to handle an exception
            # get the index of the last occurence of val in nums
            nums.sort(reverse=True)
            i_end = len(nums) - 1 - nums.index(val)

            # get the index of the first occurence of val in nums
            nums.sort()
            i_start = nums.index(val)

            # delete all vals in nums in the sorted list
            del nums[i_start : i_end + 1]

        return len(nums)
