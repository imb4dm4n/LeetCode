'''
字符串相关算法
'''
from typing import List
from typing import Optional
from unittest   import *
import unittest
import collections
from xml.sax.handler import all_properties

set('zxc').intersection(set('cxz'))


class Solution:
    '''
- https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
- 645. 1239. Maximum Length of a Concatenated String with Unique Characters(Medium)
- 问题:  
输入一组字符串数组, 找出包含唯一字符的子序列 能够构成的最长字符串的字符个数.  子序列由一组数据在不改变顺序的前提下, 删除一些或不删除元素. 如输入 arr = ["un","iq","ue"], 得到4. 
因为可以构成 un; iq; ue; uniq; ique; 这几个子序列, 最长长度为4
-  
- 思路: 
遍历O(N^2)次字符串, 用一个栈保存唯一的序列,一个max_len保存结果, 入栈一个元素, 更新结果max_len, 若存在重复元素, 把最短的元素出栈.
    '''
    def maxLength(self, arr: List[str]) -> int:
        max_len         =   0
        unique_strs     =   []
        
        for i, s in enumerate(arr):
            if set(s).__len__() != len(s):
                continue
            unique_strs.append(set(s))
        
        # for i, t in enumerate(unique_strs):
            tmp     =   [unique_strs[0]]
            cur_len =   0
            print(f"tmp is {tmp}")
            for j in range(1, unique_strs.__len__()-1):
                s1  =   unique_strs[j]
                print(f"work on {s1}")
                should_append   =   True
                # tmp.append(s1)
                for i1, t1 in enumerate(tmp):
                    cur_len +=  len(t1)
                    if t1.intersection( s1):
                        print(f"conflict {t1} {s1}")
                        # 存在重复,移除最短的那个
                        if len(t1) >= len(s1):
                            should_append   =   False
                            print(f"{should_append} not append {s1}")
                            break
                        else:
                            cur_len -=  len(t1)
                            x=tmp.pop(i1)
                            print(f"pop {x}")
                            break
                print(f"{should_append} append {s1}")
                if should_append:
                    # print(f"{should_append} append {s1}")
                    cur_len += len(s1)
                    tmp.append(s1)
            if cur_len > max_len:
                max_len =   cur_len
        
        return max_len
        
        for i, s in enumerate(arr):
            if set(s).__len__() != len(s):
                continue
            tmp     =   [set(s)]
            for j in range(i+1, arr.__len__()):
                s1  =   arr[j]
                s1_ =   set(s1)
                if s1_.__len__() != len(s1):
                    continue
                tmp.append(s1_)
                tmp_s   =   "".join(tmp)
                if set(tmp_s).__len__()   != len(tmp_s):
                    # 存在重复元素, 移除最小的那个
                    for i1, t in enumerate(tmp):
                        if t & s1_:
                            tmp.pop(i1)
                            break
                # 计算最长的
                tmp_s   =   "".join(tmp)
                if len(tmp_s) > max_len:
                    max_len =   tmp_s
        return max_len
                    # tmp.pop(-1)
    '''
    # 76. Minimum Window Substring (hard)
    # https://leetcode.com/problems/minimum-window-substring/
    # tag: window
    问题: 输入字符串 s 和 t, 找出s中的一小段子字符串, 包括了 t 的所有字母(包括重复的字母), 若不存在, 返回空.
    (s的长度可能小于t)
    思路: 包括 t 的所有字符, 那么窗口大小至少是 t 的长度. 从 0 偏移开始构建窗口.
    构造t的集合, 每个窗口的集合, 求交集. 但是窗口长度可能会大于t的长度. 因此从0开始遍历.

    LeetCode思路: 滑动窗口. 用 left 和 right 指针表示一个窗口的左右区间.  https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems
    a.当 left 和 right 构成的窗口无法满足条件时, 把 right 增大, 直到找到一个满足的窗口.
    b.当 left 和 right 构成的窗口满足条件时. 把 left 增大, 判断窗口是否满足, 若满足则继续缩小窗口, 否则回到步骤a
    c. 遍历直到结束
    类似投票算法? 
    Runtime: 215 ms, faster than 56.25% of Python3 online submissions for Minimum Window Substring.
    Memory Usage: 14.8 MB, less than 36.77% of Python3 online submissions for Minimum Window Substring.
    '''
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        # store ascii chrarcter counts. 不用 collection.Counter 是因为 dict 更慢
        ch_hash     =   [0] * 128

        for c in t:
            # 统计丢失的字符个数/ 初始化需要寻找的字符的个数
            ch_hash[ord(c)]  +=  1
        
        left            =   0   # 窗口起始坐标
        right           =   0   # 窗口结束坐标
        begin           =   0   # 最新满足条件的窗口起始坐标
        min_size        =   0x1fffff # 最小的窗口大小
        missing         =   t.__len__() # 丢失\ 需要寻找的字符个数
        
        while right < s.__len__():
            # 当前字符在 需要寻找的字符中, 减少需要寻找的字符个数
            if ch_hash[ord(s[right])] > 0:
                missing          -=  1
            
            # 无论当前字符是否能够在 t 中找到, 都减1, 如果是不存在的, 则对应字符计数器为负数
            # 让丢失的字符个数减1
            ch_hash[ord(s[right])]   -=  1
            right        +=  1  # 移动窗口

            # 若所有字符都找到了, 开始尝试缩小窗口
            while missing    ==  0:
                # calculate the window size to find the smallest window.
                if right - left < min_size:
                    min_size    =   right   -   left
                    begin       =   left
                
                # 从窗口最左边开始, 使得窗口无效. 字符是想要的, 则计数器会大于0, 若不是想要的, 会变成0
                # 让丢失的字符个数加1
                ch_hash[ord(s[left])]    +=  1
                # 若当前字符 丢失个数 大于0, 说明是想要的字符, 前一步已经让它再次作为丢失的字符了
                if ch_hash[ord(s[left])] > 0:
                    missing  +=  1      # 丢失的字符个数 +1
                left        +=  1       # 缩小窗口
        
        if min_size != 0x1fffff:
            return s[begin:begin+min_size]
        return ''


    '''
    # 1832. Check if the Sentence Is Pangram (easy)
    # https://leetcode.com/problems/check-if-the-sentence-is-pangram/
    问题: 输入一个字符串, 若所有的字符覆盖了26个字母, 则返回 true ,否则返回false
    思路1: 用集合保存唯一的字符, 遍历一遍字符串, 把每个字符加入到集合中, 若集合的长度为26, 则提前返回.
    遍历结束, 集合长度不为 26, 则返回false.
    Runtime: 55 ms, faster than 54.97% of Python3 online submissions for Check if the Sentence Is Pangram.
    Memory Usage: 13.9 MB, less than 11.66% of Python3 online submissions for Check if the Sentence Is Pangram.
    '''
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet    =   set()
        for c in sentence:
            if alphabet.__len__() == 26:
                return True
            alphabet.add(c)
        
        if alphabet.__len__() == 26:
            return True
        return False

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
# exit(0)
# 3. Longest Substring Without Repeating Characters
ret             =   solution.lengthOfLongestSubstring("abcabcbb")
print(ret)
ret             =   solution.lengthOfLongestSubstring("bbbbb")
print(ret)
ret             =   solution.lengthOfLongestSubstring("pwwkew")
print(ret)
ret             =   solution.lengthOfLongestSubstring("aab")
print(ret)
