// LeetCode.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>
#include "CTwoSum.h"
#include "CAddTwoNumbers.h"
#include "ClengthOfLongestSubstring.h"
#include "BinaryTree.h"
#include "CConcurrency.h"
void test_concurrency()
{
    using namespace CConcurrency;
    ZeroEvenOdd obj(10);
    auto print = [](int num) {
        std::cout<< num;
    };
    auto worker0 = [&]() {
        obj.zero(print);
        //std::cout<<" worker0 exit"<<std::endl;
    };
    auto worker1 = [&]() {
        obj.even(print);
        //std::cout<<" worker1 exit"<<std::endl;
    };
    auto worker2 = [&]() {
        obj.odd(print);
        //std::cout<<" worker2 exit"<<std::endl;
    };
    std::thread p(worker0);
    std::thread p1(worker1);
    std::thread p2(worker2);
    p.join();
    p1.join();
    p2.join();

}
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

void test_random_list()
{
    //LinkList::CLinkList l;
    LinkList::CLinkList::Solution s(nullptr);
    s.getRandom();
}
using namespace letcoode;
void test_bst()
{/*
    vector<int> x = { 3, 1, 2 };
    TreeNode* t = sortedArrayToBST(x);*/
    vector<int> r = { 3,1,5,-1,2,4,6 };
    r = { -85,0,59,0,0,0,71,0,0,0,0,0,0,0,85 };
    r = { 5, 4, 8, 11, 0, 13, 4, 7, 2, 0, 0, 5, 1 };
    TreeNode* root = create_bt(r, 0);
    pathSum(root, 22);
    isValidBST(root);
    recoverTree(root);
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
    string s = "hlelo";
    string* l = new string("asdjdaos qwoejqiwoe2109093z zxjczoasjiod2");
    std::cout << l->c_str() << s.c_str();
    //test_random_list();
    //test_concurrency();
    // test_bst();
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