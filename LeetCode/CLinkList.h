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
			/*
			bubbling sort : push small one from the bottom to top 
			condition: prev.val >= x and prev.val > cur.val
			*/
			ListNode* ret = head, * prev = nullptr, * cur = head, * end = nullptr;
			if (head == nullptr || head->next == nullptr)
				return head;
			
			ListNode* top = nullptr;
			ListNode* tmp_stack[300] = { 0 };
			int sp = -1;
			// push all nodes to stack
			while (cur != nullptr) {
				tmp_stack[++sp] = cur;
				cur = cur->next;
			}
			int saved_sp = sp;	// decrease saved_sp by 1 each time
			//while (saved_sp > 0) {
			while (1) {
				// 
				sp = saved_sp;
				while (sp > 0) {
					top = tmp_stack[sp];
					if (sp > 0) {
						// there is prev node 
						prev = tmp_stack[sp - 1];
 						if (top->val < x && prev->val >=x ) {
							// exchange the value 
							int tmp = prev->val;
							prev->val = top->val;
							top->val = tmp;
						}
					}
					--sp;
				}
				if (check_partition(head, x))
					break;
				//--saved_sp;
			}
			return head;

		}
	};
};
