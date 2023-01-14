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
python -m unittest  tests  -k TestArray
'''
class TestArray(unittest.TestCase):
    def test_matrixBlockSum(self):
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
python -m unittest  tests  -k TestStrings
'''
class TestStrings(unittest.TestCase):
    def test_minDeletionSize(self):
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
    def test_canCompleteCircuit(self):
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
    def test_countSubTrees(self):
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
class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.so     =   GS()
        self.t          =   timer("Graph")
        return super().setUp()
    
    def tearDown(self) -> None:
        self.t.stop()
        return super().tearDown()

    def test_validPath(self):
        temps   =   [[0,1],[1,2],[2,0]]
        ret = self.so.validPath(temps.__len__(),temps,0,2)
        print(ret)
        temps   =   [[0,1],[0,2],[3,5],[5,4],[4,3]]
        ret = self.so.validPath(temps.__len__(),temps,0,5)
        print(ret)
        temps   =   [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
        ret = self.so.validPath(temps.__len__(),temps,7,5)
        print(ret)
        return

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

    def test_dailyTemperatures(self):
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
    
    def test_minStoneSum(self):
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

class TestLinkList(unittest.TestCase):
    def setUp(self) -> None:
        print("[+]Running test....")
        self.so         =   Solution()
        self.t          =   timer("LinkList")
        return super().setUp()
    
    def tearDown(self) -> None:
        self.t.stop()
        return super().tearDown()

    def test_removeDuplicates(self):
        inp     =   [0,0,1,1,1,2,2,3,3,4]
        print("输入 {}".format(inp))
        s       =   self.so.removeDuplicates(inp)
        print("s={} inp = {}".format(s, inp))

        inp     =   [1,1,2]
        print("输入 {}".format(inp))
        s       =   self.so.removeDuplicates(inp)
        print("s={} inp = {}".format(s, inp))
    
    #def test_reverseBetween(self):
    def test_MedianFinder(self):
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

l = ["the","day","is","is","sunny","the","the","the","sunny","is","is"]
import collections
c = collections.Counter(l)
d = c.most_common(4)
order_items = sorted(d, key=lambda x: (-x[1], x[0]))
out = [k for k,v in order_items]
