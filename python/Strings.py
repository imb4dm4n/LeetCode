'''
字符串相关算法
'''
from typing import List
from typing import Optional
from unittest   import *
import unittest
import collections

class Solution:
    '''
    # https://leetcode.com/problems/longest-palindrome/
    # 409. Longest Palindrome
    问题: 输入一个区分大小写的字符串, 返回由这些字符能构成的最长回文长度. ie : 输入 abccccdd 返回 7, 最长回文dccaccd
    思路1: 本质就是求有多少个能成对的字符, 若还有单个字符, 则额外加1.
    用一个dict保存每个字符出现个数, 再一次遍历, 统计成对的个数. 无法通过边界测试: ccc
    边界测试: ccc; 
    思路2: 需要把使用过的字符移出来. 
    Runtime: 110 ms, faster than 5.58% of Python3 online submissions for Longest Palindrome.
    Memory Usage: 13.9 MB, less than 66.55% of Python3 online submissions for Longest Palindrome.
    '''
    def longestPalindrome(self, s: str) -> int:
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)
        # 思路2:
        l_tmp           =   list(s)
        total           =   0
        has_single      =   False
        while l_tmp.__len__() > 0:
            c       =   l_tmp.pop()
            if c in l_tmp:
                total   += 2
                l_tmp.remove(c)
                # print(l_tmp)
                continue
            else:
                has_single  =   True
        # print(l_tmp)
        if has_single:
            total       +=  1
        return total

        # 思路1: 无法通过边界测试: ccc
        s_dict          =   {}
        total           =   0   # 返回的个数
        has_single      =   False# 最后是否有单个字符
        for c in s:
            if not s_dict.get(c):
                s_dict[c]   =   1
            else:
                s_dict[c]   +=  1
        
        for c, count in s_dict.items():
            if count > 1:
                total       +=  count // 2 * 2
            elif count == 1:
                has_single  =   True
        
        if has_single:
            total   +=  1
        return total

    '''
    # https://leetcode.com/problems/longest-substring-without-repeating-characters/
    # 3. Longest Substring Without Repeating Characters
    问题: 输入一个字符串, 返回最长不包含重复字符的子串长度
    思路1: 用longest 保存最长子串长度, substr 保存构造的子串.
    当遇到重复字符时, 从 substr 下一个非重复字符开始构造新的 substr,
    更新 longest 或维持原始值
    Runtime: 64 ms, faster than 93.60% of Python3 online submissions for Longest Substring Without Repeating Characters.
    Memory Usage: 14 MB, less than 49.66% of Python3 online submissions for Longest Substring Without Repeating Characters.
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest         =   0
        substr          =   ''
        for i in range(s.__len__()):
            c           =   s[i]    # 取出当前字符
            # print("substr = " + substr)

            if substr.find(c) > -1:
                # 存在重复子串, 更新构造最新子串起始偏移
                substr  =   substr[substr.find(c)+1:]
                substr  +=  c
                longest =   longest if longest > substr.__len__() else substr.__len__()
                continue

            # substr 不存在重复子串
            substr      +=  c
            longest     =   longest =   longest if longest > substr.__len__() else substr.__len__()
        
        return      longest

# class testit(unittest.TestCase):
#     def test_lengthOfLongestSubstring(self):
solution        =   Solution()
# 409. Longest Palindrome
ret             =   solution.longestPalindrome("ccc")
print(ret)
ret             =   solution.longestPalindrome("abccccdd")
print(ret)
exit(0)
# 3. Longest Substring Without Repeating Characters
ret             =   solution.lengthOfLongestSubstring("abcabcbb")
print(ret)
ret             =   solution.lengthOfLongestSubstring("bbbbb")
print(ret)
ret             =   solution.lengthOfLongestSubstring("pwwkew")
print(ret)
ret             =   solution.lengthOfLongestSubstring("aab")
print(ret)
