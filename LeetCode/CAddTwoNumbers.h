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
    // ��ջpushһ�� val������ջ��
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
        /*��ʼ��һ���������ͷ����
        ��ʼ��һ����λֵ 0

        1. ������������ ������һ����Ϊ�յ�ʱ�򣬽���
            ���Ͻ�λֵ = ��� = 3 + 9 + 9 = 21
            ��� % 10 �õ���ǰ�ڵ��ֵ
            ��� / 10 �õ���һ�� ��λֵ
            �����ڵ㣬���뵽����
            �ƶ���������ָ��

        ��λֵ��Ϊ0����ӵ��ڵ㵽�������
        ����ͷ����	*/
    public:
        static ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
            ListNode* ret = nullptr, * head = nullptr;
            int calc = 0;   // ��λֵ
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