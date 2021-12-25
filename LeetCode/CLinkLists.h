#pragma once
#include<iostream>
#include<string>
using namespace std;

namespace LinkedList {
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
    // 队列
    class List {
    public:
        List() { head = nullptr; }
        ListNode* insert(int val) // 插入一个值到队列
        {
            ListNode* tmp = new ListNode(val);
            if (head == nullptr)
            {
                // empty list 
                head = cur = tmp;
                return tmp;
            }
            if (cur) {
                cur->next = tmp;
                cur = tmp;
            }
            return tmp;
        }
        void dump(ListNode* h=nullptr)
        {
            ListNode* tmp = head;
            if (h)
                tmp = h;
            while (tmp) {
                std::cout << "list val " << tmp->val << std::endl;
                tmp = tmp->next;
            }
        }
        ListNode* get_head() const { return head; }
        ListNode* head;// 队列头
        ListNode* cur;// 当前指针
    };
	class CLinkLists
	{
        // https://leetcode.com/problems/swap-nodes-in-pairs/
        // swap a pair of nodes [ 1,2,3,4] => [2,1,4,3]
        // 
    public:
        static ListNode* swapPairs(ListNode* head) {
            ListNode* ret = nullptr, * cur = head, * next = nullptr, * prev=nullptr;
            if (head == nullptr || head->next == nullptr)
                return head;
            next = cur->next;
            while (cur && next) {
                // swap two nodes 1->next = 2->next, 2->next = 1
                cur->next = next->next;
                next->next = cur;
                // once swaped, if we have previous nodes, it's next should changed into next .
                if (prev)
                    prev->next = next;
                if (ret == nullptr)
                    ret = next;
                prev = cur;
                cur = cur->next;
                if (cur)
                    next = cur->next;
                else
                    next = nullptr;
            }
            return ret;
        }
	};

};

