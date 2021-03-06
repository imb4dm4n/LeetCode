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
        // https://leetcode.com/problems/rotate-list/
        static ListNode* rotateRight(ListNode* head, int k) {
            ListNode* arr_p[600]={0};   // number of node is less than 500
            int n = 0;// number of nodes in the list
            ListNode* tmp = head;
            if(k==0 || head == nullptr) // nothing to rotate
                return head;
            while(head != nullptr) {
                arr_p[n++] = head;  // store every nodes pointer
                head = head->next;
            }
            head = tmp;
            int pos = n - k % n; // calculate the actual rotate number;
            if(n ==1 || pos == n)   // 1 node or roate round is equal to number of nodes
                return tmp;
            arr_p[pos - 1]->next = nullptr;
            arr_p[n - 1]->next = arr_p[0];  // the last node of the tail part of list, should change it's next
            return arr_p[pos];
        }
	};

};

