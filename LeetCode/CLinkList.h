#pragma once
#include<vector>
#include<iostream>
namespace LinkList {


	class CLinkList
	{
	public:
		// Definition for singly-linked list.
		//template<class T>
		struct ListNode {
			int val;
			ListNode* next;
			ListNode() : val(0), next(nullptr) {}
			ListNode(int x) : val(x), next(nullptr) {}
			ListNode(int x, ListNode* next) : val(x), next(next) {}
		};
		
		static ListNode* next(ListNode* node) {
			if (node != nullptr)
				return node->next;
			return nullptr;
		}
		static ListNode* insert(ListNode* node,int data) {
			ListNode* ret = new ListNode(data, node);
			if (node)
				node->next = ret;
			return ret;
		}

	public:
		// remove n-th node from the end of list . return the head
		// find the node and it's previous node , change prev node.next = cur.next
		// edge situation : the removed node is the head .
		// https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/
		static ListNode* removeNthFromEnd(ListNode* head, int n) {
			using std::vector;
			vector<ListNode*> nodes;
			ListNode* ret = head, * cur_node = nullptr, *prev_node=nullptr,* tmp_head=head;
			while (head != NULL) {
				nodes.push_back(head);
				if (head->next == nullptr)
					break;
				head = head->next;
			}
			int remove_index = nodes.size() - n;
			if (remove_index < 0) {
				return tmp_head;
			}
			else if (remove_index == 0) {
				// remove the first node 
				ret = tmp_head->next;
				//free(tmp_head);
			}
			else {
				// get previous 
				prev_node = nodes[remove_index - 1];
				cur_node = nodes[remove_index];
				prev_node->next = cur_node->next;
				//free(cur_node);
			}
			return ret;
		}
		/*
		merge two sorted list into one sorted list. iterate over two list,
		find the smaller one and insert it into the new list, change list pointers.
		*/
		static ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
			ListNode* head = nullptr, * cur_node = nullptr,
				*cur_l1= list1, *cul_l2= list2;
			while (cur_l1 || cul_l2) {
				int cur_val_1 = 0, cur_val_2 = 0;
				ListNode* tmp = nullptr;
				if (cur_l1 != nullptr)
					cur_val_1 = cur_l1->val;
				if (cul_l2 != nullptr)
					cur_val_2 = cul_l2->val;
				// bost list not empty 
				if (cur_l1 && cul_l2) {
					if (cur_val_1 < cur_val_2) {
						tmp = insert(cur_node, cur_val_1);
						cur_l1 = cur_l1->next;
					}
					else {
						tmp = insert(cur_node, cur_val_2);
						cul_l2 = cul_l2->next;
					}
					cur_node = tmp;
					if (head == nullptr) {
						 head = tmp;
					}
					continue;
				}
				// list 1 not empty, concat it 
				else if (cur_l1) {
					if (cur_node) {
						cur_node->next = cur_l1;
					}
					else {
						head = cur_node = cur_l1;
					}
					break;
				}
				// list 1 not empty, concat it 
				else if (cul_l2) {
					if (cur_node) {
						cur_node->next = cul_l2;
					}
					else {
						head = cur_node = cul_l2;
					}
					break;
				}
			}
			return head;
		}
		// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
		// remove all duplicated number from a sorted list, return it's head.
		// my bad: it wishes to remove all node which have duplicated value. thus: [1,1,2]=> [2]
		// we need four pointers,and one bool flag has_dup. 
		// first is for store the original head
		// second is for the prev node, third is for the cur node, fourth is for next node

		static ListNode* deleteDuplicates(ListNode* head) {
			ListNode* next = nullptr;
			ListNode* top = nullptr;
			ListNode* tmp_stack[400] = { 0 };
			int sp = -1;						// stack pointer
			bool has_dup = false;
			if (head == nullptr || head->next == nullptr)
					return head;
			next = head->next;
			tmp_stack[++sp] = head;	// push first node to stack 
			while (next) {			// loop until we hit the last node
				if (sp > -1) {
					// the stack is not empty
					top = tmp_stack[sp];	// get the top node from stack
					if (top->val == next->val) {
						// mark duplicate node found, remove next from list, update top's next 
						has_dup = true;
						top->next = next->next;
						next = next->next;
					}
					else {
						// we need to check if previously found a duplicate node
						if (has_dup) {
							// stack pop
							ListNode* tmp = top;
							if (sp > 0) {
								top = tmp_stack[--sp];
							}
							else {
								top = nullptr;
								--sp;
							}
							// reset top's next 
							if (top)
								top->next = next;
						}
						// mark not duplicated
						has_dup = false;
						// not duplicate node, push the next to stack 
						tmp_stack[++sp] = next;
						next = next->next;
					}

				}
				else {
					// stack is empty, push one node 
					tmp_stack[++sp] = next;
					next = next->next;
				}
			}
			// the last round out , 
			if (has_dup) {
				// stack pop
				ListNode* tmp = top;
				if (sp > 0) {
					top = tmp_stack[--sp];
				}
				else {
					top = nullptr;
					--sp;
				}
				// set 
				if (top)
					top->next = next;
			}
			if (sp > -1)
				return tmp_stack[0];
			return nullptr;
		}
		// https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/
		// I resolved yesterday ... but codes were deleted...
		static ListNode* deleteDuplicates2(ListNode* head) {
			ListNode *cur = head, *next = nullptr;
			if (head == nullptr || head->next == nullptr)
				return head;
			next = cur->next;
			while (next) {
				// loop until we hit the end 
				if (cur->val == next->val) {
					// update cur's next
					cur->next = next->next;
					next = next->next;
					continue;
				}
				cur = next;
				next = next->next;
			}
			return head;
		}
		
		// https://leetcode.com/problems/partition-list/
		/*
		prev =nul, cur =1, 
		prev=1, cur=4
		if prev > cur  and prev >= 3 and cur != 3
			exchange prev and cur 
		else
			prev = cur
			cur = cur->next
		*/
		static bool check_partition(ListNode* head, int x) {
			bool small = true, great = false, has_changed = false, ret = true;
			while (head != nullptr) {
				if (has_changed == false && small && head->val < x) {
					head = head->next;
					continue;
				}
				else {
					small = false;
					has_changed = true;
					great = true;
				}
				if (has_changed && great && head->val >= x) {
					head = head->next;
					continue;
				}
				else if (has_changed ){
					return false;
				}
			}
			return ret;
		}
		static ListNode* partition(ListNode* head, int x) {
			ListNode* small_head = new ListNode(0);
			ListNode* great_head = new ListNode(0);
			ListNode* cur_small = small_head, * cur_great = great_head;
			if (head == nullptr || head->next == nullptr)
				return head;
			while (head != nullptr) {
				if (head->val < x) {
					// insert into small;
					cur_small->next = head;
					cur_small = head;
					head = head->next;
				}
				else {
					cur_great->next = head;
					cur_great = head;
					head = head->next;
				} 
			}
			cur_great->next = NULL;
			cur_small->next = great_head->next;
			if(small_head->next)
				return small_head->next;

			return great_head->next;
		}

		static ListNode* reverseList(ListNode* head) {
			// given a list , reverse it.
			// we need 3 nodes: prev, cur, tmp . let tmp = cur->next, cur->next= prev, prev = cur, cur = tmp
			if (head == nullptr || head->next == nullptr)
				return head;
			ListNode* prev=nullptr, *cur=head, *tmp;
			while(cur != nullptr) {
				tmp = cur->next;
				cur->next = prev;
				prev = cur;
				cur = tmp;
			}
			return prev;
		}

		// https://leetcode.com/problems/reverse-linked-list-ii/

		static ListNode* reverseBetween(ListNode* head, int left, int right) {
			// like reverse a link list, we need to find where the break nodes are. break_1, break_2
			// between break_1 and break_2, reverse the list, and then, hook it back to where it was break.
			if (head == nullptr || head->next == nullptr || left >= right)
				return head;
			int i = 1;
			ListNode * cur = head, *break_1 ,*break_2 = nullptr ;
			ListNode* prev=nullptr,  *tmp;
			while(cur != nullptr) {
				if(i > right)
				{
					break;
				}
				if (i < left) {
					// before reverse start
					++i;
					prev = cur;
					cur = cur->next;
					continue;
				}
				// i >= left , begin reverse procedure
				if (i == left) {
					// save the break point 1 , 2
					break_1 = prev;
					break_2 = cur;
				}
				++i;
				tmp = cur->next;
				cur->next = prev;
				prev = cur;
				cur = tmp;
			}
			// need to fix two nodes: 
			if (break_1) {
				break_1->next = prev;
			}
			if (break_2) {
				break_2->next = cur;
			}
			if (left == 1) {
				// reverse from first position
				return prev;
			}
			else {
				return head;
			}
		}

		// https://leetcode.com/problems/linked-list-cycle/
		// 141. Linked List Cycle
		/*Given head, the head of a linked list, determine if the linked list has a cycle in it.

	There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

	Return true if there is a cycle in the linked list. Otherwise, return false.
		solution1 ： 用两个循环来找是否有环. 类似冒泡排序算法 // 超时
		solution2 ： 用map： 34 ms, faster than 5.29% of C++ online submissions for Linked List Cycle.
		solution3 ： 赛跑。 在一个环里，a跑得比b快一倍，那么一定时间后，a会再次遇到b。 Runtime: 12 ms, faster than 74.89% of C++ online submissions for Linked List Cycle.
	*/
		bool hasCycle(ListNode *head) {
			if(!head || head->next == nullptr)	
				return false;
			ListNode * fast=head, *slow=head;
			while(fast && fast->next) {
				fast = fast->next->next;
				slow = slow->next;
				if(fast == slow)
					return true;
			}
			return false;

			
			// if(!head || head->next == nullptr)	
			// 	return false;
			// map<ListNode*, int> m;
			// while(head) {
			// 	auto r = m.find(head);
			// 	if(r != m.end()) 
			// 		return true;
			// 	m[head] = head->val;
			// 	head = head->next;
			// }
			// return false;


			// bool has_cycle = false;
			// ListNode* cur=head, *iter = nullptr;
			// while (cur && !has_cycle)
			// {
			// 	iter = cur->next;
			// 	while(iter) {
			// 		if(iter->next == cur) {
			// 			has_cycle = true;
			// 			break;
			// 		}
			// 		iter = iter->next;
			// 	}
			// 	cur = cur->next;
			// }
			// return has_cycle;
			
		}
	};
};
