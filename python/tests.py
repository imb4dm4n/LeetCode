import unittest
from LinkedList import  *
import time
import os, datetime
from DynamicProgram import Solution as SD
from BinaryTree import Solution as SBT
from BinaryTree import TreeNode
from BinaryTree import *

class timer():
    def __init__(self, module_name=""):
        self.create = time.perf_counter()
        self.module_name = module_name

    def stop(self):
        '''
        返回构造到调用 stop 的时间 ms 
        '''
        stop = time.perf_counter()
        print("<%s> elapsed %s ms " % (self.module_name, (stop - self.create)*1000))
        return (stop - self.create)*1000

'''
python -m unittest  tests  -k TestGreedy
'''
class TestGreedy(unittest.TestCase):

    def test_countFairPairs(self):
        import Greedy as gd
        so  =   gd.Solution()
        r=so.numRescueBoats([1,2], 3)
        print("r= ", r)
        self.assertEqual(r, 1)

        r=so.numRescueBoats([3,2,2,1], 3)
        print("r= ", r)
        self.assertEqual(r, 4)

        r=so.numRescueBoats([3,5,3,4], limit = 5)
        print("r= ", r)
        self.assertEqual(r, 4)

'''
python -m unittest  tests  -k TestSlideWindow
'''
class TestSlideWindow(unittest.TestCase):

    def test_maxVowels(self):
        from SlideWindow import Solution as SSW
        so      =   SSW()
        r=so.maxVowels("abciiidef", 3)
        print(r)
        self.assertEqual(r, 3)

'''
python -m unittest  tests  -k TestArray
'''
class TestArray(unittest.TestCase):

    def test_spiralOrder(self):
        from Array import Solution as SA
        so      =   SA()
        r=so.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
        print(r)

    def xtest_numSubseq(self):
        from Array import Solution as SA
        so      =   SA()
        r=so.numSubseq([3,5,6,7], 9)
        self.assertEqual(r, 4)

        r=so.numSubseq([3,5,6,7], 10)
        self.assertEqual(r, 6)

        r=so.numSubseq([2,3,3,4,6,7], 12)
        self.assertEqual(r, 61)

    def xtest_closedIsland(self):
        from Array import Solution as SA
        so      =   SA()
        print("closedIsland ")
        # so.findTheArrayConcVal
        inp = [
        [0,1,1,1],
        [0,0,0,1],
        [0,1,1,1]]
        r=so.closedIsland(inp)
        print("有 {} 个岛屿".format(r))

        inp = [
        [0,1,1,1,1,1,1],
        [0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0],
        [0,1,1,1,1,1,0],
        ]
        r=so.closedIsland(inp)
        print("有 {} 个岛屿".format(r))

        inp = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
        r=so.closedIsland(inp)
        print("有2= {} 个岛屿".format(r))

        inp = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
        r=so.closedIsland(inp)
        print("有1= {} 个岛屿".format(r))

        inp = [[0,1,1,1,0],[1,0,1,0,1],[1,0,1,0,1],[1,0,0,0,1],[0,1,1,1,0]]
        r=so.closedIsland(inp)
        print("有1= {} 个岛屿".format(r))

        inp = [[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0],[1,1,1,0,0,1,0,1,0,1],[1,1,1,0,1,1,0,1,1,0]]
        r=so.closedIsland(inp)
        print("有5= {} 个岛屿".format(r))

    def xtest_countFairPairs(self):
        from Array import Solution as SA
        so      =   SA()
        print("countFairPairs ")
        # so.findTheArrayConcVal
        r=so.countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6)
        print("countFairPairs = {}".format(r))

        r=so.countFairPairs(nums = [1,7,9,2,5], lower = 11, upper = 11)
        print("countFairPairs = {}".format(r))

        
        r=so.countFairPairs([0,0,0,0,0,0],0,0)
        print("countFairPairs = {} == 15".format(r))
        
        r=so.countFairPairs([5,7,5,7,5],12,12)
        print("countFairPairs = {} == 6".format(r))
        # exit(0)

    def xtest_findTheArrayConcVal(self):
        from Array import Solution as SA
        so      =   SA()
        print("test_findTheArrayConcVal ")
        # so.findTheArrayConcVal
        r=so.findTheArrayConcVal([5,14,13,8,12])
        print("test_findTheArrayConcVal = {}".format(r))
        r=so.findTheArrayConcVal([7,52,2,4])
        print("test_findTheArrayConcVal = {}".format(r))
    
    def xtest_maxDistance(self):
        from Array import Solution as SA
        so      =   SA()
        r=so.maxDistance(grid = [[1,0,1],[0,0,0],[1,0,1]])
        print("最大距离 = {}".format(r))

    def xtest_totalFruit(self):
        from Array import Solution as SA
        so      =   SA()
        r       =   so.totalFruit([1,2,3,2,2])
        print("r={}".format(r))
        r       =   so.totalFruit([0,1,2,2])
        print("r={}".format(r))
        r       =   so.totalFruit([3,3,3,1,2,1,1,2,3,3,4])
        print("r={}".format(r))
        self.assertEqual(r, 5)

    def xtest_shuffle(self):
        from Array import Solution as SA
        so      =   SA()
        r       =   so.shuffle(nums = [2,5,1,3,4,7], n = 3)
        print("r={}".format(r))
        r       =   so.shuffle(nums = [1,2,3,4,4,3,2,1], n = 4)
        print("r={}".format(r))
        r       =   so.shuffle(nums = [1,1,2,2], n = 2)
        print("r={}".format(r))

    def xtest_vowelStrings(self):
        from Array import Solution as SA
        so      =   SA()
        r=so.vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]])
        print("vowel = {}\n\n".format(r))

        r=so.vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]])
        print("vowel = {}".format(r))

    def xtest_corpFlightBookings(self):
        from Array import Solution as SA
        so      =   SA()
        r=so.corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], 5)
        print(r)
        self.assertEqual(r, [10,55,45,25,25])
        r=so.corpFlightBookings([[1,2,10],[2,2,15]], n = 2)
        print(r)
        self.assertEqual(r,[10,25])
        r=so.corpFlightBookings([[2,2,30],[3,3,25],[3,3,20]], n = 3)
        print(r)
        self.assertEqual(r,[0,30,45])
    
    def test_carPooling(self):
        from Array import Solution as SA
        so      =   SA()
        r=so.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 4)
        print(r)
        self.assertEqual(r, False)
        r=so.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 5)
        print(r)
        self.assertEqual(r, True)
        r=so.carPooling(trips = [[2,1,5],[3,5,7]], capacity = 3)
        print(r)
        self.assertEqual(r, True)
        r=so.carPooling(trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11)
        print(r)
        self.assertEqual(r, True)
        r=so.carPooling(trips = [[2,1,5]], capacity = 1)
        print(r)
        self.assertEqual(r, False)
    
    def xtest_Difference(self):
        '''
        差分数组测试
        '''
        from Array import Solution as SA
        so      =   SA()
        from Array import Difference as df 
        diff=df([1,2,3])
        diff.increment(1,2,3)
        print(diff.get_data())
        diff.increment(1,2,-3)
        print(diff.get_data())
        diff.increment(1,1,3)
        print(diff.get_data())
        diff.increment(0,2,3)
        print(diff.get_data())
        diff.increment(2,2,3)
        print(diff.get_data())

    def xtest_findSubsequences(self):
        from Array import Solution as SA
        so      =   SA()
        r=so.findSubsequences([4,6,7,7])

        # self.assertTrue([[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]] == r)
        r=so.findSubsequences([4,4,3,2,1])

'''
python -m unittest  tests  -k Graph
'''
class TestGraph(unittest.TestCase):
    def test_findJudge(self):
        from Graph import Solution as GS
        so  =   GS()
        r=so.findJudge(n = 2, trust = [[1,2]])
        print("r={} exp {}".format(r,2))
        r=so.findJudge( n = 3, trust = [[1,3],[2,3]])
        print("r={} exp {}".format(r,3))
        r=so.findJudge(n = 3, trust = [[1,3],[2,3],[3,1]])
        print("r={} exp {}".format(r,-1))
        r=so.findJudge(n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]])
        print("r={} exp {}".format(r,3))
        r=so.findJudge(n = 2, trust = [])
        print("r={} exp {}".format(r,-1))
        

    def xtest_subarraysDivByK(self):
        from Array import Solution as SA
        so      =   SA()
        # c       =   so.subarraysDivByK([4,5,0,-2,-3,1], k = 5)
        # print(f"c={c}")
        # self.assertEqual(c,     7)
        # c       =   so.subarraysDivByK([1,2,3], k = 3)
        # print(f"c={c}")
        # self.assertEqual(c,     3)
        # c       =   so.subarraysDivByK(nums = [5], k = 9)
        # print(f"c={c}")
        # self.assertEqual(c, 0)
        c       =   so.subarraysDivByK(nums = [-1,2,9], k = 2)
        print(f"c={c}")
        self.assertEqual(c, 2)
    
    def xtest_countRangeSum(self):
        from Array import Solution as SA
        so      =   SA()
        arr     =   so.countRangeSum([-2,5,-1], -2, 2)
        

    def xtest_productExceptSelf(self):
        from Array import Solution as SA
        so      =   SA()
        arr     =   so.productExceptSelf([1,2,3,4])
        self.assertEqual(arr, [24,12,8,6])
        arr     =   so.productExceptSelf([-1,1,0,-3,3])
        self.assertEqual(arr, [0,0,9,0,0])
    
    def xtest_matrixBlockSum(self):
        from Array import Solution as SA
        so      =   SA()
        arr     =   so.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], k = 1)
        arr     =   so.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], k = 2)


    def xtest_ProductOfNumbers(self):
        from Array import Solution as SA
        so      =   SA()
        arr     =   so.ProductOfNumbers()
        arr.add(3)
        arr.add(0)
        arr.add(2)
        arr.add(5)
        arr.add(4)
        print(arr.getProduct(2))
        print(arr.getProduct(3))
        print(arr.getProduct(4))
        arr.add(8)
        print(arr.getProduct(2))
        print(arr.getProduct(1))
        print(arr.getProduct(3))
        print(arr.getProduct(4))
        print("-------test 2\n")
        #
        arr     =   so.ProductOfNumbers()
        arr.add(0)
        arr.add(5)
        arr.add(6)
        print(arr.getProduct(2))
        print(arr.getProduct(2))
        arr.add(8)
        print(arr.getProduct(4))
        arr.add(2)

    def xtest_NumMatrix(self):
        from Array import Solution as SA
        so      =   SA()
        # arr     =   so.NumMatrix([[1,2,3],[2,3,4],[3,4,5],[4,5,6]])
        arr     =   so.NumMatrix([[1,2,3],[4,5,6],[7,8,9]])
        # print(arr.pre_sum_matrix)
        arr.print_pre_sum_matrix()
        print(arr.sumRegion(1, 1, 2, 2))
        # print(arr.sumRegion(2, 1, 4, 3))
        arr     =   so.NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
        arr.print_pre_sum_matrix()
        print(arr.sumRegion(2, 1, 4, 3))
        print(arr.sumRegion(1, 1, 2, 2))
        print(arr.sumRegion(1, 2, 2, 4))
    
    def xtest_NumArray(self):
        from Array import Solution as SA
        so      =   SA()
        arr     =   so.NumArray([-2,0,3,-5,2,-1])
        self.assertEqual( arr.sumRange(0, 2), 1)
        self.assertEqual( arr.sumRange(2, 5), -1)
        self.assertEqual( arr.sumRange(0, 5), -3)

        arr     =   so.NumArray([-1])
        self.assertEqual( arr.sumRange(0, 0), -1)
        

'''
python -m unittest  tests  -k TestSearching
'''
class TestSearching(unittest.TestCase):
    def test_dailyTemperatures(self):
        from Searching import Solution as SSS
        so      =   SSS()
        
'''
python -m unittest  tests  -k TestSorts
'''
class TestSorts(unittest.TestCase):
    def test_sortArray(self):
        from Sorting import Solution as SS
        so =    SS()
        r=so.sortArray(  nums = [-1,0,3,11,2])
        print("r= ", r)
        self.assertEqual(r, [-1,0,2,3,11])
        r=so.sortArray(nums = [5,2,3,1])
        print("r= ", r)
        self.assertEqual(r, [1, 2, 3, 5])
        r=so.sortArray(  nums = [5,1,1,2,0,0])
        print("r= ", r)
        self.assertEqual(r,  [0, 0, 1, 1, 2, 5])

        
''' 
python -m unittest  tests  -k TestMatrix
'''
class TestMatrix(unittest.TestCase):
    def test_minPathSum(self):
        from Matirx import Solution  as SM
        so = SM()
        r=so.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
        print("r= ",r)
        self.assertEqual(r, 7)

        r=so.minPathSum([[1,4,8,6,2,2,1,7],[4,7,3,1,4,5,5,1],[8,8,2,1,1,8,0,1],[8,9,2,9,8,0,8,9],[5,7,5,7,1,8,5,5],[7,0,9,4,5,6,5,6],[4,9,9,7,9,1,9,0]])
        print("r= ",r)
        self.assertEqual(r, 47)

''' 
python -m unittest  tests  -k TestStrings
'''
class TestStrings(unittest.TestCase):
    def test_partitionString(self):
        from Strings import Solution
        so      =   Solution()
        r=so.partitionString("abacaba")
        print("r=",r)
        r=so.partitionString("ssssss")
        print("r=",r)

    def xtest_checkInclusion(self):
        from Strings import Solution
        so      =   Solution()
        r=so.checkInclusion(s1 = "ab", s2 = "eidboaoo")
        print("r=",r)
        r=so.checkInclusion(s1 = "ab", s2 = "eidbaooo")
        print("r=",r)


    def xtest_findAnagrams(self):
        from Strings import Solution
        so      =   Solution()
        r=so.findAnagrams(s = "cbaebabacd", p = "abc")
        print("r=",r)
        r=so.findAnagrams(s = "abab", p = "ab")
        print("r=",r)
        r=so.findAnagrams(s = "qwejosazxc", p = "as")
        print("r=",r)
        r=so.findAnagrams(s = "", p = "as")
        print("r=",r)
        r=so.findAnagrams(s = "asd", p = "z")
        print("r=",r)


    def xtest_lengthOfLongestSubstring(self):
        from Strings import Solution
        so      =   Solution()
        r=so.lengthOfLongestSubstring(s = "abcabcbb")
        print("r= ", r)
        r=so.lengthOfLongestSubstring(s = "abcabcbb")
        print("r= ", r)
        r=so.lengthOfLongestSubstring(s = "bbbbb")
        print("r= ", r)
        s = "pwwkew"
        r=so.lengthOfLongestSubstring(s)
        print("r= ", r, " s= ", s)
    
        
    def xtest_isAlienSorted(self):
        from Strings import Solution
        so      =   Solution()
        haystack = "mississippi"
        needle =  "issipi"
        r=so.strStr(haystack,needle)
        print("r= ", r, haystack.find(needle))
        self.assertEqual(r,  haystack.find(needle))

        haystack = "OOOOOOPPOOOO"
        needle = "OP"
        r=so.strStr(haystack,needle)
        print("r= ", r, haystack.find(needle))
        self.assertEqual(r,  haystack.find(needle))

        r=so.strStr(haystack = "sadbutsad", needle = "sad")
        print("r= ", r)
        self.assertEqual(r, 0)

        r=so.strStr(haystack = "leetcode", needle = "leeto")
        print("r= ", r)
        self.assertEqual(r,-1 )

        r=so.strStr(haystack = "", needle = "leeto")
        print("r= ", r)
        self.assertEqual(r,-1 )

        haystack = "asdzxcqwe"
        needle = "cqw"
        r=so.strStr(haystack,needle)
        print("r= ", r)
        self.assertEqual(r,  haystack.find(needle))

    
        
    def xtest_isAlienSorted(self):
        from Strings import Solution
        so      =   Solution()
        
        r = so.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
        )
        print("isAlienSorted {}".format(r))
        self.assertEqual(r, True)

        r=so.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
        )
        print("isAlienSorted {}".format(r))
        self.assertEqual(r, False)

        r=so.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
        )
        print("isAlienSorted {}".format(r))
        self.assertEqual(r, False)

        r=so.isAlienSorted(words =["hello","hello"],order ="abcdefghijklmnopqrstuvwxyz"
        )
        print("isAlienSorted {}".format(r))
        self.assertEqual(r, True)


    def xtest_gcdOfStrings(self):
        from Strings import Solution
        so      =   Solution()
        print("gcdOfStrings {}".format(so.gcdOfStrings(
            str1 = "ABCABC", str2 = "ABC"
        )))
        
    
    def xtest_minDeletionSize(self):
        from Strings import Solution
        so      =   Solution()
        print("minDeletionSize {}".format(so.minDeletionSize(
            ["cba","daf","ghi"]
        )))
        print("minDeletionSize {}".format(so.minDeletionSize(
            ["rrjk","furt","guzm"]
        )))
        
    def xtest_detectCapitalUse(self):
        from Strings import Solution
        so      =   Solution()
        print("detectCapitalUse {}".format(so.detectCapitalUse(
            'FlaG' 
        )))
        print("detectCapitalUse {}".format(so.detectCapitalUse(
            "ffffffffffffffffffffF"
        )))
    
    def xtest_isIsomorphic(self):
        from Strings import Solution
        so      =   Solution()
        print("isIsomorphic {}".format(so.isIsomorphic(
            'paper',
            'title'
        )))
        print("isIsomorphic {}".format(so.isIsomorphic(
            'foo',
            'bar'
        )))
        print("isIsomorphic {}".format(so.isIsomorphic(
            "badc",
            'baba'
        )))
    
    
    def xtest_makeGood(self):
        from Strings import Solution
        so      =   Solution()
        s='leEetcode'
        print("{} => {}".format(s, so.makeGood(s)))
        s='abBACc'
        print("{} => {}".format(s, so.makeGood(s)))
        s=''
        print("{} => {}".format(s, so.makeGood(s)))
    
    def xtest_reverseVowels(self):
        from Strings import Solution
        so      =   Solution()
        print(so.reverseVowels('hello'))
    
    def xtestmaxLength(self):
        from Strings import Solution
        so      =   Solution()
        inp     =   ['un','iq','ue']
        print("input {}\noutput {}".format(inp, so.maxLength(inp)))
        print("expect: 4")
        inp     =   ["cha","r","act","ers"]
        print("input {}\noutput {}".format(inp, so.maxLength(inp)))
        print("expect: 6")


    def xtest_minWindow(self):
        from Strings import Solution
        so      =   Solution()
        inp     =   "ADOBECODEBANC"
        print("input {}\noutput {}".format(inp, so.minWindow(inp, "ABC")))
        print("expect: BANC")

'''
python -m unittest  tests  -k TestAlgorithm
'''

class TestAlgorithm(unittest.TestCase):
    
    def xtest_compress(self):
        from Algorithm import Solution
        so      =   Solution()

        chars = ["a","a","b","b","c","c","c"]
        x=so.compress(chars)
        print("x= ", x, )
        self.assertEqual(x, 6)

        chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        x=so.compress(chars)
        print("x= ", x,  )
        self.assertEqual(x, 4)

        chars = ["a" ]
        x=so.compress(chars)
        print("x= ", x,  )
        self.assertEqual(x, 1)
        chars = ["a","a","a","a","a","b"]
        x=so.compress(chars)
        print("x= ", x,  )
        # self.assertEqual(x, 1)
        print("OK")
    
    def xtest_countOdds(self):
        from Algorithm import Solution
        so      =   Solution()
        x=so.countOdds(8,10)
        print("x = {}".format(x))

    def xtest_tribonacci(self):
        from Algorithm import Solution
        so      =   Solution()



        r=so.addBinary(a = "11", b = "1")
        print(f"100 = {r}\n")
        r=so.addBinary(a = "1010", b = "1011")
        print(f"10101 = {r}")
    
    def xtest_minFlipsMonoIncr(self):
        from Algorithm import Solution
        so      =   Solution()
    def test_minFlipsMonoIncr(self):
        from Algorithm import Solution
        so      =   Solution()
        x=so.tribonacci(25)
        print("x={}".format(x))
        self.assertEqual(x, 1389537)
    def xtest_minFlipsMonoIncr(self):
        from Algorithm import Solution
        so      =   Solution()
        print(so.minFlipsMonoIncr('00110'), 'expect 1')
        print(so.minFlipsMonoIncr('010110'), 'expect 2')
        print(so.minFlipsMonoIncr('00011000'), 'expect 2')
        print(so.minFlipsMonoIncr('0011'))
        print(so.minFlipsMonoIncr('00101'))
        print(so.minFlipsMonoIncr('001010'))
    
    def xtest_insert(self):
        from Algorithm import Solution
        so      =   Solution()
        r=so.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
        self.assertEqual(r, [[1,2],[3,10],[12,16]])

        r=so.insert([[1,3],[6,9]], [2,5])
        self.assertEqual(r, [[1,5],[6,9]])

        r=so.insert([[1,3],[6,9]], [4,5])
        self.assertEqual(r, [[1,3],[4,5],[6,9]])

        r=so.insert([[2,5],[6,7],[8,9]], [0,1])
        self.assertEqual(r, [[0,1],[2,5],[6,7],[8,9]])

    def xtest_canCompleteCircuit(self):
        from Algorithm import Solution
        so      =   Solution()
        self.assertEqual(
            so.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]), 3)
        
        self.assertEqual(
            so.canCompleteCircuit([2,3,4], [3,4,3]), -1)
        
        # self.assertEqual(
        #     so.canCompleteCircuit(gas, cost), -1)
    
    def xtest_minimumRounds(self):
        from Algorithm import Solution
        so      =   Solution()
        self.assertEqual(so.minimumRounds([2,2,3,3,2,4,4,4,4,4]), 4)
        print("-")
        self.assertEqual(so.minimumRounds([5,5,5,5]), 2)
        print("-")
        self.assertEqual(so.minimumRounds([66,66,63,61,63,63,64,66,66,65,66,65,61,67,68,66,62,67,61,64,66,60,69,66,65,68,63,60,67,62,68,60,66,64,60,60,60,62,66,64,63,65,60,69,63,68,68,69,68,61]), 20)
        
    def xtest_rob(self):
        from Algorithm import Solution
        so      =   Solution()
        self.assertEqual(so.rob([1,2,3,1]), 4)
        self.assertEqual(so.rob([2,7,9,3,1]), 12)
        print("rob test ok ")
    
    def xtest_climbStairs(self):
        from Algorithm import Solution
        so      =   Solution()
        self.assertEqual(so.climbStairs(11), 144)
        self.assertEqual(so.climbStairs(3), 3)
        print("返回 {}".format(
            so.climbStairs(11)
        ))
        so      =   Solution()
        print("返回 {}".format(
            so.climbStairs(3)
        ))
    def xtest_pivotIndex(self):
        from Algorithm import Solution
        so      =   Solution()
        inp     =   [-1,-1,-1,-1,-1,-1]
        print("返回 {}".format(
            so.pivotIndex(inp)
        ))
        inp     =   [1,2,3,4,6]
        print("返回 {}".format(
            so.pivotIndex(inp)
        ))
        inp     =   [-1,-1,-1,-1,-1,0]
        print("返回 {}".format(
            so.pivotIndex(inp)
        ))
        inp     =   [2,1,-1]
        print("返回 {}".format(
            so.pivotIndex(inp)
        ))


    def xtest_findBall(self):
        from Algorithm import Solution
        so      =   Solution()
        inp     =   [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
        print("返回 {}".format(
            so.findBall(inp)
        ))
        
    def xtest_isToeplitzMatrix(self):
        from Algorithm import Solution
        so      =   Solution()
        inp     =   [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
        print("对角矩阵相同 {}".format(
            so.isToeplitzMatrix(inp)
        ))
        inp     =   [[1,2],[2,2]]
        print("对角矩阵相同 {}".format(
            so.isToeplitzMatrix(inp)
        ))
    def xtest_findErrorNums(self):
        from Algorithm import Solution
        so      =   Solution()
        inp     =   [27,5,24,17,27,4,23,16,6,26,13,17,21,3,9,10,28,26,4,10,28,2]
        inp1= [26,9,14,17,6,14,23,24,11,6,27,14,13,1,15,5,12,15,23,27,28,12]
        print("最短耗时 {}".format(
            so.earliestFullBloom(inp, inp1)
        ))

    def xtest_findErrorNums(self):
        from Algorithm import Solution
        so      =   Solution()
        inp     =   [1,2,2,4]
        print("inp {}\noutput {}\nexpect {}\n".format(
            inp,
            so.findErrorNums(inp),
            [2,3]
        ))
        inp     =   [3,2,2]
        print("inp {}\noutput {}\nexpect {}\n".format(
            inp,
            so.findErrorNums(inp),
            [2,1]
        ))
        inp     =   [1,1]
        print("inp {}\noutput {}\nexpect {}\n".format(
            inp,
            so.findErrorNums(inp),
            [1,2]
        ))
        inp     =   [3,4,2,2]
        print("inp {}\noutput {}\nexpect {}\n".format(
            inp,
            so.findErrorNums(inp),
            [2,1]
        ))
        inp     =   [2,3,2]
        print("inp {}\noutput {}\nexpect {}\n".format(
            inp,
            so.findErrorNums(inp),
            [2,1]
        ))
        inp     =   [2,1,2,3,4,5]
        print("inp {}\noutput {}\nexpect {}\n".format(
            inp,
            so.findErrorNums(inp),
            [2,6]
        ))

    def xtest_intToRoman(self):
        from Algorithm import Solution
        so      =   Solution()
        print("input {} output {}".format(
            123,
            so.intToRoman(123)
        ))
        print("input {} output {}".format(
            149,
            so.intToRoman(149)
        ))
        print("input {} output {}".format(
            1997,
            so.intToRoman(1997)
        ))
        print("input {} output {}".format(
            5494,
            so.intToRoman(5494)
        ))
        print("input {} output {}".format(
            444,
            so.intToRoman(444)
        ))
        print("input {} output {}".format(
            54,
            so.intToRoman(54)
        ))

    def xtest_topKFrequent(self):
        from Algorithm import Solution
        so      =   Solution()
        ret = so.topKFrequent(["love","leetcode","i","i","love","coding"], 1)
        print("ret = {}".format(ret))

        ret = so.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4)
        print("ret = {}".format(ret))
        '''
        ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
        '''
    
    def xtest_threeSumClosest(self):
        from Algorithm import Solution
        so      =   Solution()
        ret = so.threeSumClosest([-1,2,1,-4], 1)
        print("ret = {}".format(ret))

'''
python -m unittest  tests  -k TestBinaryTree
'''
class TestBinaryTree(unittest.TestCase):


    def test_maxLevelSum(self):
        so  =   SBT()
        inp     =   [1,7,0,7,-8,null,null]
        inp     =   [-100,-200,-300,-20,-5,-10,null]
        root    =   list_2_tree(inp)
        r=so.maxLevelSum(root)
        print("r =2?  ", r )

    def xtest_widthOfBinaryTree(self):
        so  =   SBT()
        inp     =   [1,3,2,5,null,null,9,6,null,7]
        root    =   list_2_tree(inp)
        r=so.widthOfBinaryTree(root)
        print("r =7?  ", r )
        inp     =   [1,3,2,5]
        root    =   list_2_tree(inp)
        r=so.widthOfBinaryTree(root)
        print("r =2 ? ", r )
        inp     =    [1,3,2,5,3,null,9]
        root    =   list_2_tree(inp)
        r=so.widthOfBinaryTree(root)
        print("r =4 ? ", r )
        inp     =    [1,3,2,null,3,9,null,9]
        root    =   list_2_tree(inp)
        r=so.widthOfBinaryTree(root)
        print("r =2 ? ", r )
        inp     =    [0,0,0,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null,null,0,0,null]
        root    =   list_2_tree(inp)
        r=so.widthOfBinaryTree(root)
        print("r =2 ? ", r )


    def xtest_BrowserHistory(self):
        from BinaryTree import BrowserHistory as bh
        browserHistory  =   bh('www.leetcode.com')
        browserHistory.visit("google.com")
        browserHistory.visit("facebook.com")
        browserHistory.visit("youtube.com");  
        r=browserHistory.back(1);             
        print("back ", r)
        self.assertEqual(r, "facebook.com")
        r=browserHistory.back(1);                  
        print("back ", r)
        self.assertEqual(r, "google.com")
        r=browserHistory.forward(1);              
        print("forward ", r)
        self.assertEqual(r, "facebook.com")
        browserHistory.visit("linkedin.com");     
        r=browserHistory.forward(2);              
        print("forward ", r)
        self.assertEqual(r, "linkedin.com")
        r=browserHistory.back(2);                   
        r=browserHistory.back(7);   
        print("back ", r)     
        self.assertEqual(r, "www.leetcode.com")


    def xtest_buildTree(self):
        so  =   SBT()
        r=so.buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3])
        print("r ", r )


    def xtest_isCompleteTree(self):
        so  =   SBT()
        inp     =   [1,2,3,4,5,6]
        root    =   list_2_tree(inp)
        r=so.isCompleteTree(root)
        print("r ", r )
        inp     =   [1,2,3,4,5,null,7]
        root    =   list_2_tree(inp)
        r=so.isCompleteTree(root)
        print("r ", r )


    def xtest_sortedListToBST(self):
        so  =   SBT()
        inp     =   [-10,-3,0,5,9]
        root    =   ListNode.list_to_ListNode(inp)
        r = so.sortedListToBST(root)
        r=so.inorderTraversal(r)
        print("r ", r )

    def xtest_pathSum(self):
        so  =   SBT()
        inp     =   [10,5,-3,3,2,null,11,3,-2,null,1]
        root    =   list_2_tree(inp)
        r=so.pathSum(root, 8)
        print("r = {}, exp 3".format(r))

        inp     =   [5,4,8,11,null,13,4,7,2,null,null,5,1]
        root    =   list_2_tree(inp)
        r=so.pathSum(root, 22)
        print("r = {}, exp 3".format(r))

        inp     =   [1,-2,-3,1,3,-2,null,-1]
        root    =   list_2_tree(inp)
        r=so.pathSum(root, -1)
        print("r = {}, exp 4".format(r))

        inp     =   [1,-2,-3,1,3,-2,null,-1]
        root    =   list_2_tree(inp)
        r=so.pathSum(root, -2)
        print("r = {}, exp 4".format(r))

        inp     =   [1,0,1,1,2,0,-1,0,1,-1,0,-1,0,1,0]
        root    =   list_2_tree(inp)
        r=so.pathSum(root, 2)
        print("r = {}, exp 13".format(r))

        inp     =   [9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]
        root    =   list_2_tree(inp)
        r=so.pathSum(root, 4)
        print("r = {}, exp 3".format(r))


    def xtest_countSubTrees(self):
        so  =   SBT()
        inp     =   [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
        r=so.countSubTrees(7,
            inp,
            "abaedcd")
        print(r)
        inp     =   [[0,2],[0,3],[1,2]]
        r=so.countSubTrees(4,
            inp,
            "aeed")
        print(r)
        self.assertEqual([1,1,2,1], r)
        
    def xtest_maxPathSum(self):
        so  =   SBT()
        inp     =   [-10,9,20,null,null,15,7]
        self.assertEqual(
            42,
            so.maxPathSum(
                list_2_tree(inp)
            )
        )
        inp     =   [-3]
        print("返回 {}".format(
            so.maxPathSum(
                list_2_tree(inp)
            )
        ))
        inp     =   [1,-2,-3,1,3,-2,null,-1]
        print("返回 {}".format(
            so.maxPathSum(
                list_2_tree(inp)
            )
        ))
    
    def xtest_maxAncestorDiff(self):
        so  =   SBT()
        root    =   list_2_tree([1,null,2,null,0,3])
        ret = so.maxAncestorDiff(root)
        print("ret = {} ".format(ret))
        self.assertEqual(ret, 3)

        root    =   list_2_tree([8,3,10,1,6,null,14,null,null,4,7,13])
        ret = so.maxAncestorDiff(root)
        print("ret = {} ".format(ret))
        self.assertEqual(ret, 7)

    def xtest_inorderTraversal(self):
        so      =   SBT()
        root    =   TreeNode(1)
        left    =   TreeNode(2)
        root.left=left
        ret     =    so.inorderTraversal(root)
        print(ret)

'''
python -m unittest  tests  -k TestGraph
'''
# from Graph import Solution as GS
# class TestGraph(unittest.TestCase):
#     def setUp(self) -> None:
#         self.so     =   GS()
#         self.t          =   timer("Graph")
#         return super().setUp()
    
#     def tearDown(self) -> None:
#         self.t.stop()
#         return super().tearDown()

#     def test_validPath(self):
#         temps   =   [[0,1],[1,2],[2,0]]
#         ret = self.so.validPath(temps.__len__(),temps,0,2)
#         print(ret)
#         temps   =   [[0,1],[0,2],[3,5],[5,4],[4,3]]
#         ret = self.so.validPath(temps.__len__(),temps,0,5)
#         print(ret)
#         temps   =   [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
#         ret = self.so.validPath(temps.__len__(),temps,7,5)
#         print(ret)
#         return

'''
python -m unittest  tests  -k TestStack
'''
from Stack import Solution as SS
class TestStackProgram(unittest.TestCase):
    def setUp(self) -> None:
        self.so     =   SS()
        self.t          =   timer("Stack")
        return super().setUp()
    
    def tearDown(self) -> None:
        self.t.stop()
        return super().tearDown()

    def test_validateStackSequences(self): 
        ret = self.so.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1])
        print("r = ",ret)
        ret = self.so.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,3,5,1,2])
        print("r = ",ret)
        ret = self.so.validateStackSequences(pushed = [1], popped = [3])
        print("r = ",ret)

    def xtest_simplifyPath(self): 
        ret = self.so.simplifyPath("/home/../../../../hunter/")
        print("r = ",ret)
        ret = self.so.simplifyPath("/home/../././../.././/..//hunter/")
        print("r = ",ret)
        ret = self.so.simplifyPath("/home/../././../.././/..//hunter/...")
        print("r = ",ret)
        ret = self.so.simplifyPath("/..")
        print("r = ",ret)
        return

    def xtest_dailyTemperatures(self):
        temps   =   [73,74,75,71,69,72,76,73]
        ret = self.so.dailyTemperatures(temps)
        print(ret)
        return

    def xtest_evalRPN(self):
        r=self.so.evalRPN(["2","1","+","3","*"])
        print("R={}".format(r))

        r=self.so.evalRPN(["4","13","5","/","+"])
        print("R={}".format(r))

        r=self.so.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
        print("R={}".format(r))


'''
python -m unittest  tests  -k TestDynamicProgram
'''
class TestDynamicProgram(unittest.TestCase):
    def setUp(self) -> None:
        self.so     =   SD()
        self.t          =   timer("DynamicProgram")
        return super().setUp()
    
    def tearDown(self) -> None:
        self.t.stop()
        return super().tearDown()
    
    def test_countGoodStrings(self):
        r=self.so.countGoodStrings(low = 3, high = 3, zero = 1, one = 1)
        print("r= ",r)
        r=self.so.countGoodStrings(low = 2, high = 3, zero = 1, one = 2)
        print("r= ",r)
    
    def xtest_uniquePathsWithObstacles(self):
        r=self.so.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
        print("r= ",r)
        self.assertEqual(r, 2)
        r=self.so.uniquePathsWithObstacles([[0,1],[0,0]])
        print("r= ",r)
        self.assertEqual(r, 1)
        r=self.so.uniquePathsWithObstacles([
            [0,0,1,0],
            [1,0,0,0],
            [0,0,1,0],
            [0,0,0,0],
            [0,0,0,0]])
        print("r= ",r)
        self.assertEqual(r, 4)
    
    def xtest_minFallingPathSum(self):
        r=self.so.minFallingPathSum(matrix = [[2,1,3],[6,5,4],[7,8,9]])
        print("r= ",r)
        self.assertEqual(r, 13)
        r=self.so.minFallingPathSum([[-19,57],[-40,-5]])
        print("r= ",r)
        self.assertEqual(r, -59)
        r=self.so.minFallingPathSum([[13]])
        print("r= ",r)
        self.assertEqual(r, 13)
        
        
    
    def xtest_coinChange(self):
        r=self.so.coinChange(coins = [1,2,5], amount = 11)
        print("r= ",r)
        self.assertEqual(r, 3)
        r=self.so.coinChange(coins = [2], amount = 3)
        print("r= ",r)
        self.assertEqual(r, -1)
        r=self.so.coinChange(coins = [1], amount = 0)
        print("r= ",r)
        self.assertEqual(r, 0)
        

    def xtest_maxSatisfaction(self):
        # r=self.so.maxSatisfaction(satisfaction = [34,-27,-49,-6,65,70,72,-37,-57,92,-72,36,6,-91,18,61,77,-91,5,64,-16,5,20,-60,-94,-15,-23,-10,-61,27,89,38,46,57,33,94,-79,43,-67,-73,-39,72,-52,13,65,-82,26,69,67])
        # print("r= ",r)
        # self.assertEqual(r, 14)
        r=self.so.maxSatisfaction(satisfaction = [-1,-8,0,5,-9])
        print("r= ",r)
        self.assertEqual(r, 14)
        r=self.so.maxSatisfaction(satisfaction = [-1,-8,0,5,-9,33,100,-50,-120,500,-300,-200,-122,666,888,444])
        print("r= ",r)
        self.assertEqual(r, 36669)
        r=self.so.maxSatisfaction(satisfaction = [4,3,2])
        print("r= ",r)
        self.assertEqual(r, 20)
        r=self.so.maxSatisfaction(satisfaction = [-1,-4,-5])
        print("r= ",r)
        self.assertEqual(r, 0)
    
    def xtest_mincostTickets(self):
        r=self.so.mincostTickets(days = [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,24,25,27,28,29,30,31,34,37,38,39,41,43,44,45,47,48,49,54,57,60,62,63,66,69,70,72,74,76,78,80,81,82,83,84,85,88,89,91,93,94,97,99], costs = [9,38,134])
        print("r= ",r)
        self.assertEqual(r, 423)

        r=self.so.mincostTickets(days = [1,3,4,5 ], costs = [2,7,15])
        print("r= ",r)
        # return
        r=self.so.mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15])
        print("r= ",r)
        self.assertEqual(r, 11)
    
    def xtest_minPathSum(self):
        r=self.so.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
        print("r= ",r)
        self.assertEqual(r, 7)

        r=self.so.minPathSum([[1,4,8,6,2,2,1,7],[4,7,3,1,4,5,5,1],[8,8,2,1,1,8,0,1],[8,9,2,9,8,0,8,9],[5,7,5,7,1,8,5,5],[7,0,9,4,5,6,5,6],[4,9,9,7,9,1,9,0]])
        print("r= ",r)
        self.assertEqual(r, 47)
    
    def xtest_canPlaceFlowers(self):
        r=self.so.canPlaceFlowers(flowerbed = [1,0,0,0,1,0,0], n = 2)
        print("种花  ", r)
        self.assertEqual(r, True   )

        r=self.so.canPlaceFlowers(flowerbed = [0,1,0], n = 1)
        print("种花  ", r)
        self.assertEqual(r, False   )
        r=self.so.canPlaceFlowers(flowerbed = [1,0,1,0,0], n = 1)
        print("种花  ", r)
        self.assertEqual(r, True   )

        r=self.so.canPlaceFlowers(flowerbed = [1,0,0,0,0,1], n = 2)
        print("种花  ", r)
        self.assertEqual(r, False   )
        r=self.so.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1)
        print("种花  ", r)
        self.assertEqual(r, True   )
        r=self.so.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2)
        print("种花  ", r)
        self.assertEqual(r, False   )
        r=self.so.canPlaceFlowers(flowerbed = [0,1,1,0,0], n = 1)
        print("种花  ", r)
        self.assertEqual(r, True   )
    
    def xtest_maxProfit(self):
        r=self.so.maxProfit(prices = [7,1,5,3,6,4])
        print("最大利益 ", r)
    
    def xtest_minCapability(self):
        r=self.so.minCapability(nums = [2,3,5,9], k = 2)
        print("r={} == 5".format(r))
        r=self.so.minCapability(nums = [2,7,9,3,1], k = 2)
        print("r={} ==2".format(r))
        r=self.so.minCapability(nums = [5038,3053,2825,3638,4648,3259,4948,4248,4940,2834,109,5224,5097,4708,2162,3438,4152,4134,551,3961,2294,3961,1327,2395,1002,763,4296,3147,5069,2156,572,1261,4272,4158,5186,2543,5055,4735,2325,1206,1019,1257,5048,1563,3507,4269,5328,173,5007,2392,967,2768,86,3401,3667,4406,4487,876,1530,819,1320,883,1101,5317,2305,89,788,1603,3456,5221,1910,3343,4597], k = 28)
        print("r={} ==2".format(r))
        
    def xtest_bestTeamScore(self):
        # r   =   self.so.bestTeamScore(scores = [4,5,6,5], ages = [2,1,2,1])
        # print("最优分数 {}".format(r))
        # self.assertEqual(r,16)

        # r   =   self.so.bestTeamScore(scores = [1,3,5,10,15], ages = [1,2,3,4,5])
        # print("最优分数 {}".format(r))
        # self.assertEqual(r,34)

        # r   =   self.so.bestTeamScore(scores = [1,2,3,5], ages = [8,9,10,1])
        # print("最优分数 {}".format(r))
        # self.assertEqual(r,6)

        # r   =   self.so.bestTeamScore(scores = [319776,611683,835240,602298,430007,574,142444,858606,734364,896074], ages = [1,1,1,1,1,1,1,1,1,1])
        # print("最优分数 {}".format(r))
        # self.assertEqual(r, 5431066)

        r   =   self.so.bestTeamScore(scores = [1,3,7,3,2,4,10,7,5], ages = [4,5,2,1,1,2,4,1,4])
        print("最优分数 {}".format(r))
        self.assertEqual(r, 29)
    
    def xtest_minStoneSum(self):
        r   =   self.so.minStoneSum([5,4,9],2)
        print(r)
    
    def xtest_canJump(self):
        r   =   self.so.canJump([2,3,1,1,4])
        print(r)
        r   =   self.so.canJump([3,2,1,0,4])
        print(r)
        r   =   self.so.canJump([0])
        print(r)
        r   =   self.so.canJump([0,2,3])
        print(r)
    
    def xtest_longestCommonSubsequence(self):
        r   =   self.so.longestCommonSubsequence("abcde", "aaace")
        print(r)
        r   =   self.so.longestCommonSubsequence("abcde", "ace")
        print(r)
        r   =   self.so.longestCommonSubsequence("abc", "def")
        print(r)
        r   =   self.so.longestCommonSubsequence("bl", "yby")
        print(r)
        r   =   self.so.longestCommonSubsequence("bsbininm", "jmjkbkjkv")
        print(r)

    def xtest_numDecodings(self):
        r   =   self.so.numDecodings("2611055971756562")
        print(r)
        r   =   self.so.numDecodings("226")
        print(r)
        r   =   self.so.numDecodings("27")
        print(r)
        r   =   self.so.numDecodings("18")
        print(r)
        r   =   self.so.numDecodings("12")
        print(r)
        r   =   self.so.numDecodings("06")
        print(r)
        r   =   self.so.numDecodings("106")
        print(r)



'''
python -m unittest  tests  -k TestBinarySearch
'''
class TestBinarySearch(unittest.TestCase):
    
    def xtest_minEatingSpeed(self):
        from BinarySearch import Solution
        so      =   Solution()
        r=so.minEatingSpeed(piles = [312884470], h = 968709470)
        print("4= r =",r)
        # return
        r=so.minEatingSpeed(piles = [3,6,7,11], h = 8)
        print("4= r =",r)
        r=so.minEatingSpeed(piles = [30,11,23,4,20], h = 5)
        print("30= r =",r)
        r=so.minEatingSpeed(piles = [30,11,23,4,20], h = 6)
        print("23= r =",r)
    
    def xtest_minimumTime(self):
        from BinarySearch import Solution
        so      =   Solution()
        r=so.minimumTime([1,2,3], 5)
        print("r=",r)
        
    
    def test_findKthPositive(self):
        from BinarySearch import Solution
        so      =   Solution()
        # r=so.findKthPositive(arr = [2,3,4,7,11], k = 4)
        # print("r= ", r)

        r=so.findKthPositive2(arr = [2,3,4,7,11], k = 4)
        print("r= ", r)
        self.assertEqual(r, 8)
        
        # r=so.findKthPositive(arr = [1,2,3,4], k = 2)
        # print("r= ", r)
        # self.assertEqual(r, 6)
        
        r=so.findKthPositive2(arr = [1,2,3,4], k = 2)
        print("r= ", r)
        self.assertEqual(r, 6)
        # r=so.findKthPositive(arr = [1,2,3,5,7], k = 2)
        # print("r= ", r)
        # self.assertEqual(r, 6)
        r=so.findKthPositive2(arr = [1,2,3,5,7], k = 2)
        print("r= ", r)
        self.assertEqual(r, 6)
        # r=so.findKthPositive(arr = [1,2], k = 3)
        # print("r= ", r)
        # self.assertEqual(r, 5)
    

    def xtest_search(self):
        from BinarySearch import Solution as sbs
        so  =   sbs()
        r=so.searchx(nums = [1,3], target = 3)
        print("r= ", 1)
        self.assertEqual(r, 4)
        r=so.searchx(nums = [4,5,6,7,0,1,2], target = 0)
        print("r= ", r)
        self.assertEqual(r, 4)
        r=so.searchx( nums =[1,3], target = 1)
        print("r= ", r)
        self.assertEqual(r, 0)
        r=so.searchx( nums =[3, 1], target = 0)
        print("r= ", r)
        self.assertEqual(r, -1)
        r=so.searchx( nums =[3,5,1], target = 3)
        print("r= ", r)
        self.assertEqual(r, 0)
        # self.assertEqual(r, 4)
    
    def xtest_searchMatrix(self):
        from BinarySearch import Solution as sbs
        so  =   sbs()
        r=so.searchMatrix(matrix = [[-1,3]], target = -1)
        print(r)
        self.assertEqual(r, True)
        
        r=so.searchMatrix(matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], target = 19)
        print(r)
        self.assertEqual(r, True)

        r=so.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5)
        print(r)
        self.assertEqual(r, True)
        r=so.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20)
        print(r)
        self.assertEqual(r, False)
        r=so.searchMatrix(matrix = [[-5]], target = -2)
        print(r)
        self.assertEqual(r, False)

    def xtest_findPeakElement(self):
        from BinarySearch import Solution as sbs
        so  =   sbs()
        r=so.findPeakElement([2,1])
        print(r)
        self.assertEqual(r,0)
        r=so.findPeakElement([1,2,1,2,1])
        print(r)
        # self.assertEqual(r,0)
    
    def xtest_singleNonDuplicate(self):
        from BinarySearch import Solution as sbs
        so  =   sbs()
        r=so.singleNonDuplicate([1,1,2,3,3,4,4])
        print('r=',r)
        r=so.singleNonDuplicate([1,2,2,3,3,4,4])
        print('r=',r)
        r=so.singleNonDuplicate([1,1,2,2,3,3,4,4,5])
        print('r=',r)


    def xtest_bi(self):
        from BinarySearch import Solution as sbs
        so  =   sbs()
        r=  so.searchInsert(nums = [1,3,5,6], target = 5)
        print(r, "==2")
        r=  so.searchInsert(nums = [1,3,5,6], target = 2)
        print(r, "==1")
        r=  so.searchInsert(nums = [1,3,5,6], target = 7)
        print(r, "==4")
        r=  so.searchInsert(nums = [1 ], target = 1 )
        print(r)
        r=  so.searchInsert(nums = [1,3 ], target = 1 )
        print("0==",r)

'''
python -m unittest  tests  -k TestLinkList
'''
class TestLinkList(unittest.TestCase):
    def setUp(self) -> None:
        print("[+]Running test....")
        from LinkedList import Solution as SLL
        self.so         =   SLL(None)
        self.t          =   timer("LinkList")
        return super().setUp()
    
    def tearDown(self) -> None:
        self.t.stop()
        return super().tearDown()

    def test_isPalindrome(self):
        listA = ListNode.list_to_ListNode([10,1,3,5,6,77,100])
        # ListNode.print(listA)
        self.so.head = listA
        print(self.so.getRandom())
        print(self.so.getRandom())
        print(self.so.getRandom())
        print(self.so.getRandom())

    def xtest_isPalindrome(self):
        listA = ListNode.list_to_ListNode([1,2,3,2,1])
        # ListNode.print(listA)
        print(self.so.isPalindrome(listA))
        listA = ListNode.list_to_ListNode([1,2,2,1])
        # ListNode.print(listA)
        print(self.so.isPalindrome(listA))
        listA = ListNode.list_to_ListNode([1,2,])
        # ListNode.print(listA)
        print(self.so.isPalindrome(listA))
        listA = ListNode.list_to_ListNode([1,1])
        # ListNode.print(listA)
        print(self.so.isPalindrome(listA))

    def xtest_getIntersectionNode(self):
        listA = ListNode.list_to_ListNode([4,1,8,4,5])
        listB = ListNode.list_to_ListNode([5,6,1,8,4,5])
        r=self.so.getIntersectionNode(listA, listB)
        if  r :
            print("node val {}".format(r.val))
        else:
            print("没有交集")
    def xtest_mergeKLists(self):
        inp     =   [[1,4,5],[1,3,4],[2,6]]
        print("输入 {}".format(inp))
        r   =   []
        for li in inp:
            r.append(ListNode.list_to_ListNode(li))
        s       =   self.so.mergeKLists(r)
        ListNode.print(s)
        print("result={} inp = {}".format(s, inp))

        inp     =   [[],[],[]]
        print("输入 {}".format(inp))
        r   =   []
        for li in inp:
            r.append(ListNode.list_to_ListNode(li))
        s       =   self.so.mergeKLists(r)
        ListNode.print(s)
        print("result={} inp = {}".format(s, inp))

    def xtest_removeDuplicates(self):
        inp     =   [0,0,1,1,1,2,2,3,3,4]
        print("输入 {}".format(inp))
        s       =   self.so.removeDuplicates(inp)
        print("s={} inp = {}".format(s, inp))

        inp     =   [1,1,2]
        print("输入 {}".format(inp))
        s       =   self.so.removeDuplicates(inp)
        print("s={} inp = {}".format(s, inp))
    
    #def test_reverseBetween(self):
    def xtest_MedianFinder(self):
        mf  =   MedianFinder()
        # mf.addNum(5)
        # mf.addNum(7)
        # print("mf = {}".format(mf.findMedian()))
        # mf.addNum(1)
        # mf.addNum(3)
        # print("mf = {}".format(mf.findMedian()))
        # ---------------
        # mf.addNum(1)
        # mf.addNum(2)
        # print("mf = {}".format(mf.findMedian()))
        # mf.addNum(3)
        # print("mf = {}".format(mf.findMedian()))
        # ---------------
        mf.addNum(-1)
        print("mf = {}".format(mf.findMedian()))
        mf.addNum(-2)
        print("mf = {}".format(mf.findMedian()))
        mf.addNum(-3)
        print("mf = {}".format(mf.findMedian()))
        mf.addNum(-4)
        print("mf = {}".format(mf.findMedian()))
        mf.addNum(-5)
        print("mf = {}".format(mf.findMedian()))

    def xtest_reverseBetween(self):
        inp         =   ListNode.list_to_ListNode([1,2,3,4,5])
        ListNode.print(inp,"[+]input:")
        ret         =   self.so.reverseBetween(inp,2,4)
        ListNode.print(ret,"[+]result:")

        inp         =   ListNode.list_to_ListNode([3,5])
        ListNode.print(inp,"[+]input:")
        ret         =   self.so.reverseBetween(inp,1,1)
        ListNode.print(ret,"[+]result:")

        inp         =   ListNode.list_to_ListNode([3,5])
        ListNode.print(inp,"[+]input:")
        ret         =   self.so.reverseBetween(inp,1,2)
        ListNode.print(ret,"[+]result:")

        inp         =   ListNode.list_to_ListNode([1,2,3])
        ListNode.print(inp,"[+]input:")
        ret         =   self.so.reverseBetween(inp,1,2)
        ListNode.print(ret,"[+]result:")

        inp         =   ListNode.list_to_ListNode([1,2,3,4,5])
        ListNode.print(inp,"[+]input:")
        ret         =   self.so.reverseBetween(inp,1,2)
        ListNode.print(ret,"[+]result:")


    def xtest_partition(self):
        inp         =   ListNode.list_to_ListNode([1,4,3,2,5,2])
        ListNode.print(inp,"[+]input:")
        ret         =   self.so.partition(inp,3 )
        ListNode.print(ret,"[+]result:")
        
        
        inp         =   ListNode.list_to_ListNode([1,4,1,1])
        ListNode.print(inp,"[+]input:")
        ret         =   self.so.partition(inp,3 )
        ListNode.print(ret,"[+]result:")
    
    def xtest_deleteDuplicates(self):
        so      =   Solution()
        print("running test")
        ret     =   so.deleteDuplicates1(ListNode.list_to_ListNode([1,1,1]))
        # ret     =   so.deleteDuplicates1(ListNode.list_to_ListNode([1,1,2]))
        ListNode.print(ret)

# l = ["the","day","is","is","sunny","the","the","the","sunny","is","is"]
# import collections
# c = collections.Counter(l)
# d = c.most_common(4)
# order_items = sorted(d, key=lambda x: (-x[1], x[0]))
# out = [k for k,v in order_items]
