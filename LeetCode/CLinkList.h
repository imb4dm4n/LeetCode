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
		// https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
		// 116. Populating Next Right Pointers in Each Node
		/*You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
		Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

		Initially, all next pointers are set to NULL.
		solution1: use queue. 直接超时。
		solution2：先测量树的深度h，然后从1到h深度遍历二叉树，记录prev节点和cur节点，
		若prev节点不为空，则prev->next=cur，迭代到结束。 一次通过
		Runtime: 24 ms, faster than 63.47% of C++ online submissions for Populating Next Right Pointers in Each Node.
	Memory Usage: 16.7 MB, less than 85.79% of C++ online submissions for Populating Next Right Pointers in Each Node.
		*/
		class Node {
		public:
			int val;
			Node* left;
			Node* right;
			Node* next;

			Node() : val(0), left(NULL), right(NULL), next(NULL) {}

			Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

			Node(int _val, Node* _left, Node* _right, Node* _next)
				: val(_val), left(_left), right(_right), next(_next) {}
		};
		#include<queue>
		using std::queue;
		// 计算树的最大高度
		void tree_get_height(Node* root,int cur_dep, int& max_dep) {
			if(!root)
				return;
			cur_dep++;
			if(cur_dep > max_dep)
				max_dep = cur_dep;
			tree_get_height(root->left, cur_dep, max_dep);
			tree_get_height(root->right, cur_dep, max_dep);
		}
		// 连接树的每一层节点
		/*
			@prev			前一个节点
			@cur			当前节点
			@target_level	目标层
			@cur_level		当前所在层
		*/
		void tree_connect(Node*& prev, Node* cur, int target_level, int cur_level) {
			if(!cur || cur_level > target_level)
				return;
			cur_level++;
			// 递归达到目标层，修改节点
			if(prev && cur_level == target_level) {
				prev->next = cur;
				prev = cur;
			}
			// 初始化
			else if(prev == nullptr && cur_level == target_level) {
				prev = cur;
			}
			tree_connect(prev, cur->left, target_level, cur_level);
			tree_connect(prev, cur->right, target_level, cur_level);
		}
		Node* connect(Node* root) {
			if(!root)
				return root;
			int tree_height = 0, cur_dep = 0;
			tree_get_height(root, cur_dep, tree_height);
			for(int i=1; i <= tree_height; ++i) {
				Node* prev=nullptr;
				cur_dep = 0;
				tree_connect(prev, root, i, cur_dep);
			}
			return root;
			// if(!root)
			// 	return root;
			// queue<Node*> q;
			// q.push(root);
			// while(!q.empty()) {
			// 	int size = q.size();
			// 	Node* prev = nullptr;
			// 	while(size > 0) {
			// 		Node* head = q.front();
			// 		if(prev != nullptr)
			// 			prev->next = head;
			// 		prev = head;
			// 		size -= 1;
			// 		q.push(head->left);
			// 		q.push(head->right);
			// 	}
			// }
			// return root;
		}

		// https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/submissions/
		// 117. Populating Next Right Pointers in Each Node II
		/*
			和前一题一样，不同的是这颗不是完全二叉树。 某些层节点不全。
			直接提交前一题即可。
			Runtime: 36 ms, faster than 5.46% of C++ online submissions for Populating Next Right Pointers in Each Node II.
			Memory Usage: 17.4 MB, less than 81.34% of C++ online submissions for Populating Next Right Pointers in Each Node II.
		*/

	};
};
