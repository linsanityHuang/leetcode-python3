#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# https://leetcode-cn.com/problems/search-insert-position/description/
#
# algorithms
# Easy (42.18%)
# Total Accepted:    26.7K
# Total Submissions: 63.3K
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素。
#
# 示例 1:
#
# 输入: [1,3,5,6], 5
# 输出: 2
#
#
# 示例 2:
#
# 输入: [1,3,5,6], 2
# 输出: 1
#
#
# 示例 3:
#
# 输入: [1,3,5,6], 7
# 输出: 4
#
#
# 示例 4:
#
# 输入: [1,3,5,6], 0
# 输出: 0
#
#
#


class Solution:
    
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        
        if not nums:
            return 0
        else:
            low = 0
            high = n - 1
            
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif mid < n - 1 and nums[mid] < target < nums[mid + 1]:
                    return mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
            if high < 0:
                return 0
            if low > n - 1:
                return n
        

if __name__ == '__main__':
    a = [1, 3, 5, 6]
    s = Solution()
    print(s.searchInsert(a, 5))
    print(s.searchInsert(a, 2))
    print(s.searchInsert(a, 7))
    print(s.searchInsert(a, 0))
    
    # nums = [1, 3, 5, 6]
    #
    # s = Solution()
    # print(s.searchInsert(nums, 2))
    # #
    # assert s.searchInsert(nums, 5) == 2
    #
    # assert s.searchInsert(nums, 2) == 1
    #
    # assert s.searchInsert(nums, 7) == 4
    #
    # assert s.searchInsert(nums, 0) == 0
    #
    # assert s.searchInsert([1], 1) == 0
