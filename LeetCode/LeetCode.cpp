// LeetCode.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>
#include "CTwoSum.h"
#include "CAddTwoNumbers.h"
#include "ClengthOfLongestSubstring.h"
#include "BinaryTree.h"
void test_CTwoSum()
{
    vector<int> nums = { 3,2,4 };
    nums = { 3,1,4,22,2 };
    //nums = { 3,3 };
    vector<int> r = CTwoSum::twoSum(nums, 6);
    for (auto i : r) {

        std::cout << "i " << i << "\n";
    }
}

void test_CAddTwoNumbers()
{
    //CAddTwoNumbers;
}

void test_ClengthOfLongestSubstring()
{
    int max = ClengthOfLongestSubstring::lengthOfLongestSubstring("abba");
    std::cout << "max = " << max<<std::endl;
}
#include"CLinkList.h"
//using namespace 
void test_remove_dup()
{
#include<vector>
    vector<int> nums;
    nums.push_back(2);
    nums.push_back(3);
    nums.push_back(4);
    nums.pop_back();
    for (auto i : nums)
    {
        std::cout << i << std::endl;
    }

    using ListNode = LinkList::CLinkList::ListNode;
    ListNode h(1),a(2),b(2),c(3),d(3),e(4),f(5);
    //ListNode h(1), a(2),b(2);
        //, b(1), c(1), d(1), e(2), f(2);

    h.next = &a;
    //a.next = &b;
   // b.next = nullptr;
    a.next = &b;
    b.next = &c;
    c.next = &d;
    d.next = &e;
    e.next = &f;
    f.next = nullptr;

    ListNode*r = LinkList::CLinkList::deleteDuplicates(&h);
    std::cout << r->next << std::endl;
}

void test_partition()
{
    using ListNode = LinkList::CLinkList::ListNode;
    // [3,4,0,2, 2,1,2,3 ,4] 
   /* ListNode h(3), a(4), b(0), c(2), d(2), e(1),f(2),g(3),i(4);
    h.next = &a;
    a.next = &b;
    b.next = &c;
    c.next = &d;
    d.next = &e;
    e.next = &f;
    f.next = &g;
    g.next = &i;
    i.next = nullptr;*/

    ListNode h(1), a(4), b(3), c(2), d(5), e(2);
    h.next = &a;
    a.next = &b;
    b.next = &c;
    c.next = &d;
    d.next = &e;
    e.next = nullptr;
    /*h.val = 2;
    a.val = 1;
    a.next = nullptr;*/
    ListNode* r = LinkList::CLinkList::partition(&h, 3);
}
//using namespace LinkedList;
//void test_swap_nodes()
//{
//    List l;
//    l.insert(1);
//    l.insert(2);
//    l.insert(3);
//    l.insert(4);
//    l.dump();
//    ListNode* r=CLinkLists::swapPairs(l.get_head());
//    l.dump(r);
//}
void test_vec()
{
    vector<int> a = { 1,2 };
    vector<int> b = { 3,4 };
}
using namespace letcoode;
void test_bst()
{/*
    vector<int> x = { 3, 1, 2 };
    TreeNode* t = sortedArrayToBST(x);*/
    TreeNode a(1);
    TreeNode b(3);
    TreeNode c(2);
    a.left = &b;
    b.right = &c;
    recoverTree(&a);
    //isCousins(t, 8, 12);
    /*x = { 2,1 };
    x = {1,2,3};
    vector<int> y = { 3,2,1 };
    TreeNode* t = sortedArrayToBST(x);
    TreeNode* u = sortedArrayToBST(y);
    leafSimilar(t, u);*/
    /*diameterOfBinaryTree(t);
    findMode(t);
    TreeNode* left = t->left;
    TreeNode* right = t->right;
    TreeNode* c = lowestCommonAncestor(t, left, right);
    if (c != nullptr)
        printf("common ancestor is %d", c->val);
    else
        printf("it's null\n");*/
}
int main()
{
    test_bst();
    //test_partition();
    //test_remove_dup();
    //test_ClengthOfLongestSubstring();
	//test_swap_nodes();
}

// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单

// 入门使用技巧: 
//   1. 使用解决方案资源管理器窗口添加/管理文件
//   2. 使用团队资源管理器窗口连接到源代码管理
//   3. 使用输出窗口查看生成输出和其他消息
//   4. 使用错误列表窗口查看错误
//   5. 转到“项目”>“添加新项”以创建新的代码文件，或转到“项目”>“添加现有项”以将现有代码文件添加到项目
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文件