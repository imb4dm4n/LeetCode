'''
字符串相关算法
'''
from typing import List
from typing import Optional
from unittest   import *
import unittest

class Solution:
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
ret             =   solution.lengthOfLongestSubstring("abcabcbb")
print(ret)
ret             =   solution.lengthOfLongestSubstring("bbbbb")
print(ret)
ret             =   solution.lengthOfLongestSubstring("pwwkew")
print(ret)
ret             =   solution.lengthOfLongestSubstring("aab")
print(ret)
