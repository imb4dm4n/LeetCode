import unittest
from LinkedList import  *
import time
import os, datetime
from DynamicProgram import Solution as SD
from BinaryTree import Solution as SBT
from BinaryTree import TreeNode

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

class TestAlgorithm(unittest.TestCase):
    def test_topKFrequent(self):
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

class TestBinaryTree(unittest.TestCase):
    def test_inorderTraversal(self):
        so      =   SBT()
        root    =   TreeNode(1)
        left    =   TreeNode(2)
        root.left=left
        ret     =    so.inorderTraversal(root)
        print(ret)

class TestDynamicProgram(unittest.TestCase):
    def setUp(self) -> None:
        self.so     =   SD()
        self.t          =   timer("DynamicProgram")
        return super().setUp()
    
    def tearDown(self) -> None:
        self.t.stop()
        return super().tearDown()
    
    def test_numDecodings(self):
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
    
    def test_reverseBetween(self):
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


