import unittest
from LinkedList import  *
import time
import os, datetime

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


class TestLinkList(unittest.TestCase):
    def setUp(self) -> None:
        print("[+]Running test....")
        self.so         =   Solution()
        self.t          =   timer("LinkList")
        return super().setUp()
    
    def tearDown(self) -> None:
        self.t.stop()
        return super().tearDown()
    
    def test_partition(self):
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


