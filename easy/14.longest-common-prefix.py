#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (31.40%)
# Total Accepted:    46K
# Total Submissions: 146.4K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#


class Solution:
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 or "" in strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        ordered_str = sorted(strs, key=len)
        first_item = ordered_str[0]
        i = 0
        for _ in range(len(first_item)):
            for item in ordered_str[1:]:
                if first_item[i] != item[i]:
                    break
            else:
                i += 1
        return first_item[0: i]


if __name__ == '__main__':
    s = Solution()
    # strs = ["flower", "flow", "flight"]
    # strs = [""]
    # strs = ["a", "b"]
    # strs = ["a", "a", "b"]
    # strs = ["aa", "a"]
    strs = ["a"]
    print(repr(s.longestCommonPrefix(strs)))
