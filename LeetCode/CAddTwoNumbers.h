#pragma once
#ifndef ADDTOWNUMBER_H
#define ADDTOWNUMBER_H


#include<vector>
#include<map>
#include<iostream>
using namespace std;
//*
// * Definition for singly-linked list.
// * struct ListNode {
// *     int val;
// *     ListNode *next;
// *     ListNode() : val(0), next(nullptr) {}
// *     ListNode(int x) : val(x), next(nullptr) {}
// *     ListNode(int x, ListNode *next) : val(x), next(next) {}
// * };
// 
/*
[9,9,9,9,9,9,9]
[9,9,9,9]
Output
[8,9,9,9,0,0,0]
Expected
[8,9,9,9,0,0,0,1]
*/
namespace leetcode {

    struct ListNode {
        int val;
        ListNode* next;
        ListNode() : val(0), next(nullptr) {}
        ListNode(int x) : val(x), next(nullptr) {}
        ListNode(int x, ListNode* next) : val(x), next(next) {}
    };
    ListNode* next(ListNode* cur) {
        if (cur == nullptr)
            return nullptr;
        return cur->next;
    }
    // 向栈push一个 val，返回栈顶
    ListNode* push(ListNode* cur, int val) {
        ListNode* new_node = new ListNode(val, nullptr);
        if (cur != nullptr)
        {
            cur->next = new_node;
        }
        return new_node;
    }
    class CAddTwoNumbers
    {
        /*初始化一个结果链表、头链表
        初始化一个进位值 0

        1. 遍历两个链表， 当其中一个不为空的时候，进入
            加上进位值 = 结果 = 3 + 9 + 9 = 21
            结果 % 10 得到当前节点的值
            结果 / 10 得到下一个 进位值
            创建节点，加入到链表
            移动两个链表指针

        进位值不为0，添加到节点到结果链表
        返回头链表	*/
    public:
        static ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
            ListNode* ret = nullptr, * head = nullptr;
            int calc = 0;   // 进位值
            while (l1 != nullptr || l2 != nullptr) {
                int tmp = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + calc;
                ret = push(ret, tmp % 10);
                if (head == nullptr)
                    head = ret;
                calc = tmp / 10;
                if (l1 != nullptr)
                    l1 = l1->next;
                if (l2 != nullptr)
                    l2 = l2->next;
            }
            if (calc != 0)
                push(ret, calc);
            return head;
        }
    };


}

#endif // !ADDTOWNUMBER_H