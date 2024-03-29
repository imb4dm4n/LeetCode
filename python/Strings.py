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
from collections import *


class Solution:
    '''
- replace with url
- replace with problem title
- 问题:  
replace with problem description
- 思路:
replace with your idea.
    '''
    '''
- https://leetcode.com/problems/optimal-partition-of-string/
- 2405. Optimal Partition of String (Medium)
- 问题:  双指针
输入一个字符串, 返回所有子串组合中, 组合个数是最少的. 其中每个子串包含的字符是唯一的
- 思路:
子串个数最少, 需要每个唯一的字符串尽可能的长一些. 
    '''
    def partitionString(self, s: str) -> int:
        res     =   []
        s   =   list(s)
        s=sorted(s)
        while len(s) > 0 :
            tmp = ''
            slow,fast =0,0
            l   =   len(s)
            while fast < l:
                if slow == 0:
                    tmp += s[slow]
                    slow += 1
                    fast += 1
                    continue
                if tmp[slow]!= s[fast]:
                    tmp += s[fast]
                    slow += 1
                fast += 1
            res.append(tmp)
        return len(res)
                # else:
                #     fast += 1

        pass
    '''
- https://leetcode.com/problems/permutation-in-string/
- 567. Permutation in String (Medium)
- 问题:  
输入 s1 问 s2 是否包含 s1 的一个变种序列.
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
- 思路: 滑动窗口
need 窗口是 s1 的字符计数器, missing 当丢失的个数为0时, 判断窗口大小 right - left 是否为目标的长度.
Beats 75.1%
    '''
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        判断 s2 是否包含 s1 的变种序列
        '''
        missing     =   len(s1)
        l_s1        =   missing
        need        =   defaultdict(int)    # 保存查找的目标
        left,right  = 0,0
        
        for c in s1 :
            need[c]     +=  1
        
        while right < len(s2):
            c   =   s2[right]
            right   +=  1

            if need[c] > 0:     # 找到一个目标 则减小丢失数
                missing -=  1
            need[c] -=  1

            while missing == 0: # 丢失数为0时 可以缩小窗口
                if right - left == l_s1:    # 窗口大小正好是目标字符的长度
                    return True
                d   =   s2[left]
                need[d]  +=  1
                if need[d] > 0: # 若是目标字符被删除了, 则增加丢失数
                    missing +=  1
                left    +=  1

        return False
            
    '''
- https://leetcode.com/problems/find-all-anagrams-in-a-string/
- 438. Find All Anagrams in a String (Medium)
- 问题:  
输入两个字符串s,p; 输出 所有 s 中 p的 anagram 的起始索引列表;
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
- 思路: 滑动窗口
窗口大小是字符串的长度, 当窗口中的字符不满足目标时 missing > 0, 增大窗口;
当窗口字符串满足目标时, 检查窗口字符串的个数是否和目标一致, 
    一致则把left索引加到结果
    不一致则增大 窗口, 直至missing 个数 > 0 break 出去
- 思路 滑动窗口
窗口是需要查找的目标字符对应的计数器, missing 是总共需要的字符个数.
当 missing 大于0时增大窗口
Beats 63.42%
    '''
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p:
            return []
        
        left, right = 0, 0
        size    =   len(s)
        valid   =   0
        missing =   len(p)  # 丢失的字符个数
        need  =   defaultdict(int)
        window  =   defaultdict(int)
        res     =   []

        for c in p:
            need[c]   +=  1   # 初始化查找目标
        
        while right < size:
            c   =   s[right]
            right   +=  1
            if need[c] > 0:
                window
            
            
        return res
    
        left, right = 0, 0
        size    =   len(s)
        missing =   len(p)  # 丢失的字符个数
        window  =   defaultdict(int)
        res     =   []

        for c in p:
            window[c]   +=  1   # 初始化查找目标
        
        while right < size:
            # 当前字符在查找的目标中, 减少丢失数
            if window[s[right]] > 0:
                missing -=  1
            # 字符计数器减1
            window[s[right]]    -=  1

            # 没有丢失字符的时候, 开始寻找合适的窗口偏移
            while missing == 0:
                sum_c   =   sum(window.values())
                # 必须和为0 否则说明窗口内存在其他的字符
                if sum_c    ==  0:
                    res.append(left)
                c   =   s[left]
                left    +=  1       # 增大窗口
                window[c]   +=  1
                if window[c] > 0:
                    missing +=  1
            
            right   +=  1
        
        return res

            
    '''
- https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
- 3. Longest Substring Without Repeating Characters (Medium)
- 问题:  
输入一个字符串, 返回最长的那个子串.
- 思路: 滑动窗口
数组形式
窗口保存字符的个数. 遍历字符串, 累加字符计数器.     (Push + 1)
若当前字符的个数大于1个, 说明存在重复 开始缩小窗口.
取出窗口第一个字符 window[left], 缩小窗口 left += 1, 对应的窗口字符计数器 - 1 . (Pop - 1)
Beats 43.15%
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index  =   defaultdict(int)
        # char_index  =   [0] *   128
        longest     =   0
        left, right =   0,0

        while right < len(s):
            c       =   ord(s[right])
            right   +=  1
            char_index[c]   +=  1
            
            while char_index[c] > 1:
                d   =   ord(s[left])
                left    +=  1
                char_index[d]   -=  1
                
            longest =   max(longest,right   -   left)

        return longest
    '''
- https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
- 28. Find the Index of the First Occurrence in a String (Medium)
- 问题:  
输入 src 字符串, 找到 target 字符串第一次出现的位置返回. 即 strstr 函数.
- 思路:
不对, 这是双指针问题....
Beats 34.94%
正解是 KMP 算法
- tag 双指针
    '''
    def strStr(self, haystack: str, needle: str) -> int:
        # THIS is a joke for you.  Beats 90.82%
        return haystack.find(needle)
    
        slow, fast  =   0, 0
        n   =   len(haystack)
        m   =   len(needle)
        # 边界条件
        if m > n:
            return -1
        while fast < n:
            slow    =   0
            tmp     =   fast
            # print("* fast = {}".format(fast))
            while slow < m and fast < n and haystack[fast] == needle[slow]:
                fast    +=  1
                slow    +=  1
            if slow == m:
                return fast -   slow
            # print("[+]fastid={}   slowid={}  ".format(fast,  slow, ))
            # print("[-]fast={}   slow={}  ".format(haystack[fast],  needle[slow] ))
            fast    =  tmp + 1
        return -1
    
        target  =   collections.defaultdict(int)
        for c in needle:
            target[c]   +=  1
        want    =   len(needle)
        n       =   len(haystack)
        left, right, begin =0, 0, 0
        while right < n:
            if target[haystack[right]]:
                want    -=  1
            target[haystack[right]] -=  1
            while want  ==  0:
                pass
    '''
- https://leetcode.com/problems/zigzag-conversion/
- 6. Zigzag Conversion (Medium)
- 问题:  
输入一个字符串和行数n, 把它转为 n行拉链式 字符串, 按行范围结果. ie 
输入字符串 PAY PALISH IRING 和 行数3, 转为 3行 拉链式字符串.
P   A   H   N
A P L S I I G
Y   I   R
返回结果 PAHNAPLSIIGYIR 读作( PAHN APLSIIG YIR )
- 思路:
看起来需要一个二维数组, 然后替换里面的数据, 最后按行拼接成结果字符串.
一组 zigzag 存储 2n -2 个字符, 如3行, 得到一组存储 4个, 4行得到一组存6个.
一个 zigzag 有 n - 1 列.
输入 x 长的字符串, 需要 (x // (2n -2) + 1) * (n-1) 的列数? 
P    
A P  
Y  
    '''
    def convert(self, s: str, numRows: int) -> str:
        n           =   numRows
        column      =   (len(s) // (2*n -2) + 1) * (n-1)
        matrix      =   [''] 
        pass

    '''
- https://leetcode.com/problems/verifying-an-alien-dictionary/
- 953. Verifying an Alien Dictionary (Easy)
- 问题:  
输入一个外星人字典的字母顺序 和 一组 外星人的单词, 若单词组是按字符序列排序的, 则返回 true. 类似 strcmp 函数, 只是字符表不一样.
- 思路:
按照字典顺序, 生成每个字符的编号, 
考虑到如果是顺序的, 那么两两单词之间的关系, 一定也是排序的. 因此可以两两单词进行检查.
把每个单词, 拆分重新拼接, 然后验证新生成的单词组, 是否按顺序排序.
ie: order = "worldabcefghijkmnpqstuvxyz", ["word","world","row"] => 生成 'wwr', 'ooo', 'rrw', 'dl ',
由于 l 是小于 d 的, 因此不符合, 返回 false
- 注意:
    空字符需要做初始化, 否则取不到对应的 值

Beats 93.63%
    '''
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic_alphabet    =   {}
        # 注意
        dic_alphabet['']=   -1

        for i, c in enumerate(order):
            dic_alphabet[c] =   i
        
        def alien_strcmp(word1:str, word2:str):
            '''
            对比两个外星单词是否排序, 排序则返回 true
            '''
            c1  =   word1[0] if len(word1) else ''
            c2  =   word2[0] if len(word2) else ''
            # print("c1={} c2={}".format(c1, c2))
            if not c1 and not c2:
                return True
            # 若两个字符不同, 且小于, 则说明顺序是ok的
            if c1 != c2 and dic_alphabet[c1] <= dic_alphabet[c2]:
                return True
            return dic_alphabet[c1] <= dic_alphabet[c2] and \
                alien_strcmp(word1[1:], word2[1:])

        for i in range(len(words)-1):
            if not alien_strcmp(
                words[i],
                words[i+1],
                ):
                return False
        return True

    
    '''
- https://leetcode.com/problems/greatest-common-divisor-of-strings/
- 1071. Greatest Common Divisor of Strings (Easy)
- 问题:  
输入两个字符串, 寻找最大能够把他们两个都整除的字符串. gcd 算法.
s1='ABABAB' s2='AB' res='AB'
- 思路:
找出短的字符串的最大 common divisor 即可. 
由于字符串是由 t 拼接得到的, 因此只需要从一半的位置开始寻找即可.
从第一个字符遍历到字符串个数的一半, 
Beats 43.70%
- 他人思路
Beats 81.93%
    '''
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 别人思路
        if not str1 or not str2:
            return str1 if str1 else str2
        elif len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        elif str1[: len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2) :], str2)
        else:
            return ''

        # 自己的思路
        short   =   ''
        long    =   ''
        gcd     =   ''
        tmp     =   ''

        if len(str1) <= len(str2):
            short   =   str1
            long    =   str2
        else:
            long    =   str1
            short   =   str2
        half    =   len(short)//2
        len_short   =   len(short)
        len_long    =   len(long)
        for i,c in enumerate(short):
            if i == half:
                break
            tmp     +=  c
            n       =   len_short   //  len(tmp)
            m       =   len_long    //  len(tmp)
            if tmp*n == short and tmp*m == long:
                gcd = tmp
        x   =   len_long // len_short
        if x*short == long:
            gcd = short
        return gcd

    '''
- https://leetcode.com/problems/delete-columns-to-make-sorted/
- 944. Delete Columns to Make Sorted(easy)
- 问题:  
输入一组长度一样的单词, 把他们按行列出, 判断每一列是否在字母顺序上排序, 若不是, 则计数为需要删除一列.
返回需要删除多少列. 如输入以下单词, 输出1. (bca这一列不按顺序)
abc
bce
cae
- 思路:
遍历每个单词, 分别把他们加入对应的列. 然后对比 sorted 后的数组是否相同, 不同则返回值+1
Beats 30.53%
    '''
    def minDeletionSize(self, strs: List[str]) -> int:
        ret     =   0
        tmp     =   ['' for i in range(strs[0].__len__())]
        # print("tmp {}".format(tmp))
        for s in strs:
            for j,c in enumerate(s):
                tmp[j] += c
                
        for w in tmp:
            print("{} {}".format(w, "".join(sorted(w))))
            if w != "".join(sorted(w)):
                ret +=  1
        return  ret
    '''
- https://leetcode.com/problems/detect-capital/
- 520. Detect Capital(easy)
- 问题:  
输入一个单词, 判断它的大写是否用对了:
1.全是小写
2.全是大写
3.第一个字符是大写其余是小写
- 思路:
Beats 81.79%
    '''
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
        # 大写开头
        if len(word) > 1 and ord(word[0]) in range(ord('A'),ord('Z')+1):
            if ord(word[1]) in range(ord('A'),ord('Z')+1):
                return word == word.upper()
            return word[1:] == word[1:].lower()

        # 小写开头
        if len(word) > 1 and ord(word[0]) in range(ord('a'),ord('z')+1):
            # print(f"{word} {word.lower()}")
            return word == word.lower()
        
        return True
    '''
- https://leetcode.com/problems/is-subsequence/?envType=study-plan&id=level-1
- 2392. Is Subsequence(easy)
- 问题:  
输入 s 和 t 两个字符串, 判断 s 是不是 t 的子序列. 子序列是 目标字符串在不改变字符顺序的情况下, 删掉一些.
s =
"aaaaaa"
t =
"bbaaaa"    =》 False
- 思路:   
先判断字符串是不是相同.
遍历 s 的字符, 若和 t 的一个字符相同, 则移动下一个对比, 若 t 已经为空了
但是 s 非空, 那么不是子序列, 若 s 为空了则说明是子序列
    '''
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t :
            return True
        if not t:
            return False
        
        id_t    =   0
        for i, c in enumerate(s):
            # 注意下标是结束的前一个
            while t[id_t] != c and id_t < t.__len__()-1:
                id_t += 1
            if t[id_t]  ==  c:
                continue
            return False
        return True

    '''
- https://leetcode.com/problems/isomorphic-strings/?envType=study-plan&id=level-1
- 205. Isomorphic Strings(easy)
- 问题:  
判断两个字符串是否 Isomorphic 同构的: 即一个单词可以通过替换每个字母变成另一个单词,
注意, 字母出现的顺序不能变化, 一个字母只能映射成一个字母, 不能同时映射两个字母.
s = "foo", t = "bar" -> False ; s = "egg", t = "add" -> True ;  s = "paper", t = "title" -> True
- 思路:   
把s的每个字符映射到t. 若映射的 目标字符 已经在映射字典的 value 里了, 说明 存在重复的映射, 这时候不保存这个映射, 然后直接替换一个空的.
Beats 85.61%
    '''
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s.__len__ () != t.__len__ ():
            return  False
        map_word    =   {}
        s,t     =   list(s), list(t)
        for i in range(s.__len__()):
            # mapping every character
            if map_word.get(s[i]) is None and t[i] not in map_word.values():
                map_word[s[i]]  =   t[i]
                s[i]    =   t[i]
                continue
            s[i]    =   map_word.get(s[i])
        # print(s,t)
        return  s==t


    '''
- https://leetcode.com/problems/determine-if-two-strings-are-close/
- 1657. Determine if Two Strings Are Close(medium)
- 问题:  
通过两个操作判断连个单词是否相近:
    1. 随意交互两个字母的位置, 如 abc -> cbc
    2. 随意把出现的一个字母完全和另一个字母交换, 比如 aab -> bba
输入两个单词, 判断他们是否相近。 提示： 操作1 允许任意排序字母，操作2 允许任意修改字母出现频率
- 思路: 
先进行长度校验(不同长度肯定不能变化), 再进行字符校验(变化不能超出已有的字符).
其实本质就是, 验证输入的两个单词, 不同字符出现的频率列表, 是否一致. 
因为字母的顺序可以随意交换, 那么剩下的问题就是如何按照字母的个数, 变化成另一个单词了.
(类似洗牌变魔术?) 比如你有 3个A 和 1个K, 那么你是否可以通过以上规则, 得到 3个K和 1个A呢?
答案是肯定的, 本质是把A和K对应的 key 进行交换: {A:3 , K:1} => {K:3 , A:1}

Runtime: 210 ms, faster than 82.33% of Python3 online submissions for Determine if Two Strings Are Close.
Memory Usage: 15.4 MB, less than 16.87% of Python3 online submissions for Determine if Two Strings Are Close.
    '''
    def closeStrings(self, word1: str, word2: str) -> bool:
        # return False if word1.__len__() != word2.__len__() or set(word1) != set(word2) else sorted(collections.Counter(word1).values()) == sorted(collections.Counter(word2).values())
        if word1.__len__() != word2.__len__() or \
            set(word1) != set(word2):
            return False

        return sorted(collections.Counter(word1).values()) == sorted(collections.Counter(word2).values())
    
    
    '''
- https://leetcode.com/problems/reverse-words-in-a-string/
- 151. Reverse Words in a String(medium)
- 问题:  
输入一组单词, 翻转他们的顺序. 返回用一个空格间隔的结果
- 思路:
Runtime: 34 ms, faster than 94.31% of Python3 online submissions for Reverse Words in a String.
Memory Usage: 14.1 MB, less than 48.44% of Python3 online submissions for Reverse Words in a String.
    '''
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
        # li_s        =   s.split(" ")
        # ret         =   []
        # for word in li_s:
        #     if not word:
        #         continue
        #     ret.append(word)
        # ret.reverse()
        # return " ".join(ret)

    '''
- https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
- 1047. Remove All Adjacent Duplicates In String(easy)
- 问题:  
输入一个字符串, 把相邻且一样的字符移除, 若移除后, 还存在相邻又相同, 则继续移除, 直到结束.
- 思路: 
跟下面一题思路是一样的. 换一种吧.
用一个栈保存符合条件的字符列表.
遍历输入的每个字符, 和栈顶对比, 若相同, 则出栈,
否则入栈.
- 思路2:
手动模拟一个栈, 用 end 指针模拟栈顶
Runtime: 238 ms, faster than 29.33% of Python3 online submissions for Remove All Adjacent Duplicates In String.
Memory Usage: 14.7 MB, less than 86.70% of Python3 online submissions for Remove All Adjacent Duplicates In String.
    '''
    def removeDuplicates(self, s: str) -> str:
        end, a = -1, list(s)
        for c in a:
            if end >= 0 and a[end] == c:
                end -= 1
            else:
                end += 1
                a[end] = c
        return ''.join(a[: end + 1])
    '''
- https://leetcode.com/problems/make-the-string-great/
- 1544. Make The String Great(easy)
- 问题:  
输入一个字符串, 把它转为 好的 字符串. 不好的字符串是 相邻的两个字母是一样的, 但是大小写不同. 可以把他们删除.
注意: 删除后会拼接出新的字符串, 这时候可能会组合出新的 不好字符组.
- 思路: 
遍历索引, 当i和i+1 不好时, 删除他们, 在i>1的情况下, 把i-1,
继续操作新的字符串. 直到字符串为空 或 i 成为最后一个
Runtime: 79 ms, faster than 24.04% of Python3 online submissions for Make The String Great.
Memory Usage: 13.9 MB, less than 61.93% of Python3 online submissions for Make The String Great.
    '''
    def makeGood(self, s: str) -> str:
        if not s or s.__len__()==1:
            return s
        s   =   list(s)
        top =   0
        def same_char(c1, c2):
            return abs(ord(c1) - ord(c2)) == 32
        while top < s.__len__() -1:
            # print(f"top = {top}")
            if not same_char(s[top], s[top+1]):
                top     +=  1
                continue
            s.pop(top)
            s.pop(top)
            # print("pop {}".format(s.pop(top)))
            # print("pop {}".format(s.pop(top)))
            # s.pop(top)
            if top > 0:
                top -= 1
            
        return "".join(s)
    '''
- https://leetcode.com/problems/word-search-ii/
- 212. Word Search II(hard)
- 问题:  
输入一个字符矩阵 和 一组单词, 返回能够从矩阵中找出 相邻且能构成单词的列表. 相邻是水平和垂直相邻。
- 思路:
对每个单词都做一次查找. 把输入的单词作为一个集合, 遍历矩阵每个字符,
判断是否在集合内, 若在集合内, 则探测下一个字符(右边或下边)
    '''
    def contain_word(self, board: List[List[str]], words:set, x:int, y:int):
        '''
        :param      x       矩阵的坐标
        :param      y       矩阵的坐标
        '''
        if x == board[0].__len__() -1 and \
            y == board.__len__() - 1 and \
                len(words) != 0 and\
                board[x][y] not in words:
                return False
        
        if board[x][y] in words:
            tmp     =   board[x][y]
            words.remove(tmp)
            if words.__len__() == 0:
                return  True
            # continue search till words is empty
            return self.contain_word(board, words, x+1, y) or self.contain_word(board, words, x, y+1)
        else:
            # 需要回溯到前一个节点
            pass

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pass
    '''
- https://leetcode.com/problems/reverse-vowels-of-a-string/
- 345. Reverse Vowels of a String(easy)
- 问题:  
输入一个字符串, 翻转里面所有的元音字母(包含大小写).
- 思路:
遍历字符串, 用一个数组保存遇到的元音字母, 同时修改原始的字符串
中的元音字母为标记符. 
翻转保存的元音字母数组, 再遍历一遍原始字符, 遇到标记字符则替换.
Runtime: 232 ms, faster than 8.71% of Python3 online submissions for Reverse Vowels of a String.
Memory Usage: 15.3 MB, less than 33.93% of Python3 online submissions for Reverse Vowels of a String.
    '''
    def reverseVowels(self, s: str) -> str:
        s           =   list(s)
        vowels      =   []
        const_vowel =   ['a','e','i','o','u', 'A','E','I','O','U']
        for a in range(s.__len__()):
            c   =   s[a]
            if c in const_vowel:
                vowels.append(c)
                s[a]    =   1
                continue
        vowels.reverse()
        # print("反转 得到 {}\n原始 {}".format(vowels, "".join(s)))
        if len(vowels)  ==  0:
            return "".join(s)
        for a in range(s.__len__()):
            if s[a] == 1:
                s[a]    =   vowels.pop(0)
                # print("替换 {}".format(s[a]))


        return  "".join(s)

    '''
- https://leetcode.com/problems/group-anagrams/
- 49. Group Anagrams(medium)
- 问题:  
输入一组字符串, 把回文字符串组合成子数组. 这里的指的是用同样的字符列表, 组成不同的单词即可.
- 思路:
~~非常简单, 遍历一遍字符串数组, 每个都计算set, 写入到字典即可.~~
排序字符串后, 转为字符串 再写入字典
Runtime: 235 ms, faster than 40.41% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.5 MB, less than 73.37% of Python3 online submissions for Group Anagrams.
边界处理: set 会把相同的字符去掉, 导致不同字符个数的会一样.

    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map        =   {}
        r               =   []
        for s in strs:
            s_      =   str(sorted(s))      # 通过排序
            if word_map.get(s_) is not None:
                word_map[s_].append(s)
                continue
            word_map[s_]    =   []
            word_map[s_].append(s)
        for s, words in word_map.items():
            r.append(words)
        return      r
    '''
- https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
- 1662. Check If Two String Arrays are Equivalent(easy)
- 问题:  
输入两个字符串数组, 判断由他们拼接得到的字符串是否相同: Input: word1 = ["ab", "c"], word2 = ["a", "bc"]. Output: true 
Runtime: 55 ms, faster than 62.71% of Python3 online submissions for Check If Two String Arrays are Equivalent.
Memory Usage: 13.8 MB, less than 75.82% of Python3 online submissions for Check If Two String Arrays are Equivalent
    '''
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        for c1, c2 in zip(self.generate(word1), self.generate(word2)):
            if c1 != c2:
                return False
        return True

    def generate(self, wordlist: List[str]):
        for word in wordlist:
            for char in word:
                yield char
        yield None
    
    '''
- https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
- 645. 1239. Maximum Length of a Concatenated String with Unique Characters(Medium)
- 问题:  
输入一组字符串数组, 找出包含唯一字符的子序列 能够构成的最长字符串的字符个数.  子序列由一组数据在不改变顺序的前提下, 删除一些或不删除元素. 如输入 arr = ["un","iq","ue"], 得到4. 
因为可以构成 un; iq; ue; uniq; ique; 这几个子序列, 最长长度为4
-  
- 大神思路: 
1.用一个数组保存所有可能的字符组合集合
2.过滤存在重复字符的字符串.
3.遍历当前生成的所有可能的组合, 求交集, 若不存在交集则合并, 存在交集则跳过这个组合.
Runtime: 91 ms, faster than 96.86% of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.
Memory Usage: 52.9 MB, less than 8.77% of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.
    '''
    def maxLength(self, arr: List[str]) -> int:
        unique_strs     =   [set()]
        for string in arr:
            if set(string).__len__() < string.__len__():
                continue
            cur_set     =   set(string)
            for prev in unique_strs[:]:
                if prev & cur_set:
                    continue
                unique_strs.append(prev|cur_set)
        
        return max([len(a) for a in unique_strs])
        
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
